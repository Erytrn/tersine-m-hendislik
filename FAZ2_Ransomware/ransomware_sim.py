import os
import base64
import time

print("""
      💀 ========================================== 💀
      💀  ERAY-CRYPT RANSOMWARE SİMÜLASYONU BAŞLADI 💀
      💀 ========================================== 💀
""")
time.sleep(1)

# 1. KURBANIN DOSYALARINI OLUŞTUR (Hedef klasör)
hedef_klasor = "kurban_verileri"
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

dosya_yolu = f"{hedef_klasor}/cok_gizli_sifreler.txt"
with open(dosya_yolu, "w", encoding="utf-8") as f:
    f.write("SİSTEM ADMİN ŞİFRESİ: Root123! \nKASA BİLGİLERİ: 5544-3322-1100")

print(f"[*] Sistem taranıyor... Hedef dosya bulundu: {dosya_yolu}")
time.sleep(1)

# 2. DOSYAYI ŞİFRELE (Kriptografik Saldırı)
print("[!] Dosya içeriği kilitleniyor...")
with open(dosya_yolu, "r", encoding="utf-8") as f:
    orijinal_veri = f.read()

# Gerçek bir AES olmasa da, dosyayı okunamaz hale getiren Base64 tabanlı bir bozma (obfuscation) işlemi
sifreli_veri = base64.b64encode(orijinal_veri.encode("utf-8")).decode("utf-8")
sifreli_veri = sifreli_veri[::-1] # Şifreli metni tersine çevirerek iyice boz

with open(dosya_yolu, "w", encoding="utf-8") as f:
    f.write(sifreli_veri)

time.sleep(1)
print("[💀] BAŞARILI: Veriler başarıyla şifrelendi!")

# 3. VERİ SIZDIRMA SİMÜLASYONU (Webhook)
print("[-] Şifre çözme anahtarı dış sunucuya (C2) aktarılıyor...")
time.sleep(2)
print("[!] Anahtar sızdırıldı: POST https://hacker-sunucusu.com/webhook")
print("[-] Kurbanın ekranda göreceği mesaj: BİZE BİTCOİN GÖNDER!")