\# 🔍 Aşama 2: İzolasyon ve Forensics (İz Bırakmadan Temizlik)



Bu aşamada, Gitleaks aracının Ubuntu/Linux sistemlerde bıraktığı dijital ayak izlerini (artifacts) tespit ettim ve sistemin "tertemiz" (pristine) hale getirilme sürecini dökümante ettim.



\### 1. Dijital İzlerin Tespiti (Artifact Tracking)

Gitleaks çalıştırıldığında sistemde şu izleri bırakır:

\* \*\*Binaries (Çalıştırılabilir Dosyalar):\*\* Genellikle `/usr/local/bin/gitleaks` veya kullanıcının `Go/bin` klasöründe bulunur.

\* \*\*Temporary Files (Geçici Dosyalar):\*\* Gitleaks uzak bir repoyu tararken, repoyu geçici olarak `/tmp` dizinine klonlar. Eğer tarama yarıda kesilirse, bu gizli kodlar `/tmp` içinde kalmaya devam eder.

\* \*\*Command History:\*\* Bash veya Zsh geçmişinde (`.bash\_history`), taratılan repoların URL'leri ve kullanılan parametreler açıkça görünür.

\* \*\*Config Files:\*\* Kullanıcı tarafından tanımlanan `.gitleaks.toml` dosyaları sistemin farklı yerlerinde unutulabilir.



\### 2. Adli Bilişim (Forensics) Kontrol Listesi

Sistemin tamamen temizlendiğini ispatlamak için şu kontrolleri gerçekleştiriyorum:

\* `which gitleaks`: Komutun sistem yolundan (PATH) kalktığının teyidi.

\* `ls -la /tmp | grep gitleaks`: Geçici dizinde Gitleaks'e ait hiçbir klonlanmış repo kalmadığının kontrolü.

\* `history | grep gitleaks`: Terminal geçmişinde kalan komutların temizlenmesi.



\### 3. İz Bırakmadan Temizlik (Anti-Forensics) Reçetesi

Sistemi operasyon öncesi haline getirmek için şu komut hiyerarşisini uyguladım:

1\. `rm -f /usr/local/bin/gitleaks`: Ana binary dosyasının silinmesi.

2\. `rm -rf /tmp/gitleaks-\*`: Gitleaks tarafından oluşturulan tüm geçici çalışma dizinlerinin fiziksel olarak diskten temizlenmesi.

3\. `history -c \&\& history -w`: Mevcut oturumdaki komut geçmişinin tamamen silinmesi.

4\. `shred -u \~/.gitleaks.toml`: (Varsa) Yapılandırma dosyasının üzerine rastgele veriler yazılarak (shredding) geri döndürülemez şekilde silinmesi.

