import mmap
import io
import re
import subprocess
import json

with open('regexs.json', 'r') as f:
    regexs_json = json.load(f)

print(json.dumps(regexs_json, indent=4, sort_keys=True))



proc = subprocess.Popen(['bash','sh_tunnel.sh', 'om', 'scan.sh'],stdout=subprocess.PIPE)
for line in proc.stdout:
    out_line = str(line.rstrip().decode("utf-8") ) #str(bytes_string, 'utf-8')
    print(out_line)



