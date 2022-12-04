import requests

list1 = ["http://mailchi.mp/thisIsAMalicousURI",
       "http://dosbot.in/BadUmmK/YOkrebarm5",
       "http://gridxkin.com/wp-content123/plugins456/jbzpsmx"
       ]
for url in list1:
    host = url.split("//")[1].split("/")[0] #splitting whole url into only domain (ex: mailchi.mp)
    post_split = {"host": host} #formatting for API
    results = requests.post("https://urlhaus-api.abuse.ch/v1/host/", data=post_split) #query API
    m = results.json() #return everything from API
    ans = m['urls'] #pulling arl dict from m
    for i in ans: #i is each dict entry in urls
        id_h = i['id']
        threat = i['threat']
        status = i['url_status']
        url_cnt = m['url_count']
    print("Domain: " + host
          ,"\n\t" ,"ID: " + id_h, "\n\t", "Threat: " + threat, "\n\t", "Status: " + status, "\n\t", "URL Count: " + url_cnt)