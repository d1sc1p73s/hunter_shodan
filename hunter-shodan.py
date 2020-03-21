import shodan
import sys
import os

def logo():
    os.system("clear")
    """
     _    _             _
    | |  | |           | |
    | |__| |_   _ _ __ | |_ ___ _ __
    |  __  | | | | '_ \| __/ _ \ '__|
    | |  | | |_| | | | | ||  __/ |
    |_|  |_|\__,_|_| |_|\__\___|_|
     _____ _               _
    / ____| |             | |
   | (___ | |__   ___   __| | __ _ _ __
    \___ \| '_ \ / _ \ / _` |/ _` | '_ \
    ____) | | | | (_) | (_| | (_| | | | |
   |_____/|_| |_|\___/ \__,_|\__,_|_| |_|

                        By - Cyph70t

    """

def usage():
    logo()
    """
    -----------------
    :::::::TYPE::::::
    -----------------
          hunter-shodan full_addr  -->>   Get Info with IP Addr
          hunter-shodan half_addr    -->>   Get IP Addr info

    """
    
def ip_search():
    Api_Key=str(input("Enter Your Own Shodan API Key: "))
    List_Search=str(input("Enter What You Want To Search On Shodan: "))
    api = shodan.Shodan(Api_Key)
    try:
        results = api.search(List_Search)
        print ("Found Your Search: %s" %results['total'])
        for result in results['matches']:
            print ("IP Found: %s" %result['ip_str'])
            print (result['data'])
            print ("")
    except shodan.APIERROR as e:
        print ("Error Occured :: %s" %e)

def api_search():
    Api_Key=str(input("Enter Your Own Shodan API Key: "))
    List_Search=str(input("Enter What You Want To Search On Shodan: "))
    api = shodan.Shodan(Api_Key)
    try:
        results = api.search(List_Search)
        for result in results['matches']:
            print ("%s" %result['ip_str'])
    except:
        print ("Occured Error :: %s" % e)

        
if __name__ == '___main__' :
    arg = sys.argv[1:]

    if len(agr)!=1:
        usage()
    elif sys.argv[1] == "full_addr":
        logo()
        api_search()
    elif sys.argv[1] == "half_addr":
        logo()
        ip_search()
    else:
        usage()