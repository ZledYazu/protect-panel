#!/usr/bin/env python3
# PROTECT PANEL V1.0.0
# Author: @ZledYazu
# Fitur: Panel Protection + Anti-Kill + Anti-DDOS + Hardening

import os
import sys
import time
import json
import paramiko
import socket
import threading
import subprocess
import requests
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

# ==================== KONFIGURASI ====================

VERSION = "1.0.0"
AUTHOR = "@ZledYazu"

# ==================== PANEL PROTECTIONS ====================

PANEL_PROTECTIONS = [
    {
        "id": 1,
        "name": "🛡️ Anti Intip Server",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Servers/ServerController.php",
        "description": "Mencegah user selain ID 1 melihat server orang lain",
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
        $servers = Server::all();
        return view('admin.servers.index', ['servers' => $servers]);
    }
    public function view(Server $server): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View This Server ©Protect By @ZledYazu');
        }
        return view('admin.servers.view', ['server' => $server]);
    }
    public function destroy(Server $server)
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can Delete Servers ©Protect By @ZledYazu');
        }
        $server->delete();
        return redirect()->route('admin.servers')->with('success', 'Server deleted');
    }
}"""
    },
    {
        "id": 2,
        "name": "🛡️ Anti Intip User",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/UserController.php",
        "description": "Mencegah user selain ID 1 melihat user lain",
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
        $users = User::all();
        return view('admin.users.index', ['users' => $users]);
    }
    public function view(User $user): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Users ©Protect By @ZledYazu');
        }
        return view('admin.users.view', ['user' => $user]);
    }
    public function delete(Request $request, User $user)
    {
        $authUser = $request->user();
        if ($authUser->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can Delete Users ©Protect By @ZledYazu');
        }
        $user->delete();
        return redirect()->route('admin.users');
    }
}"""
    },
    {
        "id": 3,
        "name": "🛡️ Anti Intip Node",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Nodes/NodeController.php",
        "description": "Mencegah user selain ID 1 melihat node",
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
        $nodes = Node::all();
        return view('admin.nodes.index', ['nodes' => $nodes]);
    }
    public function view(int $id): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Nodes ©Protect By @ZledYazu');
        }
        $node = Node::findOrFail($id);
        return view('admin.nodes.view', ['node' => $node]);
    }
}"""
    },
    {
        "id": 4,
        "name": "🛡️ Anti Intip Location",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/LocationController.php",
        "description": "Mencegah user selain ID 1 melihat location",
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
        $locations = Location::all();
        return view('admin.locations.index', ['locations' => $locations]);
    }
    public function view(int $id): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Locations ©Protect By @ZledYazu');
        }
        $location = Location::findOrFail($id);
        return view('admin.locations.view', ['location' => $location]);
    }
}"""
    },
    {
        "id": 5,
        "name": "🛡️ Anti Intip Database",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/DatabaseController.php",
        "description": "Mencegah user selain ID 1 melihat database",
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
        $hosts = DatabaseHost::all();
        return view('admin.databases.index', ['hosts' => $hosts]);
    }
    public function view(int $host): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Databases ©Protect By @ZledYazu');
        }
        $host = DatabaseHost::findOrFail($host);
        return view('admin.databases.view', ['host' => $host]);
    }
}"""
    },
    {
        "id": 6,
        "name": "🛡️ Anti Intip API",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/ApiController.php",
        "description": "Mencegah user selain ID 1 melihat API keys",
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
        "description": "Mencegah user selain ID 1 melihat nest",
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
        $nests = Nest::all();
        return view('admin.nests.index', ['nests' => $nests]);
    }
    public function view(int $nest): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Nests ©Protect By @ZledYazu');
        }
        $nest = Nest::findOrFail($nest);
        return view('admin.nests.view', ['nest' => $nest]);
    }
}"""
    },
    {
        "id": 8,
        "name": "🛡️ Anti Intip Mount",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/MountController.php",
        "description": "Mencegah user selain ID 1 melihat mount",
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
        $mounts = Mount::all();
        return view('admin.mounts.index', ['mounts' => $mounts]);
    }
    public function view(string $id): View
    {
        $user = Auth::user();
        if ($user->id !== 1) {
            abort(403, '⛔ No Access - Only ID 1 Can View Mounts ©Protect By @ZledYazu');
        }
        $mount = Mount::findOrFail($id);
        return view('admin.mounts.view', ['mount' => $mount]);
    }
}"""
    },
    {
        "id": 9,
        "name": "🛡️ Anti Intip Settings",
        "path": "/var/www/pterodactyl/app/Http/Controllers/Admin/Settings/IndexController.php",
        "description": "Mencegah user selain ID 1 mengakses settings",
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

# ==================== ANTI-KILL & HARDENING SCRIPTS ====================

ANTI_KILL_SCRIPT = """#!/bin/bash
# ANTI-KILL SYSTEM - By @ZledYazu
# Mencegah serangan panel killer seperti index.js

