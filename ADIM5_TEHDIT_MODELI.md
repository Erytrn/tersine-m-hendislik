\# 🕵️ Adım 5: Kaynak Kod ve Tehdit Modellemesi (Threat Modeling)



Bu aşamada Vaultwarden'ın "Sıfır Bilgi" (Zero-Knowledge) mimarisini bir saldırgan gözüyle analiz ettim ve olası saldırı vektörlerini modelledim.



\### 1. Giriş Noktası (Entrypoint) ve Auth Mekanizması

\*\*Analiz:\*\* Vaultwarden'ın ana giriş noktası `main.rs` dosyasıdır ve kimlik doğrulama için \*\*JWT (JSON Web Token)\*\* kullanır. Kullanıcı ana şifresini (Master Password) girdiğinde, bu şifre sunucuya \*\*hiçbir zaman açık metin olarak gönderilmez.\*\* Şifreleme istemci tarafında (browser/app) yapılır.



\### 2. Tehdit Modellemesi: "Hacker Sunucuda!" Senaryosu

\*\*Soru:\*\* Bir saldırgan sunucudaki `db.sqlite3` dosyasını çalarsa ne olur?

\*\*Reasoning:\*\* Saldırgan veritabanını ele geçirse bile, her bir kullanıcının verisi \*\*AES-256-CBC\*\* ile şifrelenmiştir. Şifreyi çözecek olan "Simetrik Anahtar" (Symmetric Key), kullanıcının ana şifresinden (PBKDF2-SHA256) türetilir ve bu anahtar sunucuda \*\*asla saklanmaz.\*\* \* \*\*Sonuç:\*\* Hacker elinde şifreli bir blokla kalır, kullanıcının ana şifresi olmadan verileri deşifre edemez.



\### 3. Olası Saldırı Vektörleri ve Bypass Denemesi

Bir hacker Vaultwarden'a nasıl saldırabilir?

\* \*\*Brute-Force:\*\* Kullanıcının ana şifresini tahmin etmeye çalışmak. (Vaultwarden bunu 'rate-limiting' ile engeller).

\* \*\*Memory Dump:\*\* Eğer bir kullanıcı sisteme giriş yapmışsa, şifreleme anahtarı kısa süreliğine RAM'de (bellekte) durur. Bir saldırgan sistemde root olup belleği dump ederse (Volatility vb.) anahtarı sızdırabilir.

\* \*\*Logic Bypass:\*\* Kaynak kodda bir hata bulunarak (örn: JWT doğrulama hatası), şifre sormadan oturum açma (Session Hijacking) denenebilir.

