import socket, struct
from appearance.hue import *
from appearance.error_handling import *
#Thanks D4v1nc1
def run_mask_ip():
    try:
        print (info("Enter the IP Address of the remote/local machine"))
        ip1 = input(que("IP Address: "))
        def ip2long(ip):
            p = ip.split(".")
            return str(((((int(p[0]) * 256 + int(p[1])) * 256) + int(p[2])) * 256) + int(p[3]))
        def ip_as_urlencoded(ip):
            en=""
            for i in ip :
                if i.isdigit() :
                    en += "%3{}".format(i)
                elif i == "." :
                    en += "%2E"
                elif i == ":" :
                    en += "%3A"
            return en
        
        packedIP = socket.inet_aton(ip1) 
        ip2num = struct.unpack("!L", packedIP)[0] 
        ip2num1 = str(ip2num)

        o_ip = '.'.join(format(int(x), '04o') for x in ip1.split('.'))

        #print ip1 + "-" + ip2num1
        print (info("http://" + str(ip2num1)))
        print (info("http://google.com@" + str(ip2long(ip1))))
        print (info("http://www.google.com@search@" + str(ip_as_urlencoded(ip1))))
        print (info("http://ANYWEBSITEHERE.com@" + o_ip))
        print (info("http://" + o_ip))
    
    except Exception as e:
        #run_error_handling(e)
        #print e
        raise

