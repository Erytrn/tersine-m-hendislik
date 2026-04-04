\# 🕵️ Aşama 1: Kurulum Analizi ve Tersine Mühendislik (Header Avcısı)



Gitleaks projesinin `Makefile` dosyasını ve derleme (build) mimarisini bir Güvenlik Uzmanı gözüyle analiz ettim. İnceleme sonuçlarım aşağıdadır:



\### 1. Kurulum Scripti (Makefile) Analizi

\*\*Bulgu:\*\* `Makefile` dosyasını incelediğimde, siber güvenlikte çok tehlikeli bulduğumuz `curl | bash` (körü körüne dışarıdan kod çalıştırıp kurma) mantığının \*\*kullanılmadığını\*\* tespit ettim. Sistem, tamamen Go dilinin yerleşik ve güvenli `go build` komutuna dayanıyor. Herhangi bir şüpheli dizin oluşturmuyor veya root yetkisi talep etmiyor.



\### 2. Hash ve İmza Kontrolü (Checksum)

\*\*Bulgu:\*\* Projenin dışarıdan paket/modül çekerken Go'nun yerleşik `go.sum` dosyasını kullandığını gördüm. Bu dosya, indirilen her bağımlılığın \*\*kriptografik hash\*\* (SHA-256) özetini tutar. Eğer araya giren bir saldırgan (MITM) paketlerden birini değiştirirse, hash uyuşmazlığı çıkar ve derleme anında durur. Ayrıca yayınlanan (Release) sürümlerde `checksums.txt` ile dağıtım yapılmaktadır.



\### 3. İleri Seviye İnceleme: Header Avcısı (ELF Analizi)

Gitleaks kaynak kodundan derlenen bir Linux binary'sini (ELF - Executable and Linkable Format) statik analize tabi tuttuğumuzda şu "Header" karakteristiği ortaya çıkar:

\* \*\*Magic Bytes:\*\* `7F 45 4C 46` (Geçerli bir Linux çalıştırılabilir dosyası).

\* \*\*Linking (Bağlantı Türü):\*\* Go derleyicisi dosyayı \*\*"Statically Linked" (Statik Bağlantılı)\*\* olarak üretir. Yani dışarıdan `libc.so` gibi kütüphanelere ihtiyaç duymaz. Bu durum aracı çok "taşınabilir" (portable) yapar; hedef sistemde hiçbir şey kurulu olmasa bile tıkır tıkır çalışır.

\* \*\*Entry Point (Giriş Noktası):\*\* ELF başlığındaki \*Entry Point\* adresi (örn: `0x401000`), doğrudan uygulamanın ana başlatıcı fonksiyonuna (`runtime.main` ve ardından `main.main`) işaret eder.

