#./#/#/#. Coded By Giorgi Zirakashvili #./#/#/#.#
from ziraka import *

print(" ### IAAI ძებნის ფილტრი ### ")

today = date.today()
end_date = date.today() + timedelta(days=20)
end_date = end_date.strftime("%m%d%Y")


with requests.Session() as s:
    tokken = authenticate(s)

    cart = input("სედანი = 1; ჯიპი = 5; უნივერსალი = 3 ")
    if cart == "": cart = 1
    year1 = input("წელი -დან ")
    if year1 == "": year1 = '2013'
    year2 = input("წელი -მდე ")
    if year2 == "": year2 = '2024'
    odo1 = input("გარბენი -დან ")
    if odo1 == "": odo1 = '100'
    odo2 = input("გარბენი -მდე ")
    if odo2 == "": odo2 = '100000'
    mark = input("ბრენდი ")
    model = input("მოდელი ")
    chartva = input("რამდენი განცხადება ჩატვირთოს Min:5,10,20,50,Max:100: ")
    if chartva == "": chartva = '100'
    if int(chartva) > 100:  
        chartva = 100
    else:
        chartva = chartva
    if model != "":
        json_data = {
        'Searches': [
            {'Facets': [{
                        'Group': 'Make',
                        'Value': str(mark).upper(),},],
                'FullSearch': None,
                'LongRanges': None,
            },{'Facets': None,
                'FullSearch': None,
                'LongRanges': [{
                        'From': int(odo1),
                        'Name': 'ODOValue',
                        'To': int(odo2),},],
            },{'Facets': [{
                        'Group': 'StartsDesc',
                        'Value': 'Run & Drive',},],
                'FullSearch': None,
                'LongRanges': None,
            },{
                'Facets': None,
                'FullSearch': None,
                'LongRanges': [{
                        'From': int(year1),
                        'Name': 'Year',
                        'To': int(year2),},],
            },{'Facets': [{
                    'Group': 'Model',
                    'Value': str(model.upper()),
                    },],
                'FullSearch': None,
                'LongRanges': None,
            },{'Facets': [{
                        'Group': 'IsDemo',
                        'Value': 'False',},],
                'FullSearch': None,
                'LongRanges': None,
            },
        ],
        'ZipCode': '',
        'miles': 0,
        'PageSize': int(chartva),
        'CurrentPage': 1,
        'Sort': [{
                'IsGeoSort': False,
                'SortField': 'AuctionDateTime',
                'IsDescending': False,},],
        'SaleStatusFilters': [{
                'SaleStatus': 1,
                'IsSelected': True,},],
        'BidStatusFilters': [{
                'BidStatus': 6,
                'IsSelected': True,},],
        }
    else:
        json_data = {
        'Searches': [
            {'Facets': [{
                        'Group': 'Make',
                        'Value': str(mark).upper(),},],
                'FullSearch': None,
                'LongRanges': None,
            },{'Facets': None,
                'FullSearch': None,
                'LongRanges': [{
                        'From': int(odo1),
                        'Name': 'ODOValue',
                        'To': int(odo2),},],
            },{'Facets': [{
                        'Group': 'StartsDesc',
                        'Value': 'Run & Drive',},],
                'FullSearch': None,
                'LongRanges': None,
            },{
                'Facets': None,
                'FullSearch': None,
                'LongRanges': [{
                        'From': int(year1),
                        'Name': 'Year',
                        'To': int(year2),},],
            },
            {'Facets': [{
                        'Group': 'IsDemo',
                        'Value': 'False',},],
                'FullSearch': None,
                'LongRanges': None,
            },
        ],
        'ZipCode': '',
        'miles': 0,
        'PageSize': int(chartva),
        'CurrentPage': 1,
        'Sort': [{
                'IsGeoSort': False,
                'SortField': 'AuctionDateTime',
                'IsDescending': False,},],
        'SaleStatusFilters': [{
                'SaleStatus': 1,
                'IsSelected': True,},],
        'BidStatusFilters': [{
                'BidStatus': 6,
                'IsSelected': True,},],
        }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ka-GE;q=0.8,ka;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.iaai.com',
        'pragma': 'no-cache',
        'referer': 'https://www.iaai.com/Search?url=9QryrXirfQoB59ajRHSfUDEGW9b2%2fRgV4NNkc4IoV%2fA%3d',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    response = requests.post('https://www.iaai.com/Search?c=1713107614260', headers=headers, json=json_data)
    soup = BeautifulSoup(response.content,features="html.parser")
    content = soup.find('div', class_='table-body border-l border-r').find_all('div', class_='table-row table-row-border')
    counter = soup.find('div', {'id':'TotalVehicleAmount'}).text
    if int(counter) > 0:
        print("მიმდინარე ფილტრით მოიძებნა "+str(counter)+" მონაცემი")
        for cnt in content:
            image_array = []
            array_for_more_info = []
            image = cnt.find('img', class_='img-responsive lazyload', attrs={'data-container':"body"})
            if 'https://vis.iaai.com/resizer?imageKeys' in image['data-src']:
                for a in range(1,10):
                    image_array.append(image['data-src'].replace('~I1&','~I'+str(a)+'&').replace('&width=400&height=300','&width=845&height=633'))
                name = cnt.find('h4', class_='heading-7 rtl-disabled')
                if name:
                    sorting = name.text.split()
                    if "land rover" in name.text.lower():
                        make = sorting[1]+""+sorting[2]
                    elif "alfa romeo" in name.text.lower():
                        make = sorting[1]+""+sorting[2]
                    else:
                        make = sorting[1]

                    if len(sorting) > 3 and make.lower() == "mercedes-benz":
                        if 'amg' in name.text.lower():
                            if str(sorting[2]).lower() == "amg": 
                                model = str(sorting[3])+""+str(sorting[4])+""+str(sorting[2])
                            else:
                                model = str(sorting[2])+""+str(sorting[3])+""+str(sorting[4])
                        elif '-class' in name.text.lower():
                            model = str(sorting[3])+""+str(sorting[4])
                        else:
                            model = str(sorting[2])+""+str(sorting[3])
                    elif len(sorting) > 3 and make.lower() == "tesla":
                        model = str(sorting[2])+""+str(sorting[3])
                    elif len(sorting) > 3 and make.lower() == "lexus":
                        model = str(sorting[2])+""+str(sorting[3])
                    elif len(sorting) > 3 and make.lower() == "landrover":
                        if 'range' in name.text.lower():
                            if "evoque" in name.text.lower() or "sport" in name.text.lower() or "velar" in name.text.lower():
                                model = str(sorting[3])+""+str(sorting[4])+""+str(sorting[5])
                            else:
                                model = str(sorting[3])+""+str(sorting[4])
                        elif 'discovery' in name.text.lower():
                            if "sport" in name.text.lower():
                                model = str(sorting[3])+""+str(sorting[4])+""+str(sorting[5])
                            else:
                                model = str(sorting[3])+""+str(sorting[4])
                        else:
                            model = str(sorting[3])
                    elif len(sorting) > 3 and make.lower() == "alfaromeo":
                        model = str(sorting[3])
                    else:
                        model = str(sorting[2])
                    year = sorting[0]
                m_info = cnt.find_all('li', class_='data-list__item')
                for mr_info in m_info:
                    if mr_info.find('span', class_='data-list__value'):
                        if mr_info.find('span', class_='data-list__value').has_attr('title'):
                            value_span_text = mr_info.find('span', class_='data-list__value').text
                            value_title = mr_info.find('span', class_='data-list__value')['title']
                            if  "Stock #: " in value_title:
                                id = value_span_text.strip()
                            if  "Odometer: " in value_title:
                                garbeni = str(int(int(''.join(filter(str.isdigit, value_span_text)))*1.609))
                            if  "Cylinder: " in value_title:
                                cilindri = value_span_text.strip().replace(" Cyl","")
                                elektro = ""
                            if  "Engine: " in value_title:
                                dzravi = value_span_text.strip()
                                dzravi = dzravi[:3].replace('.','')+"00"
                            if  "Fuel Type: Electric" in value_title:
                                dzravismodeli = "7" # ელექტრო
                                elektro = '4'
                                dzravi = '100'
                            elif "Fuel Type: Hybrid" in value_title:
                                dzravismodeli = "11" # ჰიბრიდი
                                elektro = ""
                            elif "Fuel Type: Gasoline" in value_title:
                                dzravismodeli = "2" # ბენზინი
                                elektro = ""
                            elif "Fuel Type: Diesel" in value_title:
                                dzravismodeli = "2" # ბენზინი
                                elektro = ""
                            elif "Fuel Type: Flexible Fuel" in value_title:
                                dzravismodeli = "2" # ბენზინი
                                elektro = ""
                            elif "Fuel Type: Other" in value_title:
                                dzravismodeli = "2" # ბენზინი
                                elektro = ""
                            if 'Driveline Type' in value_title:
                                if "rear" in value_title.lower(): wamyvani = "2" # უკანა
                                elif "4x4" in value_title.lower() or "4" in value_title.lower() or "all" in value_title.lower(): wamyvani = "3" #4იქს4
                                elif "front" in value_title.lower(): wamyvani = "1" # წინა
                                else: wamyvani = "2" # უკანა
                fotoebi = ",".join(map(str,image_array))
                if model[-1:].lower() == 'i':
                    model = model.lower().replace('i','')
                #print(str(make),str(model),str(year),str(dzravi),str(cilindri+""+elektro),str(garbeni),"I"+str(id)+"I",cart,dzravismodeli,wamyvani)
                posttomy(s,tokken,str(make),str(model),str(year),fotoebi,str(dzravi),str(cilindri+""+elektro),str(garbeni),"I"+str(id)+"I",cart,dzravismodeli,wamyvani)
    else:
        print("მიმდინარე ფილტრით მონაცემი არ მოიძებნა "+str(counter))
