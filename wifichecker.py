# program to check available wifi
import subprocess 
nw = subprocess.check_output(["netsh","wlan","show","network"])
decoded_nw = nw.decode("ascii")
print(decoded_nw)
#print(decorded_nw)<|eom_id|><|start_header_id|>assistant
