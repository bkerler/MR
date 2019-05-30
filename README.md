# Mobile Revelator

## Smartphone Forensic Tools

- Generate report with open python scripts from Android Binaries

- Cryptutils

- Open up images, parse and recover deleted data

- Imaging tools

## Installation

### Windows
[Download MR 2.2.7 64Bit Windows](https://revskills.de/MR_64Bit_Windows.exe)
- Just install. Scripts will be added to "User Documents/MobileRevelator"

### Linux

These are the instructions for how to install MR on a Debian distribution of Linux. For other distributions, you can follow [CyberCiti's instructions to view packages.](https://www.cyberciti.biz/faq/show-display-get-installed-packages-software-list-linux-freebsd-openbsd/)

This program requires libssl 1.0.0 and OpenSSL 1.0.2. It will not run with updated versions of those packages, so below are instructions for how to install them on your system.

1. `wget https://revskills.de/MR_x86_64_Linux.zip`
2. `unzip MR_x86_64_Linux.zip`
3. Check libssl version with `dpkg --get-selections | grep libssl`
4. If libssl version is 1.0.0 skip to step 11. Otherwise continue.
5. `cd etc/apt`
6. `nano sources.list`
7. Add `deb http://security.debian.org/debian-security jessie/updates main`
8. Save and Exit. 
9. Restart your system.
10. `sudo apt install libssl1.0.0`
11. Check openssl version with `openssl version`
12. If version is 1.0.2, skip to step 14. Otherwise continue.
13. [Follow this guide to install OpenSSL 1.0.2](https://www.howtoforge.com/tutorial/how-to-install-openssl-from-source-on-linux/)
14. `./MR_x86_64_Linux.appimage`

- Template/Plugins are stored in "~/Documents/MobileRevelator"
- If the AppImage is not executable by default, use `chmod +x MR_x86_64_Linux.appimage` to make it executable.
- If the app crashes, run `export QT_NO_FT_CACHE=1` first.

## Examples

### Partition View
![Partition View](https://revskills.de/mr1.png)

### File View
![File View](https://revskills.de/mr2.png)

### SQLite View
![SQLite View](https://revskills.de/mr3.png)

### Timeline Module
![Timeline Module](https://revskills.de/mr4.png)

### JPG Carver
![JPG Carver](https://revskills.de/mr5.png)


Enjoy :)
