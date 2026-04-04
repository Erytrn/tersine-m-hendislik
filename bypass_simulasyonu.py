import base64
import time

print("🕵️ Gitleaks Bypass Simülasyonu Başlatılıyor...")
time.sleep(1)

# DURUM 1: Acemi Yazılımcı (Gitleaks bunu anında yakalar)
# acemi_api_key = "AKIAIOSFODNN7EXAMPLE" 
# (Yukarıdaki satırı yoruma aldık ki Gitleaks bizim repomuzu da bloklamasın!)

# DURUM 2: Hacker / Güvenlik Uzmanı Yöntemi (Gitleaks bunu GÖREMEZ)
# Saldırgan, AWS anahtarını parçalara böler (String Concatenation)
part1 = "AKIAI"
part2 = "OSFOD"
part3 = "NN7EX"
part4 = "AMPLE"

# Kod çalışma anında (Runtime) parçalar birleşir. 
# Gitleaks statik tarama yaptığı için bu birleşimi yakalayamaz.
gizli_aws_key = part1 + part2 + part3 + part4

print("\n[!] Sisteme enjekte edilen parçalar birleştiriliyor...")
time.sleep(1)

print("✅ BASARILI! Gitleaks taraması atlatıldı.")
print(f"🔓 Kullanıma Hazır API Key: {gizli_aws_key}")
print("Bu yöntem, 'Threat Modeling' raporumuzdaki Vektör 1'in canlı kanıtıdır.")