echo "🛡️ ANTI-KILL ACTIVATED - V1.0.0"

# 1. Monitor proses mencurigakan
while true; do
    # Deteksi pattern index.js killer
    ps aux | grep -E "node.*writeSync|Buffer\.allocUnsafe|cluster\.fork" | grep -v grep | while read line; do
        pid=$(echo $line | awk '{print $2}')
        cmd=$(echo $line | awk '{for(i=11;i<=NF;i++) printf $i" "}')
        
        if [[ $cmd == *"writeSync"* ]] || [[ $cmd == *"Buffer.allocUnsafe"* ]] || [[ $cmd == *"cluster.fork"* ]]; then
            echo "🔥 KILLER DETECTED! PID: $pid"
            kill -9 $pid 2>/dev/null
            echo "$(date): Killed killer process $pid" >> /var/log/zledfr-kill.log
        fi
    done
    
    # 2. Cek file mencurigakan (pattern index.js)
    find /tmp /dev/shm /var/tmp /run /var/lib -type f \\( -name "*.bin" -o -name "*.tmp" -o -name "*.img" \\) -size +10M 2>/dev/null | while read file; do
        echo "🔥 SUSPICIOUS FILE: $file"
        rm -f "$file"
        echo "$(date): Removed $file" >> /var/log/zledfr-kill.log
    done
    
    # 3. Cek hidden directories (pattern index.js)
    for path in /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db; do
        if [ -d "$path" ]; then
            echo "🔥 HIDDEN DIR: $path"
            rm -rf "$path"
            echo "$(date): Removed $path" >> /var/log/zledfr-kill.log
        fi
    done
    
    sleep 3
done &
"""

FILESYSTEM_HARDENING = """#!/bin/bash
# FILESYSTEM HARDENING - By @ZledYazu

echo "🔐 Applying filesystem hardening..."

# 1. Protect critical files
chattr +i /etc/passwd 2>/dev/null
chattr +i /etc/shadow 2>/dev/null
chattr +i /etc/group 2>/dev/null
chattr +i /etc/gshadow 2>/dev/null
chattr +i /etc/ssh/sshd_config 2>/dev/null
chattr +i /var/www/pterodactyl/.env 2>/dev/null

# 2. Secure mount points
mount -o remount,noexec,nosuid,nodev /tmp 2>/dev/null
mount -o remount,noexec,nosuid,nodev /var/tmp 2>/dev/null
mount -o remount,noexec,nosuid,nodev /dev/shm 2>/dev/null

# 3. Create honeypot (jebakan untuk killer)
mkdir -p /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chmod 000 /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db
chattr +i /dev/shm/.cache /tmp/.sys /var/tmp/.journal /run/.lock /var/lib/.db 2>/dev/null

# 4. Real-time monitoring dengan inotify
nohup bash -c '
while true; do
    if command -v inotifywait &> /dev/null; then
        inotifywait -r -e create,write /var/www /tmp /dev/shm /var/tmp 2>/dev/null | while read path action file; do
            if [[ "$file" == *.bin ]] || [[ "$file" == *.tmp ]] || [[ "$file" == *.img ]] || [[ "$file" == *.js ]] && [[ "$file" != "index.js" ]]; then
                echo "🔥 ALERT: $file created in $path"
                rm -f "$path/$file" 2>/dev/null
                pkill -f "node.*$file" 2>/dev/null
            fi
        done
    fi
    sleep 5
