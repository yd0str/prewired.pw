Title: Disk benchmark with bonnie in Linux
Category: repost, Linux
Date: 2014-6-24 8:00
Slug: disk-benchmark
Tags: repost, Linux
Author: John Troon
Summary: Disk benchmarking on Linux

*bonnie++* is a different tool compared to other disk testing tools, which are probably included in other performance monitoring tools like `vmstat` just to mention the most common one on any Linux install.

It runs a performance test of the filesystem I/O and uses C library calls hence simulating non exaggerated results. It writes 8KB blocks to estimate maximum sustained rate of transfer. To make results interesting and reliable, it cycles through rewriting and rereading to provide BEST simulation of filesystem usage.

After installing bonnie, all the details of the tests performed by Bonnie++ are contained in the file. `/usr/share/doc/bonnie++/readme.html`

For more details on usage, use `man bonnie++`

> NB: Despite the fact his tool is to aid in detecting bottlenecks with the Disks, it can cause a serious I/O contention while running. So don't run it on a production system that is live.

Below is an output from my Desktop with a T4300 dual processor (2100 MHz, Bus speed 800 MHz; GNU/Linux 3.13.0-27-generic Kernel, x86_64).

-------------------------------------------------------------------------------------------------------------------------
```bash
Writing a byte at a time…done
Writing intelligently…done
Rewriting…done
Reading a byte at a time…done
Reading intelligently…done
start ‘em…done…done…done…done…done…
Create files in sequential order…done.
Stat files in sequential order…done.
Delete files in sequential order…done.
Create files in random order…done.
Stat files in random order…done.
Delete files in random order…done.
Version 1.97 ——Sequential Output—— –Sequential Input- –Random-
Concurrency 1 -Per Chr- –Block– -Rewrite- -Per Chr- –Block– –Seeks–
Machine Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP /sec %CP
warlord 4G 232 97 47643 12 14893 4 819 99 35599 4 89.7 2
Latency 70015us 1807ms 1637ms 33484us 235ms 667ms
Version 1.97 ——Sequential Create—— ——–Random Create——–
warlord -Create– –Read— -Delete– -Create– –Read— -Delete–
files /sec %CP /sec %CP /sec %CP /sec %CP /sec %CP /sec %CP
16 9025 21 +++++ +++ 26989 51 23112 52 +++++ +++ 26063 52
Latency 84074us 966us 1410us 118us 2034us 2684us
1.97,1.97,warlord,1,1402393673,4G,,232,97,47643,12,14893,4,819,99,35599,4,89.7,2,16,,,,,

9025,21,+++++,+++,26989,51,23112,52,+++++,+++,26063,52,70015us,1807ms,1637ms,

33484us,235ms,667ms,84074us,966us,1410us,118us,2034us,2684us
```

