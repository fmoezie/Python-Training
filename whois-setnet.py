#!/usr/local/bin/python3
'''
Network check tool checks an AS-SET's members
to see if a network is included. Whois command currently runs
against rr.ntt.net.
'''

import os

asset = input ("Input AS-SET to check ")
network = input("Input Network/CIDR to find ")
print ("Checking AS-SET " + asset + " for network " + network)

cmd = ("whois -h rr.ntt.net \!i" + asset +",1 | sed '/^\[/d' | sed 2\!d")


memberlist = os.popen(cmd).read().split()


for item in memberlist:
    cmd2 = ("whois -h rr.ntt.net \!g" + item)
    print("Checking Member " + item)
    nets = os.popen(cmd2).read().split()

    for net in nets:
        if net == network:
            print("Member " + item + " includes " + net)
        



