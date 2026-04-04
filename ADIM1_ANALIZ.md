\# 🕵️ Adım 1: Kurulum ve Yapılandırma Analizi (Reasoning)



\### 1. Güvenli Paket Çekimi (Hash Kontrolü)

\*\*Analiz:\*\* `image: vaultwarden/server:latest` satırı incelendiğinde, yazılımın Docker Hub üzerinden çekildiği görülmektedir. Docker, paketleri indirirken SHA256 Hash (Digest) kontrolünü otomatik olarak yapar. Bu, hocamızın belirttiği "körü körüne kurulum" riskini ortadan kaldırır; çünkü paket bozulmuşsa Docker kurulumu reddeder.



\### 2. Dizin Oluşturma ve Yetki Talepleri

\*\*Analiz:\*\* `volumes: - ./vw-data:/data` satırı, tüm şifreli verilerin host makinedeki `vw-data` klasöründe saklanacağını gösterir. Tersine mühendislik bakış açısıyla; bu klasörün izinleri (`chmod 700`) kısıtlanmadığı takdirde sistemdeki diğer kullanıcılar veritabanına erişebilir.



\### 3. Kritik Port Analizi

\*\*Analiz:\*\* Uygulama varsayılan olarak `80` portunu açmaktadır. Güvenlik mimarisi açısından bu bir risk teşkil eder; gerçek bir senaryoda bu trafik mutlaka bir Reverse Proxy (Nginx vb.) ile şifrelenmelidir.

