Title: Queue & Load Average in Linux
Category: Linux
Date: 2015-3-19 14:15
Slug: Queue-and-CPULoads
Tags: Linux
Author: John Troon
Summary: Something about Queue & Load Average in Linux

Queue is the current runtime queue for processes. Load averages are measurements of this metric over 5-, 10-, and 15- minute
intervals. So, the runtime queue is a count of the number of processes ready to run at any given point in time.

```bash
$ uptime
 14:17pm  up   0:57,  6 users,  load average: 0.37, 0.54, 0.44
```
That means, a value less than 1 is not bad and there is never a process idling in the queue waiting to be run. Therefore, when
the load averages start to rise over 1, know there is always a process ready and waiting to be scheduled!

Obviously, when the load averages rise above 1 there is something in the system being delayed. If it's a mission critical system, running some serious stuff in a production environment, getting an additional CPU can solve the problem and ensure that there is a better chance of “schedulable” time.

----------

These data can be monitored through:
```bash
$ uptime
$ top
$ vmstat
```
uptime somehow has a nice output of the load average data.


----------

Read:

1. [Understanding Linux CPU Load](http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages)
2. [Understanding Linux Load Average – Part 1](https://prutser.wordpress.com/2012/04/23/understanding-linux-load-average-part-1)