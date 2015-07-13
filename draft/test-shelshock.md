
Oct 3, 2014
Testing for ShellShock in Linux (CentOS/OEL)

Below is a link to a simple bash script I've been using to test for shellshock vulns in my Linux setups. Though, it's not a script to really decide weather you are totally safe of not, due to the nature of shellshock and other different attack vectors that leverage it .

Keep following updates from CVE and other Linux news portals. I've been using the script on CentOS 6.5 and Oracle Linux 6.5.. I do understand all bash versions through 4.3 are affected but I discovered even after patching my systems with the first fix updates, my Bash binary was somehow still affected until I did another update/upgrade.

You can sample the script here >> https://github.com/JohnTroony/ShellShock-tes
