\# 🔍 Adım 2: İzolasyon ve İz Bırakmadan Temizlik (Forensics)



Bu aşamada, Vaultwarden kurulumunun sistemde bıraktığı dijital ayak izlerini tespit ettim ve sistemin "tertemiz" hale getirilme sürecini aşağıda belgeledim.



\### 1. Dijital İzlerin Tespiti (Artifacts)

Vaultwarden konteyneri çalıştırıldığında sistemde şu izler oluşur:

\* \*\*Hafif İzler:\*\* Docker `networks` katmanında sanal bir köprü (bridge).

\* \*\*Kalıcı İzler (Volumes):\*\* Host sistemdeki `./vw-data` klasörü. Bu klasör, şifreli SQLite veritabanını (`db.sqlite3`) ve yapılandırma dosyalarını barındırır.

\* \*\*Ağ İzleri:\*\* 80 portunu dinleyen bir Docker proxy servisi.



\### 2. Adli Bilişim (Forensics) Kontrol Listesi

Sistemin tamamen temizlendiğini ispatlamak için şu kontrolleri gerçekleştirdim:

\* `docker ps -a`: Hiçbir konteynerin arka planda (zombi) çalışmadığının kontrolü.

\* `netstat -ano | findstr :80`: 80 portunun artık dinlenmediğinin (Listening) kanıtı.

\* `ls -R`: `./vw-data` klasörünün ve içindeki hassas verilerin (SQLite DB) tamamen silindiğinin teyidi.



\### 3. İz Bırakmadan Temizlik Reçetesi

Sistemi fabrika ayarlarına döndürmek için şu komut hiyerarşisini uyguladım:

1\. `docker-compose down`: Konteyner ve ağ yapılarını güvenle durdurur.

2\. `rm -rf ./vw-data`: En kritik adım; şifreli verilerin fiziksel olarak diskten silinmesi.

3\. `docker image rm vaultwarden/server`: İndirilen imajın (hash doğrulanmış paket) sistemden atılması.

