#!/data/data/com.termux/files/usr/bin/python3
# PROTECT PANEL V1.0.0 - DENGAN PILIHAN PER FILE
# Author: @ZledYazu

import os
import sys
import time
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

VERSION = "1.0.0"
AUTHOR = "@ZledYazu"

# ==================== PANEL PROTECTIONS ====================

PANEL_PROTECTIONS = [
    {
        "id": 1,
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
        "id": 2,
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
        "id": 3,
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
        "id": 4,
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
        "id": 5,
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
        "id": 6,
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
        "id": 7,
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
        "id": 8,
        "name": "🛡️ Anti Intip Mount",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/MountController.php",
        "code": """<?php
namespace Pterodactyl\\Http\\Controllers\\Admin;
use Illuminate\\View\\View;
use Illuminate\\Support\\Facades\\Auth;
use Pterodactyl\\Models\\Mount;
use Pterodactyl\\Http\\Controllers\\Controller;
class MountController extends Controller
{
    public function index(): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - You Are Not ID 1 ©Protect By @ZledYazu');
        }
        return view('admin.mounts.index');
    }
}"""
    },
    {
        "id": 9,
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
# ANTI-KILL SYSTEM
while true; do
    ps aux | grep -E "node.*writeSync|Buffer.*allocUnsafe|cluster\\.fork" | grep -v grep | awk '{print $2}' | xargs -r kill -9 2>/dev/null
    find /tmp /dev/shm /var/tmp -type f \\( -name "*.bin" -o -name "*.tmp" -o -name "*.img" \\) -delete 2>/dev/null
    rm -rf /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db 2>/dev/null
    sleep 5
done &
'''

FS_HARDENING = '''#!/bin/bash
# FILESYSTEM HARDENING
chattr +i /etc/passwd /etc/shadow /etc/group /etc/gshadow 2>/dev/null
mount -o remount,noexec,nosuid,nodev /tmp /var/tmp /dev/shm 2>/dev/null
mkdir -p /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chmod 000 /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chattr +i /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db 2>/dev/null
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
EOF
sysctl -p 2>/dev/null
'''

ANTI_DDOS = '''#!/bin/bash
# ANTI-DDOS
iptables -N ZLEDFR-DDOS 2>/dev/null
iptables -F ZLEDFR-DDOS
iptables -A ZLEDFR-DDOS -m limit --limit 25/second --limit-burst 50 -j ACCEPT
iptables -A ZLEDFR-DDOS -j DROP
iptables -A INPUT -p tcp --syn -m limit --limit 10/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP
iptables-save > /etc/iptables/rules.v4 2>/dev/null
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
        print(f"{Fore.CYAN}══════════════════════════════════════════════")
        print(f"  PROTECT PANEL V{VERSION} - FULL VERSION")
        print(f"  Author: {AUTHOR}")
        print(f"  STATUS: HARDENING + ANTI-KILL + ANTI-DDOS")
        print(f"══════════════════════════════════════════════{Style.RESET_ALL}")

    def main_menu(self):
        print(f"\n{Fore.WHITE}MAIN MENU")
        print(f"{Fore.YELLOW} 1{Fore.WHITE}. Connect to VPS")
        print(f"{Fore.YELLOW} 2{Fore.WHITE}. Install Panel Protections (Pilih per file)")
        print(f"{Fore.YELLOW} 3{Fore.WHITE}. Install Anti-Kill System")
        print(f"{Fore.YELLOW} 4{Fore.WHITE}. Install Filesystem Hardening")
        print(f"{Fore.YELLOW} 5{Fore.WHITE}. Install Kernel Hardening")
        print(f"{Fore.YELLOW} 6{Fore.WHITE}. Install Anti-DDOS")
        print(f"{Fore.YELLOW} 7{Fore.WHITE}. Install ALL Protections (3+4+5+6)")
        print(f"{Fore.YELLOW} 8{Fore.WHITE}. Check Status")
        print(f"{Fore.YELLOW} 9{Fore.WHITE}. Exit")
        print(f"{Fore.YELLOW}10{Fore.WHITE}. Install Panel Tema (Coming Soon){Style.RESET_ALL}")

    def panel_menu(self):
        print(f"\n{Fore.CYAN}┌─ PANEL PROTECTIONS MENU")
        for p in PANEL_PROTECTIONS:
            print(f"{Fore.WHITE}├─ {Fore.YELLOW}{p['id']}{Fore.WHITE}. {p['name']}")
        print(f"{Fore.WHITE}├─ {Fore.YELLOW}10{Fore.WHITE}. Install ALL (1-9)")
        print(f"{Fore.CYAN}└─ {Fore.YELLOW}0{Fore.WHITE}. Back to Main Menu{Style.RESET_ALL}")

    def ssh_command(self, cmd):
        full_cmd = f"sshpass -p '{self.password}' ssh -o StrictHostKeyChecking=no -p {self.port} root@{self.ip} '{cmd}' 2>/dev/null"
        return os.system(full_cmd) == 0

    def upload_file(self, remote_path, content):
        self.ssh_command(f"cp {remote_path} {remote_path}.bak 2>/dev/null")
        content = content.replace("'", "'\\''")
        return self.ssh_command(f"echo '{content}' > {remote_path}")

    def upload_script(self, remote_path, content):
        if self.upload_file(remote_path, content):
            self.ssh_command(f"chmod +x {remote_path}")
            return True
        return False

    def connect(self):
        print(f"\n{Fore.CYAN}┌─ VPS CONNECTION")
        self.ip = input(f"{Fore.WHITE}├─ IP Address: {Fore.YELLOW}").strip()
        self.password = input(f"{Fore.WHITE}├─ Password: {Fore.YELLOW}").strip()
        port_input = input(f"{Fore.WHITE}├─ Port (22): {Fore.YELLOW}").strip()
        self.port = int(port_input) if port_input else 22
        print(f"{Fore.CYAN}└─{Style.RESET_ALL}")

        print(f"\n{Fore.WHITE}Testing connection...{Style.RESET_ALL}")
        if self.ssh_command("echo 'Connected'"):
            print(f"{Fore.GREEN}✓ Connected successfully{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Connection failed{Style.RESET_ALL}")

    def install_single_protection(self, prot):
        print(f"{Fore.CYAN}  Installing {prot['name']}...{Style.RESET_ALL}")
        if self.upload_file(prot['path'], prot['code']):
            print(f"{Fore.GREEN}  ✓ Success{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}  ✗ Failed{Style.RESET_ALL}")
            return False

    def install_panel_protections(self):
        if not self.ip:
            print(f"{Fore.RED}✗ Connect to VPS first{Style.RESET_ALL}")
            return

        while True:
            self.panel_menu()
            choice = input(f"\n{Fore.YELLOW}Select protection [0-10]: {Fore.WHITE}").strip()

            if choice == '0':
                break

            elif choice == '10':
                print(f"\n{Fore.WHITE}Installing ALL panel protections...{Style.RESET_ALL}\n")
                success = 0
                for p in PANEL_PROTECTIONS:
                    if self.install_single_protection(p):
                        success += 1
                    time.sleep(0.5)
                print(f"\n{Fore.GREEN}✓ Installed {success}/9 protections{Style.RESET_ALL}")

            elif choice.isdigit() and 1 <= int(choice) <= 9:
                prot = next((p for p in PANEL_PROTECTIONS if p['id'] == int(choice)), None)
                if prot:
                    print(f"\n{Fore.WHITE}Installing single protection...{Style.RESET_ALL}\n")
                    self.install_single_protection(prot)
                else:
                    print(f"{Fore.RED}✗ Invalid choice{Style.RESET_ALL}")

            else:
                print(f"{Fore.RED}✗ Invalid choice{Style.RESET_ALL}")

            if choice != '0':
                input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")

    def install_anti_kill(self):
        print(f"\n{Fore.WHITE}Installing Anti-Kill System...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-kill.sh", ANTI_KILL_SCRIPT):
            self.ssh_command("nohup /usr/local/bin/anti-kill.sh > /dev/null 2>&1 &")
            print(f"{Fore.GREEN}✓ Anti-Kill installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_fs_hardening(self):
        print(f"\n{Fore.WHITE}Installing Filesystem Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/fs-hardening.sh", FS_HARDENING):
            self.ssh_command("bash /usr/local/bin/fs-hardening.sh")
            print(f"{Fore.GREEN}✓ Filesystem Hardening installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_kernel_hardening(self):
        print(f"\n{Fore.WHITE}Installing Kernel Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/kernel-hardening.sh", KERNEL_HARDENING):
            self.ssh_command("bash /usr/local/bin/kernel-hardening.sh")
            print(f"{Fore.GREEN}✓ Kernel Hardening installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_anti_ddos(self):
        print(f"\n{Fore.WHITE}Installing Anti-DDOS...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-ddos.sh", ANTI_DDOS):
            self.ssh_command("bash /usr/local/bin/anti-ddos.sh")
            print(f"{Fore.GREEN}✓ Anti-DDOS installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_all_hardening(self):
        self.install_anti_kill()
        self.install_fs_hardening()
        self.install_kernel_hardening()
        self.install_anti_ddos()
        print(f"\n{Fore.GREEN}✓ ALL HARDENING INSTALLED{Style.RESET_ALL}")

    def check_status(self):
        if not self.ip:
            print(f"{Fore.RED}✗ Connect to VPS first{Style.RESET_ALL}")
            return

        print(f"\n{Fore.WHITE}Checking protection status...{Style.RESET_ALL}\n")

        protected = 0
        for p in PANEL_PROTECTIONS:
            if self.ssh_command(f"grep -q '@ZledYazu' {p['path']} 2>/dev/null"):
                protected += 1
                print(f"{Fore.GREEN}✓ {p['name']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ {p['name']}{Style.RESET_ALL}")

        print(f"\n{Fore.CYAN}Anti-Kill:{Style.RESET_ALL}", end=" ")
        if self.ssh_command("pgrep -f anti-kill.sh > /dev/null"):
            print(f"{Fore.GREEN}✓ Running{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Not running{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Anti-DDOS:{Style.RESET_ALL}", end=" ")
        if self.ssh_command("iptables -L ZLEDFR-DDOS 2>/dev/null | grep -q ZLEDFR-DDOS"):
            print(f"{Fore.GREEN}✓ Active{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Not active{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}✓ Panel Protections: {protected}/9{Style.RESET_ALL}")

    def run(self):
        if os.system("which sshpass > /dev/null") != 0:
            print(f"{Fore.RED}sshpass not installed. Run: pkg install sshpass -y{Style.RESET_ALL}")
            return

        while True:
            self.banner()
            self.main_menu()
            choice = input(f"\n{Fore.YELLOW}Select [1-10]: {Fore.WHITE}").strip()

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
                self.install_all_hardening()
            elif choice == '8':
                self.check_status()
            elif choice == '9':
                print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                break
            elif choice == '10':
                print(f"{Fore.YELLOW}Coming Soon...{Style.RESET_ALL}")
                time.sleep(1)
            else:
                print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")

            if choice in ['2','3','4','5','6','7','8']:
                input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        ProtectPanel().run()
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")LL}")
        else:
            print(f"{Fore.RED}✗ Connection failed{Style.RESET_ALL}")

    def install_panel_protections(self):
        if not self.ip:
            print(f"{Fore.RED}✗ Connect to VPS first{Style.RESET_ALL}")
            return

        print(f"\n{Fore.WHITE}Installing panel protections...{Style.RESET_ALL}\n")
        success = 0

        for i, p in enumerate(PANEL_PROTECTIONS, 1):
            print(f"{Fore.CYAN}[{i}/9] {p['name']}{Style.RESET_ALL}")
            if self.upload_file(p['path'], p['code']):
                success += 1
                print(f"{Fore.GREEN}  ✓ Success{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}  ✗ Failed{Style.RESET_ALL}")
            print("")

        print(f"{Fore.GREEN}✓ Installed {success}/9 protections{Style.RESET_ALL}")

    def install_anti_kill(self):
        print(f"\n{Fore.WHITE}Installing Anti-Kill System...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-kill.sh", ANTI_KILL_SCRIPT):
            self.ssh_command("nohup /usr/local/bin/anti-kill.sh > /dev/null 2>&1 &")
            print(f"{Fore.GREEN}✓ Anti-Kill installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_fs_hardening(self):
        print(f"\n{Fore.WHITE}Installing Filesystem Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/fs-hardening.sh", FS_HARDENING):
            self.ssh_command("bash /usr/local/bin/fs-hardening.sh")
            print(f"{Fore.GREEN}✓ Filesystem Hardening installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_kernel_hardening(self):
        print(f"\n{Fore.WHITE}Installing Kernel Hardening...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/kernel-hardening.sh", KERNEL_HARDENING):
            self.ssh_command("bash /usr/local/bin/kernel-hardening.sh")
            print(f"{Fore.GREEN}✓ Kernel Hardening installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_anti_ddos(self):
        print(f"\n{Fore.WHITE}Installing Anti-DDOS...{Style.RESET_ALL}")
        if self.upload_script("/usr/local/bin/anti-ddos.sh", ANTI_DDOS):
            self.ssh_command("bash /usr/local/bin/anti-ddos.sh")
            print(f"{Fore.GREEN}✓ Anti-DDOS installed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed{Style.RESET_ALL}")

    def install_all(self):
        self.install_panel_protections()
        self.install_anti_kill()
        self.install_fs_hardening()
        self.install_kernel_hardening()
        self.install_anti_ddos()
        print(f"\n{Fore.GREEN}✓ ALL PROTECTIONS INSTALLED{Style.RESET_ALL}")

    def check_status(self):
        if not self.ip:
            print(f"{Fore.RED}✗ Connect to VPS first{Style.RESET_ALL}")
            return

        print(f"\n{Fore.WHITE}Checking protection status...{Style.RESET_ALL}\n")

        protected = 0
        for p in PANEL_PROTECTIONS:
            if self.ssh_command(f"grep -q '@ZledYazu' {p['path']} 2>/dev/null"):
                protected += 1
                print(f"{Fore.GREEN}✓ {p['name']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ {p['name']}{Style.RESET_ALL}")

        print(f"\n{Fore.CYAN}Anti-Kill:{Style.RESET_ALL}", end=" ")
        if self.ssh_command("pgrep -f anti-kill.sh > /dev/null"):
            print(f"{Fore.GREEN}✓ Running{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Not running{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Anti-DDOS:{Style.RESET_ALL}", end=" ")
        if self.ssh_command("iptables -L ZLEDFR-DDOS 2>/dev/null | grep -q ZLEDFR-DDOS"):
            print(f"{Fore.GREEN}✓ Active{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Not active{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}✓ Panel Protections: {protected}/9{Style.RESET_ALL}")

    def run(self):
        if os.system("which sshpass > /dev/null") != 0:
            print(f"{Fore.RED}sshpass not installed. Run: pkg install sshpass -y{Style.RESET_ALL}")
            return

        while True:
            self.banner()
            self.menu()
            choice = input(f"\n{Fore.YELLOW}Select [1-9]: {Fore.WHITE}").strip()

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
                print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")

            if choice in ['2','3','4','5','6','7','8']:
                input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        ProtectPanel().run()
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
