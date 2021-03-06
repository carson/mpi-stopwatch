#!/usr/bin/env python

"""
A simple latency timer written in mpi4py

Copyright (C) 2013 Carson Reynolds

mpi-stopwatch.py is free software released under the GNU General Public License. See gpl.txt for more information.

The code was written for python 2.7.3 and test on ubuntu 12.10.

It requires the following packages to be installed:

sudo apt-get install openmpi-bin openmpi-doc libopenmpi-devp python-mpi4py ptpd

To test local computer parallel latency try:

'mpirun -np 2 python mpi-stopwatch.py'

To test network latency a hostfile with multiple host IPs is required:

'mpirun -np 2 -hostfile [list of cluster IPs] python mpi-stopwatch.py'

Cluster clocks are assumed to be synchronized using ptp.
"""

__author__ = "Carson Reynolds and Hyuno Kim"
__license__ = "GPL"

from mpi4py import MPI
import datetime

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0: # launching process
        start = datetime.datetime.now()
        comm.send(start, dest=1, tag=11)
        stop = datetime.datetime.now()
        comm.send(stop, dest=1, tag=12)
elif rank == 1: # spawned processes
        startdata = comm.recv(source=0, tag=11)
        recvstart = datetime.datetime.now()
        stopdata = comm.recv(source=0, tag=12)
        recvstop = datetime.datetime.now()

comm.Barrier()   # wait for all hosts

# if a spawned node, report communication latencies in microseconds
if rank == 1:
        startdelta = recvstart - startdata
        print 'start difference (uS) : ' + str(startdelta.microseconds) + '\n'
        stopdelta = recvstop - stopdata
        print 'stop difference (uS) : ' + str(stopdelta.microseconds) + '\n'
        transmitdelta = stopdata - startdata
        print 'transmit difference (uS) : ' + str(transmitdelta.microseconds) + '\n'
