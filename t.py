sites = {"youtube": "https://www.youtube.com", "wikipedia": "https://www.wikipedia.com","google": "https://www.google.com", "github": "https://github.com",}
a = str(sites.keys())
print(a)

def web(query):
    for site,url in sites:
            if "Open " + site.lower() in query.lower():
                print("aaaaaaa")

web("open youtube")                