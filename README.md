# 🛡️ Gitleaks Açık Kaynak Güvenlik ve Mimari Analizi

<p align="left">
  <img src="https://img.shields.io/badge/Security-Analysis-red?style=for-the-badge&logo=githubactions" />
  <img src="https://img.shields.io/badge/Reverse_Engineering-Header_Hunter-blue?style=for-the-badge&logo=go" />
  <img src="https://img.shields.io/badge/PoC-Bypass_Sim-green?style=for-the-badge&logo=python" />
</p>

**Hazırlayan:** Eray Turan  
**Proje Kapsamı:** Bilişim Güvenliği Teknolojisi Vize Projesi  
**Seçilen Hedef Repo:** [Gitleaks](https://github.com/gitleaks/gitleaks) (SecOps / Secret Scanning)  
**Proje Durumu:** Tamamlandı ✅  

## 📌 Proje Amacı
Bu projenin amacı, endüstri standardı bir güvenlik aracı olan Gitleaks'i bir **Güvenlik Uzmanı ve Sistem Mimarı** gözüyle uçtan uca incelemektir. Proje; kurulum komutlarının tersine mühendisliğinden, Docker mimarisine ve kaynak kod tabanlı tehdit modellemesine kadar 5 temel aşamada gerçekleştirilmiş ve teorik bulgular **Proof of Concept (PoC)** kodları ile ispatlanmıştır.

---

## 🗺️ 5 Aşamalı Analiz Yol Haritası

### 1. Kurulum Analizi ve Tersine Mühendislik (Header Avcısı)
* **Analiz:** Gitleaks'in `Makefile` yapısı incelenerek kurulum güvenliği ve hash (SHA-256) doğrulama mekanizmaları deşifre edildi.
* **Tersine Mühendislik:** Derlenmiş Binary dosyası üzerinde statik analiz yapılarak "Magic Bytes" (MZ Header) ve mimari yapısı incelendi.
* 📄 **Dosyalar:** `1.ANALIZ.md`, `RE_HEX_DUMP_KANITI.txt`

### 2. İzolasyon ve Forensics (İz Bırakmadan Temizlik)
* **Analiz:** Gitleaks'in sistemde bıraktığı dijital ayak izleri (artifacts), geçici dosyalar (`/tmp`) ve terminal geçmişi kalıntıları tespit edildi.
* **Anti-Forensics:** Sistemin tamamen temizlenmesi için gereken adli bilişim protokolü oluşturuldu.
* 📄 **Dosya:** `2.FORENSICS.md`

### 3. CI/CD Pipeline ve İş Akışı Analizi
* **Analiz:** Gitleaks'in GitHub Actions entegrasyonu ve otomasyon süreçleri incelendi.
* **Webhook Mimarisi:** Yeni kod eklendiğinde (push/PR) Webhook mekanizmasının güvenlik taramasını nasıl tetiklediği teknik olarak açıklandı.
* 📄 **Dosya:** `3.CICD.md`

### 4. Docker Mimarisi ve Konteyner Güvenliği
* **Analiz:** Gitleaks Docker imajının "Multi-stage build" yapısı ve izolasyon sınırları analiz edildi.
* **Karşılaştırma:** Sanal Makine (VM), Docker ve Kubernetes (K8s) mimarilerinin güvenlik ve performans farkları modellendi.
* 📄 **Dosya:** `4.DOCKER.md`

### 5. Kaynak Kod Analizi ve Tehdit Modellemesi (Threat Modeling)
* **Analiz:** Uygulamanın `main.go` giriş noktası ve Regex/Entropi tabanlı tarama algoritmaları incelendi.
* **Bypass PoC:** Statik analiz motorunu atlatmaya yönelik (String Concatenation/Obfuscation) saldırı vektörleri kurgulandı ve canlı bir simülasyon kodu ile kanıtlandı.
* 📄 **Dosyalar:** `5.TEHDIT_MODELI.md`, `bypass_simulasyonu.py`

---

## 🚀 Proje Kanıtları ve Simülasyonlar
Bu projede sadece teorik raporlama yapılmamış, aşağıdaki dosyalarla analizler kanıtlanmıştır:
* **`bypass_simulasyonu.py`**: Gitleaks taramasını atlatan tekniklerin Python üzerindeki PoC uygulaması.
* **`RE_HEX_DUMP_KANITI.txt`**: Gitleaks binary dosyasının Hex-Dump statik analiz çıktısı.
* **`Makefile`**: Projenin kurulum mimarisinin orijinal kaynak dosyası.

---
*Bu çalışma Eray Turan tarafından Bilişim Güvenliği Teknolojisi dersi vize projesi olarak hazırlanmıştır.*
