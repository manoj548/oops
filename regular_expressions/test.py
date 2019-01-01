import re
string = 'jeevan.kumar@plivo.com'
print(re.findall(r'[\w.]+@[\w.]+', string))
print(re.findall(r'[0-9a-zA-Z.-]+@[a-z.]+',string))

ip = "10.10.10.10"
print(re.findall(r'[\d.]+',ip))


