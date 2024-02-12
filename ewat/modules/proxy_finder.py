from proxyscrape import create_collector
from appearance.hue import *
import requests
collector = create_collector('default', 'http')
collector.refresh_proxies(force=False)

def run_proxy_scraper():
    num = raw_input(que("Number of proxies [(num)/all]: "))
    if num.isdigit():
        num = int(num)
        print (info("Printing " + str(num) + " proxies:"))
        for i in range(num):
            proxy = collector.get_proxy()
            print (proxy)
    else:
        r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&anonymity=elite&ssl=no')
        print (good("Showing all proxies: "))
        print (r.text)

