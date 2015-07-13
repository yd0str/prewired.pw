Setting up SSH With Two-Factor Authentication
August 19, 2014

Two-factor authentication adds a second level of authentication to an account log-in. When you have to enter only your username and one password, that's considered a single-factor authentication. 2FA requires the user to have two out of three types of credentials before being able to access an account. The three types are:

    Something you know, such as a Personal Identification Number (PIN), password, or a pattern
    Something you have, such as an ATM card or phone
    Something you are, such as a biometric like a fingerprint or voice print

[source cnet.com]

Well, with SSH we can use Google Authenticator PAM module to add another level of security to the normal login. This can be a good idea if you have a cloud instance such as AWS services. I personally would like to endorse KILI : robust cloud infrastructure built to support a wide range of applications and *services*.


Before setting up the 2FA, make sure you have the "google authenticator" app in your phone, you can get support on how to install the app in Android, Blackberry or Apple device here

Now, decide which account you want to setup the 2FA for, I mean, if you use a normal account, you'll not be able to login as root. (I love root :D ). If you love root like me, login as root and follow along. I've my "google authenticator" app installed on my Samsung with Android 4.2.2 and I'm using Ubuntu 14.x

1)Install required files

sudo apt-get install libpam-google-authenticator


2) Set up config files

a) Open /etc/pam.d/sshd with your favourite editor and add the following line

auth required pam_google_authenticator.so

make sure you save changes

b) Again, open /etc/ssh/sshd_config with your favourite file editor and look for

ChallengeResponseAuthentication no

replace the no with a yes and save changes

3) Switch to the account to set-up and enter the following:

google-authenticator

This will enable you setup the google-authenticator through a
series of yes (y) and no (n) questions.
make sure you select "time-based" for better security service, and
save updates in the default file... You can follow along the other
questions (they are easy pizzy and depends with your preferences).

NB: after chosing Y in the first option
(authentication tokens to be time-based), a new secret key,
verification code and an emergency scratch codes are generated with
barcode also.

After setting up the options to your preference(s), restart the
ssh-server
service ssh restart

4) Open the google-authenticator app in your phone and click on
"add on account"then tap on the "Enter key provided" and enter your secret key.

NB: You can choose "scan a barcode" and scan the generated barcode
but that didn't work for me.

5) Now try login in from another machine....
You should get a verification prompt before the password/login-in
guys using ssh-keys

That's it! Easy! uh!
