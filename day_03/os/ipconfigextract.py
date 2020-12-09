import subprocess

# subprocess.call("ipconfig -all", shell=True)

content = subprocess.check_output("ipconfig -all", shell=True).decode().split("\r\n")
phyaddrs = []
for line in content:
    if("Physical Address" in line):
	    phyaddrs.append(line.split(":")[1].strip())

print(phyaddrs)