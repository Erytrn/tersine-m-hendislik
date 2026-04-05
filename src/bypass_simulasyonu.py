import base64
import time

# Eray Turan - Gitleaks Bypass PoC
# Amac: Statik analiz motorlarinin dize parçalama (string concatenation) 
# karsisindaki zafiyetini kanitlamaktýr.

print("??? Gitleaks Bypass Simülasyonu...")
# Hackerlar genelde bu yöntemi 'Deobfuscation' zorlastýrmak için kullanýr.
part1 = "AKIAI" # AWS Access Key Prefix
part2 = "OSFOD"
part3 = "NN7EX"
part4 = "AMPLE"

gizli_aws_key = part1 + part2 + part3 + part4
print(f"? Birlesmis Key: {gizli_aws_key}")

# Alternatif Bypass: Base64 Obfuscation
def b64_bypass():
    secret = 'QUZJQTRSU09GT0ROTjdFWQU1UExF' # Base64 encoded key
    return base64.b64decode(secret)

