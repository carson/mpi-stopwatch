mpi-stopwatch
=============

A simple latency timer written in mpi4py

The code was written for python 2.7.3 and test on ubuntu 12.10.

It requires the following packages to be installed:

sudo apt-get install openmpi-bin openmpi-doc libopenmpi-devp python-mpi4py

To test local computer parallel latency try:

'mpirun -np 2 python mpi-stopwatch.py'

To test network latency a hostfile with multiple host IPs is required:

'mpirun -np 2 -hostfile [list of cluster IPs] python mpi-stopwatch.py'
