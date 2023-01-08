# Simple-Packet-Sniffer

<pre>
       .__               .__                                __           __                  .__  _____  _____             
  _____|__| _____ ______ |  |   ____   ___________    ____ |  | __ _____/  |_    ______ ____ |__|/ ____\/ ____\___________ 
 /  ___/  |/     \\____ \|  | _/ __ \  \____ \__  \ _/ ___\|  |/ // __ \   __\  /  ___//    \|  \   __\\   __\/ __ \_  __ \
 \___ \|  |  Y Y  \  |_> >  |_\  ___/  |  |_> > __ \\  \___|    <\  ___/|  |    \___ \|   |  \  ||  |   |  | \  ___/|  | \/
/____  >__|__|_|  /   __/|____/\___  > |   __(____  /\___  >__|_ \\___  >__|   /____  >___|  /__||__|   |__|  \___  >__|   
     \/         \/|__|             \/  |__|       \/     \/     \/    \/            \/     \/                     \/       
</pre>
<br>

### This is a command line packet scanner utility for Windows based on Python. When in a network, you can use this to sniff http packets for leaked usernames and passwords, thereby performing MITM.


### NOTE: You need to install scapy module before using this tool.
### Installation for scapy -->
<code>pip install scapy</code>

### OR

<code>pip3 install scapy-python3</code>

## How to use?

<code> python network_scanner.py </code>

### Example -->
<code>
[+] HTTP Request >>>b'testphp.vulnweb.com/userinfo.php'
b'uname=USER&pass=PASSWORD' 
</code>