done &' > /dev/null 2>&1 &

echo "✅ Filesystem hardening complete!"
"""

KERNEL_HARDENING = """#!/bin/bash
# KERNEL HARDENING - By @ZledYazu

echo "⚡ Applying kernel hardening..."

# 1. Sysctl hardening
cat >> /etc/sysctl.conf << 'EOF'

# ZLEDFR HARDENING V1.0.0
fs.protected_fifos = 2
fs.protected_regular = 2
fs.protected_symlinks = 1
fs.protected_hardlinks = 1
fs.suid_dumpable = 0
kernel.randomize_va_space = 2
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
kernel.printk = 3 3 3 3
kernel.unprivileged_bpf_disabled = 1
net.core.bpf_jit_harden = 2
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_rmem = 4096 87380 6291456
net.ipv4.tcp_wmem = 4096 65536 6291456
EOF

sysctl -p

# 2. Disable unused filesystems
echo "install cramfs /bin/true" >> /etc/modprobe.d/disable.conf 2>/dev/null
echo "install freevxfs /bin/true" >> /etc/modprobe.d/disable.conf 2>/dev/null
echo "install jffs2 /bin/true" >> /etc/modprobe.d/disable.conf 2>/dev/null
echo "install hfs /bin/true" >> /etc/modprobe.d/disable.conf 2>/dev/null
echo "install hfsplus /bin/true" >> /etc/modprobe.d/disable.conf 2>/dev/null

echo "✅ Kernel hardening complete!"
"""

ANTI_DDOS_SCRIPT = """#!/bin/bash
# ANTI-DDOS SYSTEM - By @ZledYazu

echo "🛡️ ANTI-DDOS ACTIVATED - V1.0.0"

# 1. Iptables rules untuk mitigasi DDOS
iptables -N ZLEDFR-DDOS 2>/dev/null
iptables -F ZLEDFR-DDOS

# 2. Rate limiting per IP
iptables -A ZLEDFR-DDOS -m limit --limit 25/second --limit-burst 50 -j ACCEPT
iptables -A ZLEDFR-DDOS -j DROP

# 3. Protect terhadap SYN flood
iptables -A INPUT -p tcp --syn -m limit --limit 10/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# 4. Protect terhadap UDP flood
iptables -A INPUT -p udp -m limit --limit 20/s --limit-burst 40 -j ACCEPT
iptables -A INPUT -p udp -j DROP

# 5. Protect terhadap ICMP flood
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 5/s --limit-burst 10 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

# 6. Connection tracking
iptables -A INPUT -m state --state INVALID -j DROP
iptables -A INPUT -m state --state NEW -j ZLEDFR-DDOS

# 7. Save rules
iptables-save > /etc/iptables/rules.v4 2>/dev/null

# 8. Monitor traffic mencurigakan
nohup bash -c '
while true; do
    # Deteksi traffic spike
    netstat -an | grep :80 | wc -l > /tmp/conn_count
    connections=$(cat /tmp/conn_count)
    
    if [ "$connections" -gt 1000 ]; then
        echo "$(date): HIGH TRAFFIC DETECTED - $connections connections" >> /var/log/zledfr-ddos.log
        # Tambah rules ketat
        iptables -I INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 -j DROP
    fi
    
    sleep 10
done &' > /dev/null 2>&1 &

echo "✅ ANTI-DDOS active!"
"""

SYSTEMD_SERVICE = """[Unit]
Description=ZLEDFR Panel Protect V1.0.0
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/zledfr-monitor.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""

