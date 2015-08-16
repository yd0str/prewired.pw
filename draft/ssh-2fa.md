Title: Setting up SSH With Two-Factor Authentication
Category: Linux
Date: 2014-8-19 9:00
Slug: SSH-with-2FA
Tags: repost, Linux
Author: John Troon
Summary: Using 2FA to protect SSH 


Two-factor authentication adds a second level of authentication to an account log-in. When you have to enter only your username and one password, that's not considered a single-factor authentication. 2FA requires the user to have two out of three types of credentials before being able to access an account. The three types are:

*    Something you know, such as a Personal Identification Number (PIN), password, or a pattern
*    Something you have, such as an ATM card or phone
*    Something you are, such as a biometric like a fingerprint or voice print

[Source: cnet.com](http://www.cnet.com)

--------------------------------------------------------

Well, with SSH we can use Google Authenticator PAM module to add another level of security to the normal login. This can be a good idea if you have a cloud instance such as AWS services. I personally would like to endorse both our local robust cloud infrastructure built to support a wide range of applications, [KILI](http://www.kili.io) and [Angani](http://www.angani.co).


Before setting up the 2FA, make sure you have the `google authenticator` app installed on your phone (Android?), you can get support on how to install the app in Android, Blackberry or Apple device [here](https://support.google.com/accounts/answer/1066447?hl=en)

Now, decide which account you want to setup the 2FA for, I mean, if you use a normal account, you'll not be able to login as root. (I love root :D ). If you love root like me, login as root and follow along. I've my "google authenticator" app installed on my Samsung with Android 4.2.2 and I'm using Ubuntu 14.x

-------------------------------------------------------

### 1) Install required applications

```bash
apt-get install libpam-google-authenticator
```
On CentOS you will need to install `libpam-google-authenticator` from the source file.

```bash
yum -y groupinstall "Development Tools"
yum install pam-devel
yum -y install ntp
wget https://google-authenticator.googlecode.com/files/libpam-google-authenticator-1.0-source.tar.bz2
bunzip2 libpam-google-authenticator-1.0-source.tar.bz2
tar -xvf libpam-google-authenticator-1.0-source.tar
cd libpam-google-authenticator-1.0/
make
make install
```

### 2) Set up config files

    a) Open `/etc/pam.d/sshd` with your favourite editor and add the following line 

    	`auth required pam_google_authenticator.so` 

    make sure to the save changes.

    b) Then open `/etc/ssh/sshd_config` with your favourite file editor (again) and look for 

	`ChallengeResponseAuthentication no` 

    replace the `no`  with a `yes` and save the changes.

### 3) Setup the google-authenticator

Switch to the account to set-up and enter the following:

`google-authenticator`

This will enable you setup the google-authenticator through a series of yes (y) and no (n) questions. 
Make sure you select `time-based` for 	better security service, and save updates in the default file... 
You can follow along the other questions (they are easy pizzy and depends with your preferences).

NB: after chosing `Y` in the first option (authentication tokens to be time-based), a new secret key, 
verification code and an emergency scratch codes are generated with barcode also. 

After setting up the options to your preference(s), restart the ssh-server:
`service ssh restart`

Make sure on your system, the time is correctly set with the same time zone on your phone. I don't want to overemphasis on this, but you 	 need ntpd runninig on your system. 

On Ubuntu `apt-get install ntp` while on CentOS `yum -y install ntp` then start `ntpd` and enable it on 	 System boot.

### 4) Linking the APP on our	 phone...

Open the google-authenticator app on your phone and click the *add on account* option, then tap on the *Enter key provided* and enter your secret key.

NB: You can choose *scan a barcode* and scan the generated barcode but that didn't work for me.

### 5) Now test the set up....
Try login from a diffrent computer... You should get a verification prompt before the password/login-in for guys using ssh-keys.
 That's it! Easy! uh!
