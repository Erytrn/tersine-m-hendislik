\# ☣️ FAZ 2: Kriptografik Şantaj (Ransomware) ve Savunma Mimarisi



Bu aşamada, projenin "Saha Uygulaması" kapsamında kendi yazdığımız bir Python Fidye Yazılımı (Ransomware) simülasyonu ile sisteme saldırdık ve ardından bu saldırıyı durduracak Blue Team (Mavi Takım) savunma katmanlarını modelledik.



\## 🔴 Saldırı Simülasyonu (Red Team)

Geliştirdiğimiz `ransomware\_sim.py` aracı şu adımları başarıyla gerçekleştirmiştir:

1\. \*\*Keşif ve Hedefleme:\*\* Sistemdeki `kurban\_verileri` dizinini tespit etti.

2\. \*\*Kriptografik Kilitleme:\*\* İçerideki hassas verileri Base64 tabanlı bir obfuscation (gizleme/şifreleme) yöntemiyle okunamaz hale getirdi.

3\. \*\*Veri Sızdırma (Exfiltration):\*\* Şifreyi çözecek anahtarı HTTP POST isteği ile dışarıdaki bir C2 (Command \& Control) sunucusuna gönderdiğini simüle etti.



\## 🔵 Savunma Mekanizması (Blue Team)

Bir Sistem Mimarı olarak, bu tür bir saldırıyı kaynağında durdurmak için şu iki güvenlik katmanını tasarladım:



\### 1. Ağ İzolasyonu (Sızmayı Engelleme)

Fidye yazılımı anahtarı dışarı çıkaramazsa (Webhook engellenirse), veriler şifrelense bile kurtarılabilir. Linux sunucusunda `iptables` ile şüpheli Python işlemlerinin dış ağa çıkışı bloklanmalıdır:

\\`\\`\\`bash

\# Sadece yetkili servislerin dışarı çıkmasına izin ver, diğerlerini (Python scripti dahil) engelle.

iptables -A OUTPUT -p tcp --dport 80 -m owner ! --uid-owner root -j DROP

\\`\\`\\`



\### 2. Dosya Yetki Kısıtlaması (RBAC / Read-Only)

Zararlı yazılımın orijinal dosyanın üzerine "şifreli" versiyonunu yazabilmesi için "Write" (Yazma) yetkisine ihtiyacı vardır. Eğer hassas dizinler sadece "Okunabilir" (Read-Only) yapılırsa, fidye yazılımı dosyayı şifreleyemez, "Permission Denied" hatası alır.

\\`\\`\\`bash

\# Klasörü sadece okunabilir yap (Yazma yetkisini al)

chmod -R 400 kurban\_verileri/

\\`\\`\\`



\*\*Sonuç:\*\* Bu savunma mimarisi aktif olsaydı, `ransomware\_sim.py` scripti ne şifrelenmiş veriyi diske kaydedebilecek ne de anahtarı dış dünyaya sızdırabilecekti.

