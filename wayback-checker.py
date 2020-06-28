import requests
import argparse
import json


print(""" 
$$\      $$\                     $$\                           $$\        $$$$$$\  $$\                           $$\                           
$$ | $\  $$ |                    $$ |                          $$ |      $$  __$$\ $$ |                          $$ |                          
$$ |$$$\ $$ | $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ $$ $$\$$ | \____$$\ $$ |  $$ |$$  __$$\  \____$$\ $$  _____|$$ | $$  |$$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$$$  _$$$$ | $$$$$$$ |$$ |  $$ |$$ |  $$ | $$$$$$$ |$$ /      $$$$$$  / $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$$  / \$$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      $$  _$$<  $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
$$  /   \$$ |\$$$$$$$ |\$$$$$$$ |$$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\__/     \__| \_______| \____$$ |\_______/  \_______| \_______|\__|  \__| \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                       $$\   $$ |                                                                                             #hOrcun                 
                       \$$$$$$  |                                                                                                              
                        \______/                                                                                                               
""")

parser = argparse.ArgumentParser(description="This tool extracts the registered URL and other inventory in the wayback web archive, and also checks the activity status of the urls. |IMPORTANT| If you select the active mode, it will check the status and size by making requests to the target site. However, if you choose passive mode, it will only search the urls via webarchive.")
parser.add_argument("--target", required=True)
parser.add_argument("--mode", required=True, choices=["active", "passive"], type=str,)
args = parser.parse_args()


            
def checks():
    url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=txt&fl=original&collapse=urlkey' % (args.target)
    r = requests.get(url)
    fle = open("target-list.txt", "w") 
    fle.write(r.text)
    with open("target-list.txt", "r") as fle: 
        for i in fle:
            strippedLine = i
            checkRequest = requests.get(strippedLine)
            status = checkRequest.status_code
            sizeUrl = len(checkRequest.content)
            if status == 200:
                print(statusColors.OK + "URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))
            elif status == 404:
                print(statusColors.notFound +"URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))
            elif status == 500:
                 print(statusColors.serverError +"URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))
            elif status == 401 or 400:
                 print(statusColors.notAuth +"URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))   
            elif status == 302 or 301:
                 print(statusColors.redirect +"URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))         
            else:
                print(statusColors.others +"URL:{}  STATUS ==> {} | LENGTH ==> {}".format(i, status, sizeUrl))

class statusColors:
    OK = '\033[92m'
    notFound = '\033[93m'
    serverError = '\033[91m'
    notAuth = '\033[0m'
    others = '\033[95m'
    redirect = '\033[94m'

def passiveCheck():
    url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=txt&fl=original&collapse=urlkey' % (args.target)
    r = requests.get(url)
    print(r.text)


checkType = args.mode
if checkType == "active":
    checks()
    print("scan complete")
elif checkType == "passive":
    passiveCheck()
else:
    print("please check your arguments and parameters.")

 