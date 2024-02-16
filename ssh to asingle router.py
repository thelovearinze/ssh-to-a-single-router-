from netmiko import ConnectHandler
 
#First create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '172.20.42.10',
    'username': 'Love',
    'password': 'Cisc@o#2mT'
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
# Then send the command and print the output
output = net_connect.send_command('show ip int brief')
print (output)
 
# Finally close the connection
net_connect.disconnect()