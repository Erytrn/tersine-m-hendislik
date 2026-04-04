\# 🐳 Adım 4: Docker Mimarisi ve Konteyner Güvenliği



Bu aşamada Vaultwarden'ın üzerinde yükseldiği Docker mimarisini ve izolasyon seviyelerini analiz ettim.



\### 1. Docker İmajı ve Katman Analizi

\*\*Reasoning:\*\* Bir Docker imajı, uygulamanın çalışması için gereken tüm bağımlılıkları içeren salt-okunur (read-only) bir paket şablonudur. Vaultwarden imajı "Layered" (katmanlı) bir yapıdadır:

\* \*\*Base Layer:\*\* Alpine Linux veya Debian (İşletim sistemi çekirdeği değil, kullanıcı alanı kütüphaneleri).

\* \*\*Application Layer:\*\* Vaultwarden'ın Rust ile derlenmiş ana binary dosyası.

\* \*\*Config Layer:\*\* Çevresel değişkenler ve port tanımları.



\### 2. İzolasyon ve Erişim Sınırları

\*\*Reasoning:\*\* Konteyner, host sistemin çekirdeğini (Kernel) paylaşır ancak kendi dosya sistemi ve ağ alanında hapsolmuştur. Vaultwarden konteyneri sadece dış dünyaya 80 portunu açar ve sadece belirlenen `./vw-data` klasörüne yazar. Sistemin geri kalanına (örn: `/etc/passwd`) erişimi Docker Engine tarafından bloke edilir.



\### 3. Kritik Karşılaştırma: VM vs Docker vs K8s

Hocamızın sorduğu o temel farkları şöyle analiz ettim:

\* \*\*Sanal Makine (VM):\*\* Tam bir işletim sistemi (Hypervisor) simüle eder. Çok güvenlidir ama hantaldır.

\* \*\*Docker:\*\* Sadece uygulama ve bağımlılıklarını paketler. Çok hızlıdır, izolasyon seviyesi VM kadar katı değildir.

\* \*\*Kubernetes (K8s):\*\* Tek bir konteyner değil, binlerce konteynerin orkestrasyonudur (otomatik ölçekleme, hata yönetimi).



\### 4. Sıkılaştırma (Hardening) Önerisi

Sistemi en güvenli hale getirmek için konteyneri `root` kullanıcısı yerine `non-root` bir kullanıcıyla çalıştırmalı ve dosya sistemini `read-only: true` yaparak saldırganın konteyner içine dosya indirmesini engellemeliyiz.

