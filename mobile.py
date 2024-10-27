from ziraka import *

headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'cookie': 'vi=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaWQiOiI1Y2I3YzI1MC1hMzg0LTQxYjEtYWMzMi00ODI1ZDhjMWM0ZmMiLCJpYXQiOjE3MTM4NzU5NjUsImRudCI6dHJ1ZX0.KlEROVcMFmsHFV4UsBScorv8473BBbU_hGDd4Y2X2w8; optimizelyEndUserId=oeu1713875965738r0.7055305265571536; mobile.LOCALE=en; mdeConsentData=CP9hcQAP9hcQAEyAHAENAxEgAAAAAELAAAYgAAALzgCAAgABoAEwBeYAwSBkAAgABYAFQAOAAeABkADwAIgAVQAzABvAD0AH4AQgAhoBEAESAI4ASwAmgBgADDAHcAPaAfYB-gEUAI0ASIAkoBcwC9AGKANoAbgBIgCdgFDgKPAUiAtgBgwDDQGSAMnAZmA1cBrIDggHjgPaAhyOgbgALAAqABwAGQAPAAiABVgC4ALoAYgAzABvAD0AH4AQ0AiACJAEsAJoAUYAwABhgDRAHcAPaAfYB-gEUAIsAR0AkQBJQC5wF5AXoAxQBtADcAHUAQgAi8BIgCdgFDgKPAWwAwYBhoDJAGTgMqAZYAzMBq4DiwHjgPaAgCBDkhASAAWAFUALgAYgA3gB6AEcAMAAdwBFACUgFzAMUAbQA6gC0QGTgPHJQGgAEAALAA4ADwAIgAVQAuABiAENAIgAiQBHACjAGAAPwAuYBigDqAIQAReAkQBR4C2AGSAMnAe0BAEpApAAWABUADgAMgAeABEACkAFUAMQAZgA_ACGgEQARIAowBgADRgH4AfoBFgCOgEiAJKAXMAvIBigDaAG4AOoAi8BIgCdgFDgLYAYaAyQBk4DLAGsgOCAeOA9oCHJaAMAI4AYAA7gC9AMzAeO; bm_mi=C305253C8A5CE1B64B7137F309B8C5B4~YAAQiANJF0Z4asqOAQAAUt9lFRdlo2jaHNB9P++g7cg0eGakT12aO+ASii3SFD3Bck+5G+SahM6QWAP70aJVhjv74f8MOXzpppQLtD3Hf5erDIulWiJ7cXc7Cj8kxhkVpSFr1QJqlDaEcnl+gjY+4m+b23kwuQj3cdEJ4frwveGf7lgN4gZaxJKwLE/pKECA04290lToK4mtUUIPElbN4Jz7O8xNho4DZpr8qtKBNm5MBMmQ+ORJlHxMib8fckctrCFOUZwY+mr+dEkRIYlTSHB6VvPcdITotyzas/YBI4uj48R3VVsODXzgXsmLaaZG+2teRMIgIfyTPsoOcuXMp6o=~1; _abck=9A0B3C555F770626BC3DDAAC2694A9D2~-1~YAAQiANJF5lKbMqOAQAA8/R5FQvPLtngGSBfvt00RRPe+/U82Wysfasi9EDs6z64ZQe8Nnt139HbFjL6J9756s6ueYNnGEJCgUhMEYuYNhtMxdK0EQfpOOlqOvqx/ZnxCxYd6INKForseQSY6ii3kvS2YKy6ikugyd/U9YVTPFrVWsTPB5c6KOb9CVX7RifuxZaMIeJZX7Fbe7C4CZ8gceD5G8GUkVJv3dothvIG53TVCtCRXFU3rjsUlLRrYJfBpd0tr5CZ8UpS8pMbn+L5cmKMLlgmivTOYMIiwsu9Upuj1ptdFFQlNfQBKcNrKzGrN17/DOVlcpoz7MNHOH6VE+hFYzJniFi00ow+KkkAgDrGVYPCERaDtDJi3pqEZTEvpdZkxEIdMmZFPPDScQlFdKjk+ywAtr8=~0~-1~-1; ak_bmsc=ABEA936156264A2A2457A8E0D1FFFC1C~000000000000000000000000000000~YAAQiANJF5pKbMqOAQAA8/R5FRf2JOdTiM/OAzFkmwUaWBw+5zVWZvABvl3l43CE0aC/2BXY9IlKIBBUgVI5TS2KuX+P8BZfQKykpp3ShL1jQzrt55eedaB4chfSzbLmJ3gQUnwQ7ZcuHqBYCotX74Uz1uJ8WynOBiMKIw4nfRCxvhJL10JLn9AyhwkAJyb5LVXMQemEMezZw/OMOHFGBZROJC2ZLGy7yPMAIfb2dM6kVA83bklD5E9WwOrsyYGRBFz9EK/QzMFDufO3D/BEIWsn4YpmHDOwSW3QYpRO7BvYq3STieBg4rH4raJi1n5l4OdkDU/PIFGK36R75QwXIB54B291ABnDi+22UhEpvmJ0i8SkbM7CsCdj0XvDMv9+yU5kmmjpCTrgA+chjq57KlBVE+KeHVHbtHlfh2/ruozqRdgU4BEjBbUdCPHKIPLcxjLrDYjx+xNFEzQu+j+NBahtB5gn6eIDIMjp4lxELUZL/7jk2V8Xg5XPF5qTcg8qCaURVh5LsiR3jcovTGHxeeJNuWS7v5dbM70XWbLGOq701H7ai9Hs9SrN; bm_sv=D97619A102AD02BEDA3D165C75D4AA52~YAAQiANJF5tKbMqOAQAA8/R5FRfSRiJ6lkzLNt81GZaLDnGZqziMjhb3Vq2LpSUWJMS5dEkftyPa1W5BuUpTchPg3bVJURNZR9IdZI45C6CKoos2Eb2cQ0ignS59JDj6GBJSmLQy3AFsuOC2tCkuMNKrBc8T1fUHnE3cOb1VD5jYM6POA6AvsJcJ58jjBUsfiFy8MhrjhbOkUm4NmrooR+F6hkYJB3xGYiirjlqpGahxKMudGmNdCzYomSvWn8RR~1; bm_sz=216DB39ADE05C71B7545415DFF62DE8F~YAAQiANJF5xKbMqOAQAA8/R5FRcRI0LiApSa8tc1DQg8J3u7M1vAXe/c8k43u+m+yqwP1k9w7DHBr40D5MzjDzgpbrlaP08pg0wvazg/BB9XvnuojRiy0LjxAa9YV2P7TczP+omV/oV6t5A+a1ZyJN2ZpFapX0qHfF4uNE1a3CtowJpRr/L3hanQcXtqZEDTGLpeg84ZAVPtSghgtGfl2dsIeKYIQ8QjIpW/pBFwCW6DDwQmudUWCxxGUqnaiH0U+iZTD6RZ2LT4cr9rUt1oLnZqlaAAm4+Idi/OpeBqGpZDgfJV8AUpb2impXnkubo+gvfZGmvMkmNNGnyumpaN8bf76j7ouPgPRT14Cgp8edQieR5d0qHHHQB3bxiNGPZ26nByuRxb5eNWsMxfTTozWGLiOBOlxTFHXm+EkgGEa9I5V6dpWs4cZikE28Tyuw8F0xlqPQCdmzIuNdjnXwXtR8NeU9EJAltUC/hbB1C6cxF2d7agt152Uw2eMmOSXg1lytN0M/GhRq3iN/lz/Ain0r6S~3749426~3228229',
    'origin': 'https://suchen.mobile.de',
    'priority': 'u=1, i',
    'referer': 'https://suchen.mobile.de/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-mobile-api-version': '10',
    'x-mobile-client': 'de.mobile.header',
    'x-mobile-vi': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaWQiOiI1Y2I3YzI1MC1hMzg0LTQxYjEtYWMzMi00ODI1ZDhjMWM0ZmMiLCJpYXQiOjE3MTM4NzU5NjUsImRudCI6dHJ1ZX0.KlEROVcMFmsHFV4UsBScorv8473BBbU_hGDd4Y2X2w8',
}

