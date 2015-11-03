Title: My GnuPG Transition
Category: Linux
Date: 2015-2-12 16:28
Slug: New-GPG
Tags: GPG, security
Author: John Troon
Summary: I'm slowly transiting from my old GnuPG keys to a new one.



### The old key, which I am transitional away from, is:

	pub  4096R/D5E28EE0 (0x192BA1E6D5E28EE0) 2014-02-22 
  	John Ombagi (Linux, DB & Infosec) <ombagi@promaxted.com>
	John Ombagi (Linux, DB & Infosec) <jayombagi@gmail.com>
 	Fingerprint=ACF5 FAFE 3C3D 4CE5 95D9  C31B 192B A1E6 D5E2 8EE0 

### The new key, to which I am transitioning, is:

	pub  4096R/AD3A484C (0x7b85a886ad3a484c) 2014-11-10 
	John Ombagi <ombagi@outlook.com>
	John Ombagi (Troon) <jayombagi@gmail.com>
	Fingerprint=CC89 97A6 1F78 304A 7D91  C27F 7B85 A886 AD3A 484C 

### [gpg-transition.txt](https://raw.githubusercontent.com/JohnTroony/My-GPG-key-transition/master/gpg-transition.txt) 
 Contains detailed info about my GPG transition/revocation.

### [sig1.txt](https://raw.githubusercontent.com/JohnTroony/My-GPG-key-transition/master/sig1.txt)
 Signature of the gpg-transition.txt using the old key 0x192BA1E6D5E28EE0

### [sig2.txt](https://raw.githubusercontent.com/JohnTroony/My-GPG-key-transition/master/sig2.txt)
 Signature of the gpg-transition.txt using the new key 0x7b85a886ad3a484c



##Updating

To fetch the full new key from a public key server using GnuPG, run:

```bash
	$ gpg --keyserver keys.gnupg.net --recv-key 0x7B85A886AD3A484C
```

If you have already validated my old key, you can then validate that the
new key is signed by my old key:

```bash
	$ gpg --check-sigs 0x7B85A886AD3A484C
```
Just incase you need to clarify anything about my GnuPG keys, reach me via **jayombagi at gmail dot com**

