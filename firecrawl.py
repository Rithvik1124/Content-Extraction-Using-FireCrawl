import requests
from pandas import *


def StartExtraxn(headers, url):
    api_url="https://api.firecrawl.dev/v1/scrape"
    payload = {"formats": ["markdown", "json"],"onlyMainContent": True,
                   "waitFor": 0,"mobile": False,"skipTlsVerification": False,
                   "timeout": 30000,"location": {"country": "US"},"blockAds": True,
                   "url": str(url),"jsonOptions": {"systemPrompt": "Extract only the main content of the URL",
                   "prompt": ""}}
    response = requests.request("POST",api_url , json=payload, headers=headers)
    data=response.json()
    name=url[25:] #Removing  
    name=name[:name.index("/")]
    if data["success"]==False:
        print("Error Occurred: Insufficient Tokens")
    with open(name, 'w', encoding="utf-8") as file:
        file.write(str(data["data"]["markdown"]))
    print(name,"created\n Content:\n",data["data"]["markdown"][:200])
    


if __name__=="__main__":
    r= read_csv("Book1.csv")
        
    headers = {
    "Authorization": "Bearer fc-{API-KEY}", #Enter API-KEY Here
    "Content-Type": "application/json"
    }
    
    for url in r["URL"]:
        StartExtraxn(headers, url)
    
    
