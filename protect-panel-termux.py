#!/data/data/com.termux/files/usr/bin/python3
# PROTECT PANEL V1.0.0 - FULL VERSION WITH HARDENING
# Author: @ZledYazu
# FITUR: Panel Protections + Anti-Kill + Hardening + Anti-DDOS

import os
import sys
import time
import subprocess
import tempfile
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

VERSION = "1.0.0"
AUTHOR = "@ZledYazu"

# ==================== PANEL PROTECTIONS ====================

PANEL_PROTECTIONS = [
    {
        "name": "🛡️ Anti Intip Server",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Servers/ServerController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin\\Servers;
use Illuminate\\View\\View;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\Server;
use Pterodactyl\\Http\\Controllers\\Controller;
class ServerController extends Controller
{
    public function index(Request $request): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.servers.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip User",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/UserController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin;
use Illuminate\\View\\View;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\User;
use Pterodactyl\\Http\\Controllers\\Controller;
class UserController extends Controller
{
    public function index(Request $request): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.users.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip Node",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Nodes/NodeController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin\\Nodes;
use Illuminate\\View\\View;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\Node;
use Pterodactyl\\Http\\Controllers\\Controller;
class NodeController extends Controller
{
    public function index(Request $request): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.nodes.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip Location",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/LocationController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin;
use Illuminate\\View\\View;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\Location;
use Pterodactyl\\Http\\Controllers\\Controller;
class LocationController extends Controller
{
    public function index(): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.locations.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip Database",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/DatabaseController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin;
use Illuminate\\View\\View;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\DatabaseHost;
use Pterodactyl\\Http\\Controllers\\Controller;
class DatabaseController extends Controller
{
    public function index(): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.databases.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip API",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/ApiController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin;
use Illuminate\\View\\View;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Http\\Controllers\\Controller;
class ApiController extends Controller
{
    public function index(Request $request): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.api.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip Nest",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Nests/NestController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin\\Nests;
use Illuminate\\View\\View;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\Nest;
use Pterodactyl\\Http\\Controllers\\Controller;
class NestController extends Controller
{
    public function index(): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.nests.index');
    }
}"""
    },
    {
        "name": "🛡️ Anti Intip Settings",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Settings/IndexController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin\\Settings;
use Illuminate\\View\\View;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Http\\Controllers\\Controller;
class IndexController extends Controller
{
    public function index(): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.settings.index');
    }
}"""
    }
]

# ==================== HARDENING SCRIPTS ====================

ANTI_KILL_SCRIPT = '''#!/bin/bash
# ANTI-KILL SYSTEM - By @ZledYazu

while true; do
    # Deteksi proses mencurigakan (index.js killer)
    ps aux | grep -E "node.*writeSync|Buffer.*allocUnsafe|cluster\\.fork" | grep -v grep | while read line; do
        pid=$(echo $line | awk '{print $2}')
        echo "🔥 KILLER DETECTED! PID: $pid"
        kill -9 $pid 2>/dev/null
        echo "$(date): Killed process $pid" >> /var/log/zledfr-kill.log
    done
    
    # Hapus file mencurigakan
    find /tmp /dev/shm /var/tmp /run /var/lib -type f \\( -name "*.bin" -o -name "*.tmp" -o -name "*.img" \\) -size +10M -delete 2>/dev/null
    
    # Hapus hidden directories
    for path in /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db; do
        if [ -d "$path" ]; then
            rm -rf "$path"
        fi
    done
    
    sleep 5
done &
'''

FS_HARDENING = '''#!/bin/bash
# FILESYSTEM HARDENING

# Protect critical files
chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow 2>/dev/null

# Secure mount points
mount -o remount,noexec,nosuid,nodev /tmp /var/tmp /dev/shm 2>/dev/null

# Create honeypot directories
mkdir -p /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chmod 000 /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chattr +i /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db 2>/dev/null

echo "✅ Filesystem hardening complete"
'''

KERNEL_HARDENING = '''#!/bin/bash
# KERNEL HARDENING

cat >> /etc/sysctl.conf << 'EOF'
fs.protected_fifos = 2
fs.protected_regular = 2
fs.protected_symlinks = 1
fs.protected_hardlinks = 1
kernel.randomize_va_space = 2
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_syn_retries = 2
EOF

sysctl -p
echo "✅ Kernel hardening complete"
'''

ANTI_DDOS = '''#!/bin/bash
# ANTI-DDOS SYSTEM

iptables -N ZLEDFR-DDOS 2>/dev/null
iptables -F ZLEDFR-DDOS

# Rate limiting
iptables -A ZLEDFR-DDOS -m limit --limit 25/second --limit-burst 50 -j ACCEPT
iptables -A ZLEDFR-DDOS -j DROP

# SYN flood protection
iptables -A INPUT -p tcp --syn -m limit --limit 10/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# Save rules
iptables-save > /etc/iptables/rules.v4 2>/dev/null
echo "✅ Anti-DDOS active"
'''

SYSTEMD_SERVICE = '''[Unit]
Description=ZLEDFR Panel Protect
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/zledfr-monitor.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
'''

MONITOR_SCRIPT = '''#!/bin/bash
# ZLEDFR MONITOR

while true; do
    # Restart services if down
    systemctl is-active nginx > /dev/null || systemctl restart nginx
    systemctl is-active php8.1-fpm > /dev/null || systemctl restart php8.1-fpm
    
    # Check disk usage
    df -h / | awk 'NR==2 {if ($5+0 > 90) system("echo \"Disk usage high\" | wall")}'
    
    sleep 30
done
'''

CRON_JOBS = '''# ZLEDFR PANEL PROTECTION
* * * * * root /usr/local/bin/anti-kill.sh > /dev/null 2>&1
*/5 * * * * root /usr/local/bin/fs-hardening.sh > /dev/null 2>&1
*/10 * * * * root /usr/local/bin/anti-ddos.sh > /dev/null 2>&1
0 * * * * root /usr/local/bin/kernel-hardening.sh > /dev/null 2>&1
'''

# ==================== MAIN CLASS ====================

class ProtectPanel:
    def __init__(self):
        self.ip = ""
        self.password = ""
        self.port = 22

    def clear_screen(self):
        os.system('clear')

    def banner(self):
        self.clear_screen()
        print(f"""{Fore.RED}
╔═══════════════════════════════════════════════════════════╗
║  ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗║
║  ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║   ║
║  ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║   ║
║  ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║   ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ║
║                                                               ║
╠═══════════════════════════════════════════════════════════╣
║  VERSION : 1.0.0 - FULL VERSION                           ║
║  AUTHOR  : @ZledYazu                                       ║
║  STATUS  : HARDENING + ANTI-KILL + ANTI-DDOS              ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """)

    def menu(self):
        print(f"\n{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗")
        print(f"║                         MAIN MENU                            ║")
        print(f"╠═══════════════════════════════════════════════════════════╣")
        print(f"║  {Fore.YELLOW}1.{Fore.WHITE} Connect to VPS                                   {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}2.{Fore.WHITE} Install Panel Protections (9 files)              {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}3.{Fore.WHITE} Install Anti-Kill System                         {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}4.{Fore.WHITE} Install Filesystem Hardening                     {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}5.{Fore.WHITE} Install Kernel Hardening                         {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}6.{Fore.WHITE} Install Anti-DDOS                                {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}7.{Fore.WHITE} Install ALL Protections (2+3+4+5+6)              {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}8.{Fore.WHITE} Check Status                                     {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}9.{Fore.WHITE} Exit                                             {Fore.CYAN}║")
        print(f"╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

    def ssh_command(self, cmd):
        """Execute SSH command"""
        full_cmd = f"sshpass -p '{self.password}' ssh -o StrictHostKeyChecking=no -p {self.port} root@{self.ip} '{cmd}'"
        return os.system(full_cmd) == 0

    def upload_file(self, remote_path, content):
        """Upload file to remote server"""
        # Backup first
        self.ssh_command(f"cp {remote_path} {remote_path}.bak 2>/dev/null")
        
        # Escape content
        content = content.replace("'", "'\\''")
        cmd = f"echo '{content}' > {remote_path}"
        return self.ssh_command(cmd)

    def upload_script(self, remote_path, content):
        """Upload and make executable"""
        if self.upload_file(remote_path, content):
            self.ssh_command(f"chmod +x {remote_path}")
            return True
        return False

    def connect(self):
        print(f"\n{Fore.YELLOW}Enter VPS details:{Style.RESET_ALL}")
        self.ip = input(f"{Fore.CYAN}IP Address: {Style.RESET_ALL}").strip()
        self.password = input(f"{Fore.CYAN}Root Password: {Style.RESET_ALL}").strip()
        port_input = input(f"{Fore.CYAN}SSH Port (default 22): {Style.RESET_ALL}").strip()
        self.port = int(port_input) if port_input else 22

        print(f"\n{Fore.YELLOW}Testing connection...{Style.RESET_ALL}")
        if self.ssh_command("echo 'Connected' > /dev/null"):
            print(f"{Fore.GREEN}[✓] Connected!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}[✗] Connection failed!{Style.RESET_ALL}")
            return False

    def install_panel_protections(self):
        if not self.ip:
            print(f"{Fore.RED}[✗] Connect first!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}Installing panel protections...{Style.RESET_ALL}\n")
        
        success = 0
        for i, p in enumerate(PANEL_PROTECTIONS, 1):
            print(f"{Fore.CYAN}[{i}/{len(PANEL_PROTECTIONS)}] {p['name']}{Style.RESET_ALL}")
            if self.upload_file(p['path'], p['code']):
                success += 1
                print(f"{Fore.GREEN}  ✓ Success{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}  ✗ Failed{Style.RESET_ALL}")
            print()
            
        print(f"{Fore.GREEN}[✓] Installed {success}/{len(PANEL_PROTECTIONS)}{Style.RESET_ALL}")

    def install_anti_kill(self):
        print(f"\n{Fore.YELLOW}Installing Anti-Kill System...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-kill.sh", ANTI_KILL_SCRIPT):
            self.ssh_command("nohup /usr/local/bin/anti-kill.sh > /dev/null 2>&1 &")
            print(f"{Fore.GREEN}[✓] Anti-Kill installed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Failed{Style.RESET_ALL}")

    def install_fs_hardening(self):
        print(f"\n{Fore.YELLOW}Installing Filesystem Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/fs-hardening.sh", FS_HARDENING):
            self.ssh_command("bash /usr/local/bin/fs-hardening.sh")
            print(f"{Fore.GREEN}[✓] Filesystem Hardening installed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Failed{Style.RESET_ALL}")

    def install_kernel_hardening(self):
        print(f"\n{Fore.YELLOW}Installing Kernel Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/kernel-hardening.sh", KERNEL_HARDENING):
            self.ssh_command("bash /usr/local/bin/kernel-hardening.sh")
            print(f"{Fore.GREEN}[✓] Kernel Hardening installed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Failed{Style.RESET_ALL}")

    def install_anti_ddos(self):
        print(f"\n{Fore.YELLOW}Installing Anti-DDOS...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-ddos.sh", ANTI_DDOS):
            self.ssh_command("bash /usr/local/bin/anti-ddos.sh")
            print(f"{Fore.GREEN}[✓] Anti-DDOS installed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Failed{Style.RESET_ALL}")

    def install_systemd(self):
        print(f"\n{Fore.YELLOW}Installing Systemd Service...{Style.RESET_ALL}")
        self.upload_file("/etc/systemd/system/zledfr-protect.service", SYSTEMD_SERVICE)
        self.upload_script("/usr/local/bin/zledfr-monitor.sh", MONITOR_SCRIPT)
        self.ssh_command("systemctl daemon-reload")
        self.ssh_command("systemctl enable zledfr-protect.service")
        self.ssh_command("systemctl start zledfr-protect.service")
        print(f"{Fore.GREEN}[✓] Systemd service installed!{Style.RESET_ALL}")

    def install_cron(self):
        print(f"\n{Fore.YELLOW}Installing Cron Jobs...{Style.RESET_ALL}")
        self.upload_file("/etc/cron.d/zledfr-protect", CRON_JOBS)
        print(f"{Fore.GREEN}[✓] Cron jobs installed!{Style.RESET_ALL}")

    def install_all(self):
        print(f"\n{Fore.YELLOW}Installing ALL Protections...{Style.RESET_ALL}")
        self.install_panel_protections()
        self.install_anti_kill()
        self.install_fs_hardening()
        self.install_kernel_hardening()
        self.install_anti_ddos()
        self.install_systemd()
        self.install_cron()
        print(f"\n{Fore.GREEN}[✓] ALL PROTECTIONS INSTALLED!{Style.RESET_ALL}")

    def check_status(self):
        if not self.ip:
            print(f"{Fore.RED}[✗] Connect first!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}Checking protection status...{Style.RESET_ALL}\n")
        
        # Check panel protections
        print(f"{Fore.CYAN}📋 PANEL PROTECTIONS:{Style.RESET_ALL}")
        protected = 0
        for p in PANEL_PROTECTIONS:
            if self.ssh_command(f"grep -q '@ZledYazu' {p['path']} 2>/dev/null"):
                protected += 1
                print(f"{Fore.GREEN}  ✓ {p['name']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}  ✗ {p['name']}{Style.RESET_ALL}")
        
        # Check anti-kill
        print(f"\n{Fore.CYAN}💀 ANTI-KILL:{Style.RESET_ALL}")
        if self.ssh_command("pgrep -f 'anti-kill.sh' > /dev/null"):
            print(f"{Fore.GREEN}  ✓ Running{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}  ✗ Not running{Style.RESET_ALL}")
        
        # Check anti-ddos
        print(f"\n{Fore.CYAN}🌊 ANTI-DDOS:{Style.RESET_ALL}")
        if self.ssh_command("iptables -L ZLEDFR-DDOS 2>/dev/null | grep -q ZLEDFR-DDOS"):
            print(f"{Fore.GREEN}  ✓ Active{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}  ✗ Not active{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[✓] Panel Protections: {protected}/{len(PANEL_PROTECTIONS)}{Style.RESET_ALL}")

    def run(self):
        # Check sshpass
        if os.system("which sshpass > /dev/null") != 0:
            print(f"{Fore.RED}[!] sshpass not installed!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Install: pkg install sshpass -y{Style.RESET_ALL}")
            return
            
        while True:
            self.banner()
            self.menu()
            choice = input(f"\n{Fore.YELLOW}Choose menu [1-9]: {Style.RESET_ALL}")

            if choice == '1':
                self.connect()
            elif choice == '2':
                self.install_panel_protections()
            elif choice == '3':
                self.install_anti_kill()
            elif choice == '4':
                self.install_fs_hardening()
            elif choice == '5':
                self.install_kernel_hardening()
            elif choice == '6':
                self.install_anti_ddos()
            elif choice == '7':
                self.install_all()
            elif choice == '8':
                self.check_status()
            elif choice == '9':
                print(f"\n{Fore.RED}Goodbye!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}[✗] Invalid choice{Style.RESET_ALL}")

            if choice in ['2','3','4','5','6','7','8']:
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        app = ProtectPanel()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Bye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")