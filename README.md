# ssh-to-a-single-router

This script starts by importing the ConnectHandler from Netmiko.

It is importanat that you've installed Netmiko before running this script. 

Next, we create a device named CSR and provide the necessary information for Netmiko, including device_type, IP address, username, and password.

Using the net_connect module, the script establishes a connection to the CSR device.

Once connected, input the  command 'sh ip int brief' and save the result in a variable called output.

Finally, the script prints the output and disconnects from the device.

 After connecting, it proceeds to execute the 'show ip interface brief' command, checking and displaying information about the IP interfaces on the router.
