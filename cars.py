#./#/#/#. Coded By Giorgi Zirakashvili #./#/#/#.#
from ziraka import *


print(" ### CARS ძებნის ფილტრი ### ")

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
    mark = input("ბრენდი ")
    mark = mark.replace('-','_').replace(" ","_")
    model = input("მოდელი ")
    if model != "":model = mark.lower()+'-'+model.lower().replace(' ','_').replace('-','_')
    chartva = input("რამდენი განცხადება ჩატვირთოს Min:5,10,20,50,Max:100: ")
    if chartva == "": chartva = '100'
    if int(chartva) > 100:
        chartva = 100
    else:
        chartva = chartva

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ka-GE;q=0.8,ka;q=0.7',
        # 'cookie': 'CARS_als_loaded=true; CARS_has_visited=; CARS_logged_in=false; CARS_trip_id=ff417f4b-1b69-4c3a-97d3-460b98c9d4ce; CARS_navClick=; ak_bmsc=E3CD25E533C5B1221AD466893BF7D943~000000000000000000000000000000~YAAQovAQAp86N8yOAQAAV1yg1xf7pvdqUw4eq2uK2S8yN3K+O1x+B8h8pM/KdNfolbHhRRQXhuertmN7MNrjYlc7DlYvKoBcKQlX8IjBsfOPHIvifZSNyn7eUj9L9C9qV1Bhy3QXR0McA2Dn/FgxuR3OXYeGhg97LtEcZWdCvrQYyg7iDCYIBY+mMb4XwQO7E0A+x9Gik0GPF7WxLXJEiz6cVkkpB+AFlYFsI0VD6OXCccfcccl/556xL53v8yTihG8hDNxhD4rI9d+YWkvYlsWVHQ4FR10wmC+9uvcSXoX98OCVSi3IovPOssLD5SYJP9A7ZBGSx4wGynSLvzd5M2BOJH+MWmnJjOCV2nuiujSw/kAZcy11hCqkhI0Qiroi+lZ0+cvDpUzhtfSDySRGE1j9hPMdj67hUXX3azfpEKx6GooNeIUPPKbyE5D6LbbIuQ5c+6zn/aSQjGEELQ==; _cc_id=4da80e628a099dd6365a3a758b130a56; panoramaId_expiry=1713619399713; panoramaId=2442defbafd9ff32ee5c35a6bd2c185ca02c28c4a462b533574c0e2b765979e5; panoramaIdType=panoDevice; iovoxMCM=other; OptanonAlertBoxClosed=2024-04-13T13:38:35.675Z; iovox_sea=eyJmaXJzdF92aXNpdCI6IjIwMjQtMDQtMTNUMTM6NDI6MjEuMzQ1WiIsInJlZmVyZXJfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcnMuY29tL3Nob3BwaW5nL3Jlc3VsdHMvP2RlYWxlcl9pZD0ma2V5d29yZD0mbGlzdF9wcmljZV9tYXg9Jmxpc3RfcHJpY2VfbWluPSZtYWtlc1tdPW1lcmNlZGVzX2JlbnombWF4aW11bV9kaXN0YW5jZT1hbGwmbWlsZWFnZV9tYXg9Jm1vZGVsc1tdPW1lcmNlZGVzX2JlbnotYW1nX2VfNDMmbW9kZWxzW109bWVyY2VkZXNfYmVuei1hbWdfZV81MyZtb2RlbHNbXT1tZXJjZWRlc19iZW56LWFtZ19lXzYzJm1vZGVsc1tdPW1lcmNlZGVzX2JlbnotZV9jbGFzcyZtb250aGx5X3BheW1lbnQ9JnBhZ2U9MSZwYWdlX3NpemU9MTAwJnNvcnQ9YmVzdF9tYXRjaF9kZXNjJnN0b2NrX3R5cGU9YWxsJnllYXJfbWF4PTIwMjQmeWVhcl9taW49MjAxMyZ6aXA9IiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNhcnMuY29tL3ZlaGljbGVkZXRhaWwvOTE4NGMyODItZmQ2Yi00YTYyLWI3MWEtNTlkOGI0OTQzOGEzLyJ9; iovox_id=93e7c16a-eb9a-4f99-95c6-d425441e4544; __gads=ID=c704f273f9a2a4cc:T=1713014596:RT=1713016492:S=ALNI_MYj9tJ9ejga1u8ch63KUcgxEuFBzA; __gpi=UID=00000d5cfbd5e05c:T=1713014596:RT=1713016492:S=ALNI_MbQenI1DtM7HW-cO5YPDwjFX3KYUw; __eoi=ID=fe9be6d376ba3479:T=1713014596:RT=1713016492:S=AA-AfjZjKvi6CZd8feebWNBVXrUQ; CARS_search_session=SFMyNTY.g2gDdAAAAAZ3Cl9fc3RydWN0X193IUVsaXhpci5DYXJzV2ViLlBsdWcuU2VhcmNoU2Vzc2lvbncNc2VhcmNoX3JhZGl1c3cDbmlsdw1zZWFyY2hfcGFyYW1zdwNuaWx3DnNlYXJjaF96aXBjb2RldwNuaWx3EnNlYXJjaF9pbnN0YW5jZV9pZG0AAAAkZDBlNzI1NTEtMzkyMS00NDZjLWE0ZDktYzBlMGRmNmNmNGJldxJzZWFyY2hfbGlzdGluZ19pZHN3A25pbG4GAH5Av9eOAWIAAVGA.o50MVLSMo1u7HaSsrd2PFO59lJQl2Wt28jI1DSD8I1o; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+13+2024+17%3A55%3A55+GMT%2B0400+(Georgia+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4d3b040f-8ac6-4be7-a2ee-5af3113669a4&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false&geolocation=GE%3BTB; pageviewSessionCount=5; FCNEC=%5B%5B%22AKsRol96ypFqXdLc9N0bg-QJz08EpSki1lfRSSTESezSBrot-G1QqJ-YE4CeVJ3bOpW2dTC4NF0HMhMnzpm_6f1mM5Nt--pUrAXiHIn2d9ccP2q-EbS33kxgWS0sLohFq_Zqkk5j6BcduIvgSquQy-yWI5zGFMvP0A%3D%3D%22%5D%5D; _dd_s=rum=0&expire=1713017463791; CARS_marketing_source=SFMyNTY.g2gDdAAAAAR3Cl9fc3RydWN0X193I0VsaXhpci5DYXJzV2ViLlBsdWcuTWFya2V0aW5nU291cmNldwhhZmZfY29kZW0AAAAIbmF0aW9uYWx3DGNsaWNrX3NvdXJjZXQAAAAAdwN1dG10AAAAC3cKX19zdHJ1Y3RfX3clRWxpeGlyLkNhcnNXZWIuU2l0ZUFjdGl2aXR5LlVUTVBhcmFtc3cMdXRtX2NhbXBhaWdudwNuaWx3D3V0bV9jYW1wYWlnbl9pZHcDbmlsdwt1dG1fY29udGVudHcDbmlsdxV1dG1fZmlyc3Rfc2Vzc2lvbl9oaXR3A25pbHcKdXRtX21lZGl1bXcDbmlsdwx1dG1fbW9kaWZpZWR3A25pbHcOdXRtX3NldF9tZXRob2R3A25pbHcKdXRtX3NvdXJjZXcDbmlsdwh1dG1fdGVybXcDbmlsdwt1dG1fdHJ1c3RlZHcDbmlsbgYACWi_144BYgABUYA.BPUuLIkxQEKEpK0Edb6xV4jpKhdQ6om0NTjSZksCfkM; _cars_web_key=SFMyNTY.g3QAAAANbQAAAAxDQVJTX3RyaXBfaWRtAAAAJGZmNDE3ZjRiLTFiNjktNGMzYS05N2QzLTQ2MGI5OGM5ZDRjZW0AAAALX2NzcmZfdG9rZW5tAAAAGEQ2ZF9zbGZuUGwtTGNqWVdwUGx1SFktb20AAAAQYWxzX3ByaXZhdGVfZGF0YW0AAAC2UVRFeU9FZERUUS42TkFVaHFOcHc4SktnYUZGcTliOEU3NEJJQnpzN0wzcHVwTDZfUWl2WnJwblhFMXRvSWlUOWltMVlNRS5lbGp2YVREa1gwQlhDUF9oLkNJOExLN1NocmRjRXlYTTdDdmRGcnBKMkVCY1Fvb05na2NZRUlZOFM4UGhyMXpJRlhULTBRRDlxMkpQaEpwd2NITzFXYUVJLlFZZE1NeTIwbEgxeE5FQWNRSDRaREFtAAAACGJvdF90eXBldwNuaWxtAAAAEWZhY2Vib29rX2V2ZW50X2lkbQAAAFRkSEpwY0Y5cFpEMW1aalF4TjJZMFlpMHhZalk1TFRSak0yRXRPVGRrTXkwME5qQmlPVGhqT1dRMFkyVW1kSE05TVRjeE16QXhOall5T1RJMU53PT1tAAAAGGZhY2Vib29rX2V2ZW50X2ludGVudF9pZHcDbmlsbQAAAA9ncmFwaHFsX2FwaV9rZXltAAAAIDVycm1uV1ZsMU1EelBjRW5EdkVwM1B1MTAxSUdYRUdvbQAAAA1pc19zZWFyY2hfYm90dwVmYWxzZW0AAAAQbGFzdF92aWV3ZWRfcGFnZW0AAAASL3Nob3BwaW5nL3Jlc3VsdHMvbQAAAA5zZWFyY2hfemlwY29kZW0AAAAAbQAAABB0b3RhbF9wYWdlX3ZpZXdzYQZtAAAADXdlYl9wYWdlX3R5cGVtAAAAF3Nob3BwaW5nL3NlYXJjaC1yZXN1bHRzbQAAABJ3ZWJfcGFnZV90eXBlX2Zyb21tAAAACGhvbWVwYWdl.Ip0Ck0XLmeRQFUR-37L22SMNA8NJHS-nfR3oYjWO3Sw; _abck=4257A692AEA0BE6C016CFBED4044C76F~0~YAAQovAQApl2OMyOAQAARWi/1wvjmAJXD+g7gKz+JJibXTou3gj3edw7eEEEC76xSvmpvHepVGYDTir+TKZAoErw0JVGGqC/AHz/KBx8Zi6Z4cAarTIjeaEDAk1cZrI/MMYbGxzjJ3z+umNIxNZFVPqag32qcbA2kcisFu6uXFroNs+YEvilwZQan0H47MpH/js1ZGJWkXvsYHEe0x5b6oCQ0UEMtK4dTFRZWoDFX+/4KkCpkB2kEDi1qK9jTxYrfxcpFedYjdGpGFkJqly6HM1GXk4wO5wcZo22XfcC//WsELG4bgMgkVocdFa7VttyfhQPgm6Bfx5r6odyrUuN95ZNmUGjSal3ny1Sis+w9v/0OqrEeAXRK/l7M/SByEq9VYNa5fDmklLY8z6lj56hFr+Vos6HGg==~-1~-1~-1; bm_sv=C3EEF5039184336165D75E8AD4B7F280~YAAQovAQApp2OMyOAQAARWi/1xf6lBDkHxm0x1qTiuabXus8IK1IWBuDcJfjoCuIUokXSbv4R1Jw6LBx7XTleNEplodVi4S0bvuddDIDKoreionpjuI+WykgJbyxyhWXuhwMTFrG5AWug0ioeF/2ejhGvWfLxx5ECZ1KKsRROtiQDrnMCh7WsctC9hgWMmioe5bUFSzMGEA/Y8HqgN2mj3rmNKvU3tSJcE9OzPVe9tzMVm+9vUVZlgZp0Sy02w==~1; bm_sz=2E38BAA08BCAA824D2E2342926CB4763~YAAQovAQApt2OMyOAQAARWi/1xeLByCyPb2D7g3jka+P6R0M+66cwQaO7+usnI05APwoOxTUjqi95OKh0WtZ2rRzaGqxgDENmlTALIcAX7CHVf5PSALvse7qjStIKERkRpYCXawZpHNeqWmUiV0C7d2P4WaEfDqLg0+69xfd6cu+5BVzaL3iiccxBhzMoUFll9oCvEW+B3uIjlrWXklycPix3U4dZZB/DtkprDFuulWyyHrUUOS/rpRepuSPacE7jenr6jccQ+K1nA6j0T4cVmECcBYjTNoAa3EIlRGu9VoT3CaeG8bIx2EjXSWF/HmX7YJ4hQlQ00fGDHDopf296njpoRx7PXBPkLliCe306K6QO1pHmX0NLIuaexJMP7L/SSoVXngi+TrHlrnO4CZUNO17SNtrs1A42wnJywbOI9qlgvYFE9yAgESuA1uef/4u3X9sMOQeAmGXFjc3~3750192~3290182',
        'referer': 'https://www.cars.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    url = 'https://www.cars.com/shopping/results/?makes[]='+mark+'&maximum_distance=all&models%5B%5D='+model+'&stock_type=all&page_size='+chartva+'&year_max='+year2+'&year_min='+year1+'&only_with_photos=true&mileage_max=100000&zip='
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,features="html.parser")
    counter = soup.find('span', class_="total-filter-count").text.replace(" matches","").strip().replace(',','')
    if int(counter.replace('+','')) > 0:
        print("მიმდინარე ფილტრით მოიძებნა "+str(counter)+" მონაცემი")
        containter = soup.find('div', class_='vehicle-cards', attrs={'id':'vehicle-cards-container'})
        lists = containter.find_all('div', class_='vehicle-card ep-theme-hubcap')
        for list in lists:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,ka-GE;q=0.8,ka;q=0.7',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'referer': 'https://www.cars.com/shopping/results/?makes[]=mercedes_benz&maximum_distance=all&stock_type=all&zip=',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            }
            response = requests.get('https://www.cars.com/vehicledetail/'+str(list['data-listing-id'])+'/',headers=headers,)
            soup = BeautifulSoup(response.content,features="html.parser")
            sect = soup.find('section', class_='listing-overview')
            if sect.find('gallery-thumbnails'):
                name1 = sect.find('h1', class_='listing-title').text
                title = name1.split()
                try:
                    garbeni = sect.find('div', class_='listing-mileage').text.split()[0].replace(',','')
                except:
                    garbeni = 1
                year = title[0]

                # alfa romeo Name correction
                if "alfa romeo" in name1.lower() or "land rover" in name1.lower():
                    mark = title[1]+""+title[2]
                else:
                    mark = title[1]


                #mercedes-benz
                if mark.lower() == 'mercedes-benz':
                    if len(title) > 4:
                        if 'amg' in name1.lower():
                            model = title[3]+""+title[4]+"AMG"
                        elif '-class' in name1.lower():
                            model = title[3]+""+title[4]
                    else:
                        model = title[2]+""+title[3]
                #lexus 
                elif mark.lower() == 'lexus':
                    if title[3][-1:].lower() == 't' or title[3][-1:].lower() == 'h' or title[3][-1:].lower() == 'c':
                        model = str(title[2])+""+str(title[3]).replace("h",'').replace("t",'').replace("c",'')
                #bmw
                elif mark.lower() == 'bmw':
                    if len(title) > 3:
                        if title[3][-1:].lower() == 'd' or title[3][-1:].lower() == 'i' or title[3][-1:].lower() == 'e' or title[3][-6:].lower() == 'edrive':
                            model = str(title[2]).lower().replace("d",'').replace("i",'').replace("e",'').replace("edrive",'')
                    if model[:4].lower() == 'bmw-':
                        model = model.lower().replace("bmw-","").replace('_','')
                #tesla
                elif mark.lower() == 'tesla':
                    model = title[2]+""+title[3]
                #alfa romeo
                elif "alfa romeo" in name1.lower():
                    model = title[3]
                #land rover
                elif "land rover" in name1.lower():
                    if 'range' in name1.lower():
                        if "evoque" in name1.lower() or "sport" in name1.lower() or "velar" in name1.lower():
                            model = str(title[3])+""+str(title[4])+""+str(title[5])
                        else:
                            model = str(title[3])+""+str(title[4])
                    elif 'discovery' in name1.lower():
                        if "sport" in name1.lower():
                            model = str(title[3])+""+str(title[4])+""+str(title[5])
                        else:
                            model = str(title[3])+""+str(title[4])
                    else:
                        model = str(title[3])
                #defaults
                else:
                    model = title[2]

                garbeni = int(int(garbeni)*1.609)
                a = soup.find('dl', class_='fancy-description-list')
                b = a.find_all('dd') 
                #dzravi,cilindri
                if len(b) > 8:
                    info = b[6].text.split()
                    dzravi = info[0].replace('.','').replace('L','').ljust(4,'0')
                    if len(info) > 4:
                        cilindri = info[1].replace("I","").replace("V","").replace("-","")
                    else:
                        cilindri = '4'
                else:
                    cilindri = '4'
                    dzravi = '100'
                #wamyvani
                if "rear" in b[2].text.lower(): wamyvani = "2" # უკანა
                elif "4x4" in b[2].text.lower() or "4" in b[2].text.lower() or "all" in b[2].text.lower(): wamyvani = "3" #4იქს4
                elif "front" in b[2].text.lower(): wamyvani = "1" # წინა
                else: wamyvani = "2" # უკანა
                #dzravistype
                if "hybrid" in b[4].text.lower() or "hy" in b[4].text.lower(): # fuelType
                    dzravismodeli = "11" # ჰიბრიდი
                elif "electric" in b[4].text.lower() or "el" in b[4].text.lower():
                    dzravismodeli = "7" # ელექტრო
                else: 
                    dzravismodeli = "2" # ბენზინი

                fotoebi = []
                photo_section = sect.find('gallery-thumbnails')
                massivi = photo_section.find_all('img')
                raodenoba = 0
                for a in massivi:
                    if raodenoba < 10:
                        fotoebi.append(a['src'].replace('.com/small/in', '.com/xlarge/in'))
                        raodenoba = raodenoba+1
                fotoebi = ",".join(map(str,fotoebi))
                #print(str(mark),str(model.strip()),str(year),str(dzravi),str(cilindri),str(garbeni),str(list['data-listing-id']),cart,dzravismodeli,wamyvani)
                posttomy(s,tokken,str(mark),str(model.strip()),str(year),fotoebi,str(dzravi),str(cilindri),str(garbeni),str(list['data-listing-id']),cart,dzravismodeli,wamyvani)
    else:
        print("მიმდინარე ფილტრით მონაცემი არ მოიძებნა "+str(counter))

