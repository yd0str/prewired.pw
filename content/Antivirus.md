Title: Do we still need AntiVirus protection? 
Category: infosec
Date: 2015-10-10 11:41
Slug: are-AV-still-useful
Tags: AV, Antivirus, infosec, opinion
Author: John Troon
Summary: Is the role of AV in information security still active?


Antivirus (AV) softwares by design are supposed to protect the users from Malware infections; they act as a preventive countermeasure for Malware infections. The AV vendors are always tirelessly trying to analyze new Malware samples and update their products with latest Malware signatures.

###Protection is King but detection is Kong..

AV software uses various techniques to identify any malicious program/file, the level of self-protection in these malicious programs goes down to how skilled the VXer is and their goal...

Basically, for an AV product to determine if a program/file is malicious, it will do the following:

* A static scan using a set of signatures and types of packers used, if any.

* Sandbox and Heuristics - runtime analysis on some sort of OS emulation to determine what the program will do upon execution.

Bypassing all of the above AV detection process is easy, using crypters, custom payload encoders and packers; determining if the executable is running in an AV OS emulator or a real OS before executing the payload, setting timers for payload execution, killing the AV itself and so many other ways... e.g. check the `gamer.exe` I created to evade AV detection using simple `custom tricks` and a `Metasploit payload` :P 

![Sample Binary I crafted to evade AV](/images/vt.png "Virust Total result")
[virustotal.com/en/file/B7059AB990802D181E02CD25B667F25A43FF541E17EDC8C9F330F3F9CC81DC2A/analysis](https://www.virustotal.com/en/file/B7059AB990802D181E02CD25B667F25A43FF541E17EDC8C9F330F3F9CC81DC2A/analysis])

![Sample Binary I crafted to evade AV](/images/metascan.png "MetaScan - OPSWAT results")
[metascan-online.com/#!/results/file/9195e677c01f45d68defced6a34dad0c/regular](https://www.metascan-online.com/#!/results/file/9195e677c01f45d68defced6a34dad0c/regular)


Some sophisticated VXers use advance obscure techniques to avoid AV detection like taking advantage of some undocumented OS functionality or a 0day. No matter how good you think your AV vendor is trying to protect you, if their detection rate of these new rising Malware patterns is not high, you are living on false hope.

A good AV product, should be proactive, able to detect new Malware variants and neutralize such threats... So, are AV vendors able to protect users from these rapid evolution of Malware?

###The AV Industry : Money, Money, Money...

The motivation behind the AV industry is money and the same motivation is driving VXers too. Users on the other hand feel safe when they see fancy AV GUIs and lots of animated progress bars that have nothing to do with Malware detection....

Attackers and VXers are using new attack vectors that the AV industry have to keep up with, the creators of these Malware are always ahead of the game. AV vendors have set up their own labs to collect and analyze all sorts of different emerging Malware variants, and from other speculations (I've no proof if it's true or false) it has been said some of these AV vendors create Malware they can only neutralize, for commercial gains <sup>1</sup> .

Investing only on an AV product for protection and detection of potential attacks either in an enterprise network or personal computer is a bad idea. There are other considerations that you have to factor in your defensive model.

###Kill AVs or Not?

We can't rule out the fact that AVs still play a role in protecting our systems, but the way we utilize and make use of these products is what matters. An important focus is on the attack vector, for instance a Malware can download a Base64 encoded payload and execute it, another can use DNS query to get the same encoded payload, another can kill the AV process etc

Active Network monitoring and packet analysis are some of the very best ways to combine with AV features. Deploying an Intrusion Detection System (NIDS, HIDS), strict Firewall rules and ensuring all services that are not needed on the System are shutdown and also making sure the System gets all critical/non-critical updates etc. The other key thing is user-awareness, especially in an enterprise setting, train users not to click any link they see on their emails and websites. 

###Can We now get a Linux AV?

There is a common misconception that Linux is Malware-free, well, VXers are mainly motivated by money! The reason why Windows has a higher percentage of Malware hits it's not just about the Microsoft Windows OS but the market share it has, especially on personal computers. 

Linux on the other hand has a larger market share on Server Systems and it's also getting a grip on the personal computers as well. There is a rise of Linux Malware over the past decade and it's highly advisable to get a Linux AV if you are using Linux in an heterogeneous network.

The Linux Servers (or PCs) can be used to serve Malware to the Windows/Mac clients if not well scanned and monitored, these is especially in an enterprise network. other compromised Linux machines can be used for DDOS, hosting Malware, spam mail-server etc... Read about the recent
[Linux XOR Malware](http://blog.malwaremustdie.org/2014/09/mmd-0028-2014-fuzzy-reversing-new-china.html)...

###So what's the best AV?

To call an AV "the best", there are a lot of factors to consider and you have to compare with the other existing AV products. From my personal point of view, a good AV should be good in:

* Identifying malicious behavior in programs
* Identifying malicious behavior in documents and web-pages
* Identifying malicious patterns in network packets
* Adapting and identifying new malicious patters based on previous found patterns
* Self protection (so Malware can't kill it)
* Scanning compressed and packed files
* Providing some Firewall features (block malicious traffic even if the IDS/FW allowed).

Having an AV that can do all the above without bias is pretty hard and will definitely be expensive, tailored for the enterprise networks.
[AV-Test](http://www.av-test.org) is an independent IT-Security Institute, recently they did a research on trying to analyze the common AV vendors products and their detection rate on some 900 actually "already known" attackers for Linux and 12,000 attackers for Windows.

Only `Kaspersky Endpoint Version` achieved 100-percent detection under Linux and only the security package from `Symantec` achieved 100% detection under Windows (compared to their counterparts). 

Please note that these results from the tests doesn't satisfy that the AVs having 100% detection rates are the best security products for your network, as a matter of fact security is a service not a product. Today they might be able to detect 100% attackers, tomorrow maybe 50%. And another thing, if you read such reports to help you make decision on what AV to deploy on your network hosts, be reminded this is a limited test (all AV vendors use) to come up with the detection rates on the identified threats. What if the unidentified attackers are more than the identified? 


![AV-Test Results, 2015](/images/av-test.png "AV test on detection rate on Windows and Linux")

Conclusion
-----------

AV vendors have to find a way to stay relevant and useful in combating Malware otherwise they will soon be phased out by more advance prevention and detection systems. As the commonly used checksum & hash functions for building up some signatures are being cryptographically flawed (e.g. MD5<sup>2</sup> and SHA1<sup>3</sup> collisions) the process of coming up with the AV Signatures is wanting.

Before investing on an AV for your hosts in a network, do a deep threat modeling to identify your potential treats and build up a defensive mechanism for your network mainly based on your threat model for best results on a reasonable budget.

As much as network log analysis and captured network traffic analysis are important especially in an incident response, invest in setting up a real-time network traffic analysis and defense, even if you have an AV deployed. Be proactive and focus on preventing-detecting-neutralizing threats. 

####Reference:

* <sup>1</sup> - [Kaspersky AV Accused of Creating Malware for over 10 years](http://thenextweb.com/insider/2015/08/14/kaspersky-antivirus-accused-of-creating-malware-for-over-10-years/)

* <sup>2</sup> -[MD5 Collision Demo](http://www.mathstat.dal.ca/~selinger/md5collision/)

* <sup>3</sup> -[The SHAppening: freestart collisions for SHA-1](https://sites.google.com/site/itstheshappening/)

* [The contemporary AV industry and its problems](https://securelist.com/analysis/36063/the-contemporary-antivirus-industry-and-its-problems/)

