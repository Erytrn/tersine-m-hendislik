\# 🐳 Aşama 4: Docker Mimarisi ve Konteyner Güvenliği



Bu aşamada Gitleaks'in Docker dağıtım mimarisini, izolasyon sınırlarını ve konteyner güvenliğini analiz ettim.



\### 1. Docker İmajı ve Katman (Layer) Analizi

\*\*Analiz:\*\* Gitleaks Docker imajı incelendiğinde çok hafif ve güvenli bir yapı (Multi-stage build) kullanıldığı görülmektedir.

\* \*\*Base Layer (Temel Katman):\*\* Genellikle `Alpine Linux` (sadece \~5 MB) veya `scratch` (boş imaj) kullanılır. Bu, gereksiz işletim sistemi araçlarını barındırmadığı için saldırı yüzeyini (attack surface) minimuma indirir.

\* \*\*Application Layer:\*\* Go ile derlenmiş "Statically Linked" tek bir `gitleaks` binary dosyasıdır. Dış bağımlılığı yoktur.



\### 2. İzolasyon ve Erişim Sınırları

\*\*Analiz:\*\* Gitleaks konteyneri çalıştığında, varsayılan olarak host sistemin dosyalarına \*\*erişemez\*\*. Tarama yapabilmesi için hedef kod deposunun (repo) konteyner içine "Volume Mount" yöntemiyle (örneğin: `-v $(pwd):/path`) dışarıdan bağlanması (map edilmesi) gerekir. Konteyner sadece bu bağlanan dizini okuyabilir, sistemin geri kalanı (Kernel ve diğer klasörler) izole durumdadır.



\### 3. Kritik Karşılaştırma: VM vs Docker vs Kubernetes (K8s)

Hocamızın yönergesindeki kritik farklar şu şekilde özetlenebilir:

\* \*\*Sanal Makine (VM):\*\* Tam bir Donanım/İşletim Sistemi (Hypervisor) simülasyonudur. İzolasyonu en yüksektir ama hantal ve yavaştır (Gigabaytlarca yer kaplar).

\* \*\*Docker:\*\* İşletim sistemi çekirdeğini (Kernel) paylaşır, sadece uygulamayı ve bağımlılıklarını izole eder. Saniyeler içinde açılır ve çok hafiftir (Megabayt boyutunda).

\* \*\*Kubernetes (K8s):\*\* Docker'ın (veya diğer konteynerlerin) ağabeyidir. Tek bir konteyner değil, binlerce konteynerin orkestrasyonunu, çökme durumunda otomatik yeniden başlatılmasını ve yük dağıtımını (Load Balancing) yönetir.



\### 4. Sıkılaştırma (Hardening) Önerisi

Ortamı en güvenli hale getirmek için Gitleaks konteyneri çalıştırılırken `root` yetkileri kısıtlanmalı (kendi kullanıcısı ile çalıştırılmalı) ve host makineden bağlanan klasör sadece "Salt-Okunur" (Read-Only: `:ro`) olarak verilmelidir. Böylece konteyner hacklense bile orijinal kodları silemez.

