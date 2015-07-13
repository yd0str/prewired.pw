November 11, 2014
# Considerations in software design for multi-core multiprocessor architectures
Are we taking advantage of the computing power we have? 

Title: My GnuPG Transition
Category: Linux
Date: 2015-2-12 16:28
Slug: New-GPG
Tags: GPG, security
Author: John Troon
Summary: I'm slowly transiting from my old GnuPG keys to a new one.


Computing power is ever increasing not just with high clock cycles but with multiple logical processors referred as cores. Clock cycles determine the number of instructions a processor can process within a given interval of time. The more the number of clocks, the more the instructions potentially executed in terms of KHz (thousands of operations per second), MHz (millions of operations per second), and the current GHz (billions of operations per second).

A Core has it's own ALU and caches L2 and L3, among other elements to carry out instructions. Basically, cores (logical processors) enable parallel execution of different parts of a program, or even different programs, simultaneously. These new generation architectures, makes the OS assume there are more than one processor in the system even though there is a single physical chip on board.

Generally speaking, a machine with a low clock cycle speed but with multiple cores can be faster compared to a machine with a single processor and high clock cycle speeds. However, I've had both bad times and good times while trying to crunch some “big-data”, encrypting huge file-system etc. It's so frustrating when you get low speeds while using these modern high-end machines for your day-to-day computing.

Having a high-end machine (Laptop/Desktop/Server) doesn't necessary mean you'll automatically have the best computing experience.. The problem is not always with your hardware but the architecture of the software using these new generation processors.

So, what's the importance of having a laptop with 4 cores if only 1 core is operating while the rest of the cores sleep? I mean, it's like employing 4 employees and while 1 is working, the rest just eat and fart in your office.

People who use their computers for basic computing like editing files, working with ledgers, watching a movie etc won't really notice any serious performance issues compared to a programmer compiling application from source code or a SysAdmin who is trying to compress and backup gigabytes of data.
Simple Test

As a simple test, I'm using my Laptop ( i7-2640M, sandy-bridge, 4 Cores each with 2.80 GHz) running Debian to compress two files with bzip2 then compare the results with pbzip2. Well, there is a performance note about bzip2 (block-sorting file compressor) on it's man page and pbzip2 is a parallel implementation of the bzip2 that uses pthreads and achieves near-linear speedup on SMP machines.

Using pbzip2 was faster compared to bzip2 and the following screen shots shows the CPU history for both respectively.

pbzip2 CPU history:

bzip2 CPU history:
pbzip makes use of the four CPUs to compress the files and the result is far impressive compared to using bzip2. I've avoided the nitty gritty details of bzip2/pbzip since this is not a post about the tools. However, you can explore pbzip and set other options like Load average and Block size. I tried reading the files to be compressed into memory then split the compression work among the CPUs with pbzip and the performance was still good.

Conclusion:

Are we really making use of the computing power we have?
We can only make good use of these powerful computation resources if we design our applications and programs to take advantage of the power in the underlying hardware they run on, be it in a distributed environment, cloud computing or in a simple multi-core computer.

Mission critical systems need a system analysts who can identify common bottlenecks and other performance issues that can be resolved or even design new parallel algorithms in the application stack.
