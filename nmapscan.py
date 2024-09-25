import nmap

# Define the port range and target
begin = 75
end = 80
target = '127.0.0.1'

# Create a PortScanner object
scanner = nmap.PortScanner()

# Loop through the ports and scan each one
for i in range(begin, end+1):
    # Scan the target on the specific port
    result = scanner.scan(target, str(i))
    
    # Check if the scan result for the port exists
    try:
        state = result['scan'][target]['tcp'][i]['state']
        print(f"Port {i} is {state}.")
    except KeyError:
        print(f"Port {i} is not responding or no information available.")
