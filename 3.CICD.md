\# 🚀 Aşama 3: CI/CD Pipeline ve İş Akışı Analizi



Bu aşamada Gitleaks'in GitHub Actions ve CI/CD (Sürekli Entegrasyon) süreçlerine nasıl entegre olduğunu ve otomasyon güvenliğini analiz ettim.



\### 1. GitHub Actions ve DevSecOps Entegrasyonu

\*\*Bulgu:\*\* Gitleaks, `.github/workflows/` dizinindeki YAML dosyaları ile doğrudan CI/CD pipeline'larına entegre edilecek şekilde tasarlanmıştır. Bir geliştirici koda yeni bir "Push" yaptığında veya "Pull Request" (PR) açtığında, Gitleaks eylemi otomatik olarak tetiklenir.

\*\*İşlem Adımları:\*\*

1\. Kod repoya gönderilir.

2\. CI/CD sunucusu (Runner) ayağa kalkar ve `gitleaks detect` komutunu çalıştırır.

3\. Eğer kodun içinde bir AWS API anahtarı, veritabanı şifresi veya JWT token bulunursa, pipeline durumunu "Failed" (Başarısız) yapar ve o tehlikeli kodun ana projeye (production) gitmesini engeller.



\### 2. Kritik Soru: Webhook Nedir ve Ne İşe Yarar?

\*\*Analiz:\*\* Webhook, bir olay (event) gerçekleştiğinde bir uygulamanın diğerine gerçek zamanlı bilgi (HTTP POST isteği) göndermesini sağlayan "Tetikleyici" sistemdir.

\* \*\*Gitleaks Özelinde Webhook'un Rolü:\*\* Bir yazılımcı terminalinden `git push` komutunu çalıştırdığı anda, GitHub'ın sunucuları bunu algılar ve CI/CD sunucusuna bir \*\*Webhook\*\* fırlatır. Bu Webhook'un içinde \*"Hey, yeni kod geldi, hemen güvenlik taramasına başla!"\* mesajı vardır.

\* \*\*Sonuç:\*\* Webhook tetiklemesi olmadan otomasyon çalışmazdı. Gitleaks, bu webhook tetiklemesinin hemen ardından devreye giren "Otomatik Güvenlik Polisidir". Sistem sürekli (continuous) olarak kod depolarını taramak yerine, sadece webhook geldiğinde (yeni kod eklendiğinde) çalışarak sunucu kaynaklarını korur.