MONITOR_SCRIPT = """#!/bin/bash
# ZLEDFR MONITOR V1.0.0 - By @ZledYazu

while true; do
    # 1. Cek panel status
    if command -v systemctl &> /dev/null; then
        systemctl is-active nginx > /dev/null || systemctl restart nginx
        systemctl is-active php8.1-fpm > /dev/null || systemctl restart php8.1-fpm
        systemctl is-active mysql > /dev/null || systemctl restart mysql
        systemctl is-active redis-server > /dev/null || systemctl restart redis-server
    fi
    
    # 2. Cek disk usage
    df -h / | awk 'NR==2 {if ($5+0 > 90) system("echo \"Disk usage high\" | wall")}'
    
    # 3. Cek load average
    load=$(uptime | awk -F'load average:' '{print $2}' | cut -d, -f1 | tr -d ' ')
    if (( $(echo "$load > 10" | bc -l) )); then
        echo "⚠️ High load: $load" >> /var/log/zledfr-monitor.log
    fi
    
    sleep 30
done
"""

CRON_JOBS = """# ZLEDFR PANEL PROTECTION V1.0.0
* * * * * root ps aux | grep -E "node.*writeSync|Buffer\.allocUnsafe|cluster\.fork" | grep -v grep | awk '{print $2}' | xargs -r kill -9 2>/dev/null
*/5 * * * * root find /tmp /dev/shm /var/tmp -type f \\( -name "*.bin" -o -name "*.tmp" -o -name "*.img" \\) -delete 2>/dev/null
*/10 * * * * root /usr/local/bin/anti-ddos.sh > /dev/null 2>&1
0 * * * * root /usr/local/bin/fs-hardening.sh > /dev/null 2>&1
"""

# ==================== CLASS UTAMA ====================

