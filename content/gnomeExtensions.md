Title: Rocking it! GNOME3 Shell Extensions..
Category: Linux
Date: 2015-4-27 14:15
Slug: gnome-extension
Tags: Linux
Author: John Troon
Summary: Some Tempting Gnome3 Shell Extensions...

I don't really give a tinker's damn about your desktop, if you have a picture of a unicorn as your wallpaper or a really old picture of Hitler smiling, that's up to you. Though, sometimes I do care about having my files/folders arranged, in a way I can remember everything on a "where-is-X" basis, and adjusting system's default settings.

What GNOME offers, even after a fresh install without tweaks, is satisfying. There are decent unbiased articles<sup>1</sup> written specifically about GNOME features and comparison made against KDE. Both Desktop-environments have their strengths and  weaknesses, choosing what fits you is kind of religious and experimental.

The list of projects<sup>2</sup> covered under GNOME is long. Here, I simply searched for some [extensions](https://extensions.gnome.org/) that are potentially helpful, below is a list of what I picked:

* [Coverflow alt-tab](https://extensions.gnome.org/extension/97/coverflow-alt-tab/) - Nice preview of the running applications when you use Alt+Tab.
* [Minimize all](https://extensions.gnome.org/extension/760/minimize-all/) - A lot of windows and sometimes you just want to see your desktop?
* [Simple dock](https://extensions.gnome.org/extension/815/simple-dock/) - Easy access to most used application?
* [Todo list](https://extensions.gnome.org/extension/162/todo-list/) - Easily distracted and want to keep track of activities to finish?
* [Drop Down Terminal](https://extensions.gnome.org/extension/442/drop-down-terminal/) - Just a bonus extension for getting a pseudo-terminal on the fly!

No other extra configs required if you are using the "GNOME Tweak Tool" for the installs, apart from the [Drop Down Terminal](https://extensions.gnome.org/extension/442/drop-down-terminal/) extension, which requires the *Vte library (version >= 0.31)* and the *gir typelib*.. 
```bash
install
 On Fedora/Arch: 'vte3' package
 On Debian/Ubuntu:  'gir-1.2-vte-2.*' package (not installed by default)
 On OpenSUSE: 'typelib-1_0-Vte-2.*' package (not installed by default)

Then, log out/restart.
```

If you ever build<sup>3</sup> your own extension, or find any other extension worth a try, share.. To share is divine!

> References:

> <sup>1</sup> [http://www.diffen.com/difference/GNOME_vs_KDE](http://www.diffen.com/difference/GNOME_vs_KDE)

> <sup>2</sup> [https://wiki.gnome.org/Projects](https://wiki.gnome.org/Projects)

> <sup>3</sup> [https://wiki.gnome.org/Projects/GnomeShell/Extensions/StepByStepTutorial](https://wiki.gnome.org/Projects/GnomeShell/Extensions/StepByStepTutorial)

![Screenshot](/images/shot.png "Alt+Tab Gnome3 Shell Extension")
