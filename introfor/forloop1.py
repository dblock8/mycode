#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors

approved_vendors = ["cisco", "juniper", "big_ip"]


for x in vendors:
    print("The vendor is:" + x)  # each time through the loop print value of x

    if x not in approved_vendors:
        print("Not approved vendor!")

print("\nOur loop has ended.")  # when the loop ends print this

