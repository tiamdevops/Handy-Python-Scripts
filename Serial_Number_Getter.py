# Authored by Tiam Abderezai

# The following script logs into a Cisco device and retrieves its serial number:

import re # import regular expression module
from netmiko import ConnectHandler # import netmiko module


credentials = {
    'device_type': 'cisco_ios',
    'ip': '172.16.1.1',
    'username': 'username',
    'password': 'password'
}

connection = ConnectHandler(**credentials)
output = connection.send_command('show inventory')
regexoutput = re.search('FOC.*', output)
print(regexoutput.group(0))