class ProtectPanel:
    def __init__(self):
        self.ssh = None
        self.ip = ""
        self.password = ""
        self.port = 22
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def banner(self):
        self.clear_screen()
        print(f"""{Fore.RED}
╔═════════════════════════════════════════════════════════════╗
║  ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗║
║  ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║   ║
║  ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║   ║
║  ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║   ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ║
║                                                             ║
║  ██████╗  █████╗ ███╗   ██╗███████╗██╗                      ║
║  ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║                      ║
║  ██████╔╝███████║██╔██╗ ██║█████╗  ██║                      ║
║  ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║                      ║
║  ██║     ██║  ██║██║ ╚████║███████╗███████╗                 ║
║  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝                 ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║  VERSION : 1.0.0                                            ║
║  AUTHOR  : @ZledYazu                                        ║
║  STATUS  : HARDENING + ANTI-KILL + ANTI-DDOS                ║
╚═════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """)
        
    def menu(self):
        print(f"\n{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗")
        print(f"║                    PROTECT PANEL MENU                      ║")
        print(f"╠═══════════════════════════════════════════════════════════╣")
        print(f"║  {Fore.YELLOW}1.{Fore.WHITE} 🔐 Connect to VPS                                   {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}2.{Fore.WHITE} 🛡️  Install Panel Protections ({len(PANEL_PROTECTIONS)} files)     {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}3.{Fore.WHITE} 💀 Install Anti-Kill + Hardening                      {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}4.{Fore.WHITE} 🌊 Install Anti-DDOS                                 {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}5.{Fore.WHITE} ⚡ Full System Protect (2+3+4)                       {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}6.{Fore.WHITE} 📋 Check Protection Status                           {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}7.{Fore.WHITE} 🔄 Update from Git                                   {Fore.CYAN}║")
        print(f"║  {Fore.YELLOW}8.{Fore.WHITE} 🚪 Exit                                              {Fore.CYAN}║")
        print(f"╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
    def connect(self):
        print(f"\n{Fore.YELLOW}[•] Masukin data VPS bro:{Style.RESET_ALL}")
        self.ip = input(f"{Fore.CYAN}IP Address: {Style.RESET_ALL}").strip()
        self.password = input(f"{Fore.CYAN}Root Password: {Style.RESET_ALL}").strip()
        port_input = input(f"{Fore.CYAN}SSH Port (default 22): {Style.RESET_ALL}").strip()
        self.port = int(port_input) if port_input else 22
        
        print(f"\n{Fore.YELLOW}[•] Nyambung ke {self.ip}:{self.port}...{Style.RESET_ALL}")
        
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(
                hostname=self.ip,
                port=self.port,
                username='root',
                password=self.password,
                timeout=30
            )
            print(f"{Fore.GREEN}[✓] Konek bro!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[✗] Gagal: {str(e)}{Style.RESET_ALL}")
            self.ssh = None
            return False
            
    def backup_file(self, remote_path):
        try:
            backup_name = f"{remote_path.replace('/', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
            self.ssh.exec_command(f"cp {remote_path} /root/{backup_name} 2>/dev/null")
            return True
        except:
            return False
            
    def upload_file(self, remote_path, content):
        try:
            # Backup dulu
            self.backup_file(remote_path)
            
            # Upload
            sftp = self.ssh.open_sftp()
            with sftp.open(remote_path, 'w') as f:
                f.write(content)
            sftp.close()
            return True
        except Exception as e:
            print(f"{Fore.RED}  ✗ Gagal: {str(e)}{Style.RESET_ALL}")
            return False
            
    def install_panel_protections(self):
        if not self.ssh:
            print(f"{Fore.RED}[✗] Konek VPS dulu bro! (menu 1){Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}[•] Install {len(PANEL_PROTECTIONS)} panel protections...{Style.RESET_ALL}\n")
        success = 0
        
        for i, prot in enumerate(PANEL_PROTECTIONS, 1):
            print(f"{Fore.CYAN}[{i}/{len(PANEL_PROTECTIONS)}] {prot['name']}{Style.RESET_ALL}")
            print(f"  📍 {prot['path']}")
            print(f"  📝 {prot['description']}")
            
            if self.upload_file(prot['path'], prot['code']):
                success += 1
                print(f"{Fore.GREEN}  ✓ Berhasil{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}  ✗ Gagal{Style.RESET_ALL}")
            print()
            
        print(f"{Fore.GREEN}[✓] Selesai! {success}/{len(PANEL_PROTECTIONS)} terinstall{Style.RESET_ALL}")
        
    def install_anti_kill(self):
        if not self.ssh:
            print(f"{Fore.RED}[✗] Konek VPS dulu bro!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}[•] Install Anti-Kill + Hardening...{Style.RESET_ALL}\n")
        
        scripts = [
            ("/usr/local/bin/anti-kill.sh", ANTI_KILL_SCRIPT, "Anti-Kill System"),
            ("/usr/local/bin/fs-hardening.sh", FILESYSTEM_HARDENING, "Filesystem Hardening"),
            ("/usr/local/bin/kernel-hardening.sh", KERNEL_HARDENING, "Kernel Hardening"),
            ("/usr/local/bin/zledfr-monitor.sh", MONITOR_SCRIPT, "Monitor System"),
            ("/etc/systemd/system/zledfr-protect.service", SYSTEMD_SERVICE, "Systemd Service"),
            ("/etc/cron.d/zledfr-protect", CRON_JOBS, "Cron Jobs")
        ]
        
        for path, content, name in scripts:
            print(f"{Fore.CYAN}[•] Installing {name}...{Style.RESET_ALL}")
            if self.upload_file(path, content):
                print(f"{Fore.GREEN}  ✓ Berhasil{Style.RESET_ALL}")
                if path.endswith('.sh'):
                    self.ssh.exec_command(f"chmod +x {path}")
            else:
                print(f"{Fore.RED}  ✗ Gagal{Style.RESET_ALL}")
                
        # Jalankan
        self.ssh.exec_command("bash /usr/local/bin/fs-hardening.sh")
        self.ssh.exec_command("bash /usr/local/bin/kernel-hardening.sh")
        self.ssh.exec_command("systemctl daemon-reload")
        self.ssh.exec_command("systemctl enable zledfr-protect.service")
        self.ssh.exec_command("systemctl start zledfr-protect.service")
        
        print(f"\n{Fore.GREEN}[✓] Anti-Kill + Hardening installed!{Style.RESET_ALL}")
        
    def install_anti_ddos(self):
        if not self.ssh:
            print(f"{Fore.RED}[✗] Konek VPS dulu bro!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}[•] Install Anti-DDOS...{Style.RESET_ALL}\n")
        
        path = "/usr/local/bin/anti-ddos.sh"
        if self.upload_file(path, ANTI_DDOS_SCRIPT):
            self.ssh.exec_command(f"chmod +x {path}")
            self.ssh.exec_command(f"bash {path}")
            print(f"{Fore.GREEN}[✓] Anti-DDOS installed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Gagal install Anti-DDOS{Style.RESET_ALL}")
            
    def check_status(self):
        if not self.ssh:
            print(f"{Fore.RED}[✗] Konek VPS dulu bro!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}[•] Cek status proteksi...{Style.RESET_ALL}\n")
        
        # Cek panel protections
        print(f"{Fore.CYAN}▶ PANEL PROTECTIONS{Style.RESET_ALL}")
        total = 0
        aktif = 0
        
        for prot in PANEL_PROTECTIONS:
            total += 1
            try:
                stdin, stdout, stderr = self.ssh.exec_command(f"grep -l '@ZledYazu' {prot['path']} 2>/dev/null || echo 'not'")
                result = stdout.read().decode().strip()
                if result and result != 'not':
                    aktif += 1
                    print(f"{Fore.GREEN}  ✓ {prot['name']}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}  ✗ {prot['name']}{Style.RESET_ALL}")
            except:
                print(f"{Fore.YELLOW}  ? {prot['name']}{Style.RESET_ALL}")
                
        # Cek anti-kill
        print(f"\n{Fore.CYAN}▶ ANTI-KILL SYSTEM{Style.RESET_ALL}")
        stdin, stdout, stderr = self.ssh.exec_command("systemctl is-active zledfr-protect.service")
        status = stdout.read().decode().strip()
        if status == "active":
            print(f"{Fore.GREEN}  ✓ Anti-Kill Active{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}  ✗ Anti-Kill Inactive{Style.RESET_ALL}")
            
        # Cek anti-ddos
        print(f"\n{Fore.CYAN}▶ ANTI-DDOS SYSTEM{Style.RESET_ALL}")
        stdin, stdout, stderr = self.ssh.exec_command("ps aux | grep anti-ddos | grep -v grep")
        if stdout.read():
            print(f"{Fore.GREEN}  ✓ Anti-DDOS Active{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}  ✗ Anti-DDOS Inactive{Style.RESET_ALL}")
            
        print(f"\n{Fore.GREEN}[✓] Panel Protections: {aktif}/{total}{Style.RESET_ALL}")
        
    def git_update(self):
        print(f"\n{Fore.YELLOW}[•] Update dari GitHub...{Style.RESET_ALL}")
        os.system("git pull")
        print(f"{Fore.GREEN}[✓] Update selesai!{Style.RESET_ALL}")
        
    def run(self):
        while True:
            self.banner()
            self.menu()
            pilih = input(f"\n{Fore.YELLOW}Pilih menu [1-8]: {Style.RESET_ALL}").strip()
            
            if pilih == '1':
                self.connect()
            elif pilih == '2':
                self.install_panel_protections()
            elif pilih == '3':
                self.install_anti_kill()
            elif pilih == '4':
                self.install_anti_ddos()
            elif pilih == '5':
                print(f"\n{Fore.YELLOW}[•] Install FULL SYSTEM PROTECT...{Style.RESET_ALL}")
                self.install_panel_protections()
                self.install_anti_kill()
                self.install_anti_ddos()
                print(f"{Fore.GREEN}[✓] FULL SYSTEM PROTECT SELESAI!{Style.RESET_ALL}")
            elif pilih == '6':
                self.check_status()
            elif pilih == '7':
                self.git_update()
            elif pilih == '8':
                print(f"\n{Fore.RED}[!] Dadah bro!{Style.RESET_ALL}")
                if self.ssh:
                    self.ssh.close()
                break
            else:
                print(f"{Fore.RED}[✗] Salah pilih bro!{Style.RESET_ALL}")
                
            if pilih in ['2','3','4','5','6']:
                input(f"\n{Fore.YELLOW}Enter buat lanjut...{Style.RESET_ALL}")

# ==================== MAIN ====================

if __name__ == "__main__":
    try:
        app = ProtectPanel()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Bye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {str(e)}{Style.RESET_ALL}")