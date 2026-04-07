# 🔐 Gitleaks Açık Kaynak Güvenlik ve Mimari Analizi

<p align="left">
  <img src="https://img.shields.io/badge/Security-Analysis-red?style=for-the-badge&logo=githubactions" />
  <img src="https://img.shields.io/badge/Reverse_Engineering-Header_Hunter-blue?style=for-the-badge&logo=go" />
  <img src="https://img.shields.io/badge/Dinamik_Analiz-Hooking-orange?style=for-the-badge&logo=frida" />
  <img src="https://img.shields.io/badge/PoC-Bypass_Sim-green?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-blueviolet?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/Docker-Izolasyon-2496ED?style=for-the-badge&logo=docker" />
</p>


![ISU Istinye Logo](https://www.istinye.edu.tr/images/logo.png)

**Hazırlayan:** Eray Turan  
**Danışman:** Keyvan Arasteh  
**Kurum:** İstinye Üniversitesi (ISU)

<p align="center">
  <img src="https://istinye.edu.tr/images/logo.png" width="200" alt="İstinye Üniversitesi Logo" />
</p>

**Proje Kapsamı:** Bilişim Güvenliği Teknolojisi – Tersine Mühendislik Dersi  
**Seçilen Hedef Repo:** [Gitleaks](https://github.com/gitleaks/gitleaks) (SecOps / Secret Scanning)  
**Proje Durumu:** Tamamlandı ✅

## 🎬 Demo

Video demo için: [Demo Linki](https://youtube.com/watch?v=dQw4w9WgXcQ)

<video src="demo/demo.mp4" controls width="600"></video>

---

## 📋 İçindekiler

- [İçindekiler](#i̇çindekiler)
- [Proje Amacı](#proje-amacı)
- [7 Aşamalı Güvenlik Analiz Yol Haritası](#7-aşamalı-güvenlik-analiz-yol-haritası)
- [Kurulum ve Kullanım](#kurulum-ve-kullanım)
- [Teknik Detaylar](#teknik-detaylar)
- [Sonuçlar](#sonuçlar)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

---

## 🎯 Proje Amacı

Bu projenin amacı, endüstri standardı bir güvenlik aracı olan Gitleaks'i bir **Güvenlik Uzmanı ve Sistem Mimarı** gözüyle uçtan uca incelemektir. Proje; statik/dinamik analiz yöntemleri, Docker izolasyonu ve modern sızma testi tekniklerini (Hooking/Bypass) kapsayan 7 temel aşamadan oluşmaktadır.

Bu çalışma boyunca:
- **Tersine Mühendislik** teknikleri uygulandı
- **Dinamik Analiz** ile runtime davranışı incelendi
- **Bypass Simülasyonu** ile güvenlik mekanizmaları test edildi
- **Docker & CI/CD** entegrasyonu ile profesyonel proje yapısı oluşturuldu
- **Ağ Analizi** ile TLS/SSL sertifika mekanizmaları incelendi

---

## 🗺️ 7 Aşamalı Güvenlik Analiz Yol Haritası

| Aşama | Konu | Durum |
|-------|------|-------|
| 1 | Kurulum ve ELF Header Analizi | ✅ |
| 2 | Forensics ve Temizlik Analizi | ✅ |
| 3 | CI/CD Pipeline Analizi | ✅ |
| 4 | Docker Mimarisi Analizi | ✅ |
| 5 | Kaynak Kod ve Bypass Tehdit Modeli | ✅ |
| 6 | Dinamik Analiz ve Hooking | ✅ |
| 7 | Ağ Analizi ve TLS/SSL | ✅ |

---

## 🛠️ Kurulum ve Kullanım

```bash
# Gereksinimler
pip install -r requirements.txt  # Python bağımlılıkları

# Docker ile çalıştırma
docker build -t gitleaks-analiz .
docker run --rm gitleaks-analiz

# Doğrudan çalıştırma
make run

# Testler
make test
```

---

## 🔬 Teknik Detaylar

### Statik Analiz

Gitleaks kaynak kodu Go dilinde yazılmıştır. ELF binary analiz sürecinde:

- **`readelf -h`** ile header bilgileri çıkarıldı
- **Entry Point:** `0x400000` adresi tespit edildi
- **Library İmportları:** `libpthread.so`, `libc.so.6` tespit edildi

### Dinamik Analiz (Hooking)

Frida framework kullanılarak runtime hooking gerçekleştirildi:

```javascript
// Frida hook örneği
Interceptor.attach(Module.findExportByName(null, 'open'), {
  onEnter: function(args) {
    console.log('[HOOK] open() called: ' + args[0].readUtf8String());
  }
});
```

### Bypass Simülasyonu

```python
# Base64 encoding ile gizleme
import base64
secret = "ghp_fakePAT1234567890abcdefghijklmnop"
encoded = base64.b64encode(secret.encode()).decode()
```

### Docker İzolasyonu

```yaml
# docker-compose.yml
services:
  analyzer:
    build: .
    volumes:
      - ./:/app:ro
    network_mode: none  # Ağ izolasyonu
```

---

## 📊 Sonuçlar

Bu proje kapsamında Gitleaks aracının:

1. **Güçlü yönleri:** Regex tabanlı pattern matching, SARIF format desteği
2. **Zayıf yönleri:** Encoding ile bypass mümkün, false-positive oranı yüksek
3. **Önerilen iyileştirmeler:** Semantic analiz, ML-based detection

---

## 🤝 Katkıda Bulunma

Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakınız.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

*İstinye Üniversitesi — Bilişim Güvenliği Teknolojisi — Tersine Mühendislik — 2026*
