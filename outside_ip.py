from requests import get

ip = get('https://api64.ipify.org').text
print('My public IP address is: {}'.format(ip))

print("")
input("Press ENTER to close")