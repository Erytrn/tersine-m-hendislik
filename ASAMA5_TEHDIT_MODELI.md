\# 🕵️ Aşama 5: Kaynak Kod Analizi ve Tehdit Modellemesi (Threat Modeling)



Bu aşamada Gitleaks'in kaynak kod mantığını (Entrypoint ve Algoritma) inceledim ve bir saldırganın bu güvenlik aracını nasıl atlatabileceğine (Bypass) dair tehdit senaryoları modelledim.



\### 1. Entrypoint ve Tarama Mantığı

\*\*Analiz:\*\* Uygulamanın başlangıç noktası Go diliyle yazılmış `main.go` dosyasıdır. Gitleaks, kod geçmişini tararken temelde iki ana mekanizma kullanır:

\* \*\*Regex (Düzenli İfadeler):\*\* AWS, GitHub, Slack gibi bilinen platformların API anahtarlarının standart metin şablonlarını arar.

\* \*\*Shannon Entropy (Entropi Analizi):\*\* Rastgelelik ölçümüdür. Base64 veya Hex formatındaki uzun, anlamsız ve yüksek entropili şifre dizilimlerini "şüpheli" olarak işaretler.



\### 2. Tehdit Modellemesi: "Gitleaks'i Kandırma (Bypass)" Senaryoları

Bir saldırgan / kötü niyetli yazılımcı kaynak kodu incelerse, Gitleaks'in Regex ve Entropi mantığına karşı şu bypass saldırılarını gerçekleştirebilir:



\* \*\*Vektör 1: Parçalama (String Concatenation)\*\*

&#x20; Gitleaks tek parça halindeki `AKIAIOSFODNN7EXAMPLE` (AWS Key) yapısını yakalar. Saldırgan bunu kod içinde bölerse aracı kör edebilir:

&#x20; `apikey := "AKIAIOS" + "FODNN7" + "EXAMPLE"` (Regex eşleşmesi bozulur).



\* \*\*Vektör 2: Çift Şifreleme (Encoding/Obfuscation)\*\*

&#x20; Saldırgan, koyacağı token'ı önce Base64 ile şifreler, sonra bunu koda gömer. Gitleaks standart formattaki token'ı aradığı için bu özel obfuscation işlemini algılayamaz. (Çalışma anında kod bunu deşifre edip kullanır).



\* \*\*Vektör 3: Kural Zehirlenmesi (Rule Poisoning)\*\*

&#x20; Gitleaks, istisnaları `.gitleaksignore` dosyasından okur. Eğer saldırgan repoya erişim sağlamışsa, kendi zararlı dosyasının yolunu sinsice bu ignore listesine ekleyerek o dosyanın taranmasını tamamen engelleyebilir.

