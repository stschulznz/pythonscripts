# Simple python script take a standard host file with entries and converting it into the unbound dns resolver format
# Used to copy the dns4me host entries to a new file and creating a new file with the unbound dns resolver format. You can then reference this in the Custom options in pfsense with "server:include: /var/tmp/dns4me.conf"
import re

# Copy the dns4me host entries from your dns4me user console to a new txt file
f1 = open('dns4me.txt', "r")
# Write to a new file which you can then copy to your pfsense (unbound) server
f2 = open('dns4me.conf', "w")

for line in f1:
    ip = re.findall(r"(.*)\t",line)
    ipresult = str(ip)[2:-2]
    dns = re.findall(r"\t(.*)",line)
    dnsresult = str(dns)[2:-2]
    f2.write("local-data: " + '"' + (dnsresult) + " 60 IN A " + (ipresult) + '"' + "\n")