def find_model(id):
    with open('mobile_de_default.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        for dat in data:
            if id.lower() == dat['n'].lower():
                return dat['i']

def get_mark_id(s,id,prnt):
    pasuxi = False
    data = s.get('https://m.mobile.de/consumer/api/search/reference-data/models/'+str(id),headers=headers)
    data = data.json()
    for a in data['data']:
        try:
            if prnt:print(a['label']+" => კოდი:"+str(a['value']),end=" | ")
            pasuxi = True
        except KeyError:
            for b in a['items']:
                if prnt:print(b['label']+" => "+str(b['value']),end=" | ")
            pasuxi = False
    return pasuxi

with requests.Session() as s:
    #tokken = authenticate(s)
    cart = input("სედანი = 1; ჯიპი = 5; უნივერსალი = 3 ")
    if cart == "": cart = 1
    year1 = input("წელი -დან ")
    if year1 == "": year1 = '2013'
    year2 = input("წელი -მდე ")
    if year2 == "": year2 = '2024'
    odo1 = input("გარბენი -დან KM ")
    if odo1 == "": odo1 = '100'
    odo2 = input("გარბენი -მდე KM ")
    if odo2 == "": odo2 = '300000'
    mark = input("ბრენდი ")
    mark = find_model(str(mark))
    get_mark_id(s,str(mark),True)
    qvekategoria = ""
    model = ""
    if get_mark_id(s,str(mark),False):
        model = input("\nმოდელი ")
    else:
        qvekategoria = input("\nმოდელი ")
    print(model)
    chartva = input("რამდენი განცხადება ჩატვირთოს Min:5,10,20,50,Max:100: ")
    if chartva == "": chartva = '100'
    if int(chartva) > 100:
        chartva = 100
    else:
        chartva = chartva
                    #https://suchen.mobile.de/fahrzeuge/search.html?dam=false&fr=2013%3A&isSearchRequest=true&ml=1%3A300000&ms=3500%3B20%3B20%3B&od=up&ref=srp&s=Car&sb=p&vc=Car
    response = s.get('https://suchen.mobile.de/fahrzeuge/search.html?dam=false&fr='+str(year1)+'%3A'+str(year2)+'&isSearchRequest=true&ml='+str(odo1)+'%3A'+str(odo1)+'&ms='+str(mark)+'%3B%3B4%3B&od=up&ref=srp&s=Car&sb=rel&vc=Car', headers=headers)
    soup = BeautifulSoup(response.content,features="html.parser")
    content = soup.find('article', {"data-testid":"result-list-container"})
    data_for = content.find_all("a")
    for a in data_for:
        print(a['href'])

    #print(response.content)
    #rqEvz FWtU1 YIC4W
    #<article