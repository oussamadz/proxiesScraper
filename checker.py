import pandas as pd
import urllib.request, socket
import datetime
import requests as rq
import threading
import queue
import sqlite3


socket.setdefaulttimeout(2)

conn = sqlite3.connect("data.db", check_same_thread=False)

def is_bad_proxy(item):
    try:
        proxy_handler = urllib.request.ProxyHandler({"http":item, "https":item})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [("User-agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0")]
        urllib.request.install_opener(opener)
        sock = urllib.request.urlopen("https://repairpal.com")
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return 1
    return 0

def set_rep(proxy, source):
    FILENAME = datetime.datetime.today().strftime("%Y-%m-%d.txt")
    print(f"GOOD: {proxy}")
    with open(f"good_proxy/{FILENAME}", 'a') as f:
        f.write(proxy + "\n")
    try:
        cur = conn.cursor()
        data = cur.execute(f"SELECT REP FROM REP WHERE IP = '{proxy}';").fetchone()
        if data:
            data1 = data[0]+1
            print(f"{proxy} REP set from {data[0]} to : {data1}")
            cur.execute(f"UPDATE REP SET REP = {data1} WHERE IP = '{proxy}';")
        else:
            cur.execute(f"INSERT INTO REP (IP, REP, SOURCE) VALUES ('{proxy}', 1, '{source}')")
        conn.commit()
    except Exception as e:
        print(e)

goodCount = {}
def countSource(dataset, source):
    try:
        dataset[source] +=1
    except KeyError:
        dataset[source] = 1
    return dataset

def work(name, qu):
    while not qu.empty():
        proxy = qu.get()
        condition = is_bad_proxy(proxy[0])
        if condition:
            pass
        else:
            set_rep(proxy[0], proxy[1])
            #goodCount = countSource(goodCount, proxy[1])
            #print(f"Good: {proxy[0]}")


df = pd.read_csv("data.csv", names=["ip","source"])

qq = queue.Queue()
threads = []
for index, row in df.iterrows():
    qq.put(row)

for i in range(8):
    nam = f"Thread-{i}"
    t = threading.Thread(target=work, name=nam, args=(nam, qq))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

#for index, row in df.iterrows():
#    if is_bad_proxy(row[0]):
#        continue
#    else:
#        goodCount = countSource(goodCount, row[1])
#        with open(f"good_proxy/{FILENAME}", 'a') as f:
#            f.write(row[0] + "\n")
#
#print(goodCount)
