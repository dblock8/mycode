#!/usr/bin/env python3

ipchk = input("Apply an IP address.")

if ipchk == "192.168.70.1":
    print("do not use the gateway address")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not enter a value")

