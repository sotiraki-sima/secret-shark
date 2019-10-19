import subprocess
import json
import sys

FILE_REGEXS = "regexs.json"
ACTIVE_REGEXS = "active_regexs"
ACTIVE_FILES = "active_files"
EXEC_GREP_SCRIPT = "grep_tunnel.sh"
EXEC_FIND_SCRIPT = "find_tunnel.sh"


scanning_path = str(sys.argv[1])

with open(FILE_REGEXS, 'r') as f:
    regexs_json = json.load(f)

def getFinding_GREP(proc):
    findings = []

    for line in proc.stdout:
        finding = {}
        out_line = str(line.rstrip().decode("utf-8") ).split(":")
        print(out_line)
        finding["file"] = out_line[0]
        finding["line"] = out_line[1]
        finding["match"] = str(out_line[2])
        findings.append(finding)

    return findings

def getFinding_FIND(proc):
    findings = []

    for line in proc.stdout:
        finding = {}
        out_line = str(line.rstrip().decode("utf-8") )
        findings.append(out_line)

    return findings

Output_Array = {}
Output_Array["grep"] = []
Output_Array["find"] = []


def exec_grep():

    for (regex_key, regex_value) in regexs_json[ACTIVE_REGEXS].items():
        output = {}
        output["regex_key"] = regex_key
        output["regex_value"] = regex_value
        print("Grep for: " + regex_value)
        proc = subprocess.Popen(['bash', EXEC_GREP_SCRIPT, regex_value, scanning_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output["findings"] = getFinding_GREP(proc)

        if(len(output["findings"])>0):
            Output_Array["grep"].append(output)
    
    #print(json.dumps(Regexs_Output_Array, indent=4, sort_keys=True))

def exec_find():
    Regexs_Output_Array = []
    for (file_key, file_value) in regexs_json[ACTIVE_FILES].items():
        output = {}
        output["file_key"] = file_key
        output["file_value"] = file_value
        print("Find for: " + file_value)
        proc = subprocess.Popen(['bash', EXEC_FIND_SCRIPT, scanning_path, file_value],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output["findings"] = getFinding_FIND(proc)
        
        if(len(output["findings"])>0):
            Output_Array["find"].append(output)
    

def main():
    exec_grep()
    exec_find()

print("#######################################################")
print("#                                                     #")
print("#                  JSON OUTPUT                        #")
print("#                                                     #")
print("#######################################################")

main()

print("#######################################################")

print(json.dumps(Output_Array, indent=4, sort_keys=True))

print("#######################################################")
print("#######################################################")
