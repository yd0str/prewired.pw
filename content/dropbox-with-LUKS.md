Title: Securing backups to Dropbox with LUKS
Category: Linux
Date: 2015-2-25 12:28
Slug: dropbox-with-LUKS
Tags: LUKS, security
Author: John Troon
Summary: Using Dropbox to synchronize a single binary file that is a LUKS-encrypted

###Dropbox meets LUKS
When it comes to my data, I like it private even though I've nothing to hide (ignore the paradox). I've been using [Dropbox](https://www.dropbox.com/) and [Swift (OpenStack Object Storage project)](http://docs.openstack.org/developer/swift/) to backup my data.

I tried writing a BASH script to recursively encrypt all the content of a folder with my public [GPG key](http://prewired.pw/2015/02/New-GPG.html) and sync the encrypted content of the folder with my remote backup (but with time it wasn't cool, not at all!). I had to plug-in my USB disk that has my private GPG keys each time I had to open any of the encrypted files, what a PITA!

Now, I've been using Dropbox to synchronize a single binary file that is LUKS-encrypted Linux file system. It might not seem cool but it's easier for me :) 

This process (of Dropbox+LUKS) is sort of a cliché right now but I'm just posting to share my simplified way of doing it...

###Step one:
Install Dropbox, head over to [Dropbox's site](https://www.dropbox.com/install?os=lnx) and get Dropbox. I'm currently using Ubuntu 14 (Yes, Ubuntu!).. or do a Dropbox headless Install via command line

```bash
32-bit:

cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -

64-bit:

cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -

Next, run the Dropbox daemon from the newly created .dropbox-dist folder.

~/.dropbox-dist/dropboxd
```

###Step Two:
Make sure you have a working Dropbox Account, if not, [register for a Dropbox account](https://www.dropbox.com/register). Then sign-in to Dropbox via your installed Dropbox client (make sure the dropbox daemon is running).

You should have a folder named Dropbox in your home folder after you've logged-in to your account. 

###Step Three:
Download [Luks-Ops](https://github.com/JohnTroony/LUKS-OPs/releases), a script that I've written to automate the basic LUKS operation on Linux.

```bash
# 1. Clone the repo
git clone https://github.com/JohnTroony/LUKS-OPs.git
cd LUKS-OPs

# 2. Change to super user
sudo su 

# 3. Copy the script to /bin  as luksOps
cp luks-ops.sh /bin/luksOps 

# 4. Move into the Dropbox folder to create the LUKS container
cd /home/user/Dropbox 

# 5. Create a LUKS container but don't mount it, DISKNAME is the label, 1000 is size in MB
luksOps new DISKNAME 1000

# 6. Move the created LUKS container (DISKNAME) to /home/user/Dropbox
mv /usr/DISKNAME .

# 7. Mount the LUKS container. This will ask for the pass phrase.
luksOps mount DISKNAME

# 8. Add files to the Mounted LUKS container then use the following command to exit
luksOps unmount-all

```

That is all, once you have the LUKS container in the ```~/Dropbox``` folder, you can always mount it, add files (You wouldn't want to be adding and removing large multimedia files to the container though.
), unmount it and let Dropbox sync the changes!



N.B: check luksOps menu for more options like to unmount a single volume instead of all.

Done!

### I've to checkout:
1. [EDS](http://sovworks.com/eds/)
2. [EncFS](http://en.wikipedia.org/wiki/EncFS)
3. [duplicity](http://duplicity.nongnu.org/)
4. [Tahoe-LAFS](https://tahoe-lafs.org/trac/tahoe-lafs/wiki)
5. [CryptKeeper](https://apps.ubuntu.com/cat/applications/precise/cryptkeeper/)

### Let's encrypt!
