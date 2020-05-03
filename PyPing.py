import os.path
from pathlib import Path

dir = Path('E:/tmp/python')
if os.path.exists(dir):
    os.makedirs(dir, exist_ok = True)
    #print("Didnt create new directory for :", dir)
else:
    os.makedirs(dir)
    #print(dir , "Created ")

ip_list = []
file = open(dir / "vlan100.txt", "w")

for ip in range(1,5):
    ip_list.append("10.2.0." + str(ip))
for ip in ip_list:
    response = os.popen(f"ping {ip} -n 2").read()
    if "Received = 2" and "Approximate" in response :
        file.write(f"UP   {ip}" + " Successful" + "\n")
    elif "Lost = 2" in response:
        file.write(f"DOWN {ip}" + " Request time out" + "\n")
    else:
        file.write(f"UNKNOWN {ip} " + "Host Unreachable " + "\n")
file.close()
exit()