#./#/#/#. Coded By Giorgi Zirakashvili #./#/#/#.#
from ziraka import *

print(" ### COPART ძებნის ფილტრი ### ")

today = date.today()

if today.weekday() == 4:
    end_date1 = (date.today() + timedelta(days=3)).strftime("%Y%m%d")
    end_date2 = (date.today() + timedelta(days=4)).strftime("%Y%m%d")
    end_date3 = (date.today() + timedelta(days=5)).strftime("%Y%m%d")
elif today.weekday() == 3:
    end_date1 = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
    end_date2 = (date.today() + timedelta(days=4)).strftime("%Y%m%d")
    end_date3 = (date.today() + timedelta(days=5)).strftime("%Y%m%d")
elif today.weekday() == 2:
    end_date1 = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
    end_date2 = (date.today() + timedelta(days=2)).strftime("%Y%m%d")
    end_date3 = (date.today() + timedelta(days=5)).strftime("%Y%m%d")
else:
    end_date1 = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
    end_date2 = (date.today() + timedelta(days=2)).strftime("%Y%m%d")
    end_date3 = (date.today() + timedelta(days=3)).strftime("%Y%m%d")

def Fetch_photo_api(link):
    data_image = ""
    try:
        response = requests.get(link)
        response = response.json()
        for a in response['lotImages']:
            for b in a['link']:
                if b['isHdImage'] == True:
                    if a['sequence'] == 5:
                        data_image = b['url'].strip()+","+data_image
                    else:
                        data_image = data_image+""+b['url'].strip()+","

        return data_image
    except:
        print("განცხადება "+link+" გამოტოვა (გაიყიდა/წაიშალა)")
        return False
    
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

    i = 1
    with open('copart_salesdata/salesdata.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            row[23] = row[23].replace(".0","").replace(".","")
            if (mark.lower().strip() == "lexus" and mark.lower().strip() == row[11].lower().strip() and model.lower().strip().replace(" ","") in row[12].lower().strip().replace(" ","") or mark.lower().strip() == row[11].lower().strip() and model.lower().strip().replace(" ","") == row[12].lower().strip().replace(" ","")) and int(row[10].strip()) >= int(year1) and int(row[10].strip()) <= int(year2)and int(row[23].strip()) >= int(odo1) and int(row[23].strip()) <= int(odo2):
                if str(end_date1) == str(row[3]) or str(end_date2) == str(row[3]) or str(end_date3) == str(row[3]) or "0" == str(row[3]):
                    if i <= int(chartva):
                        
                        if "rear" in row[28].lower(): wamyvani = "2" # უკანა
                        elif "4x4" in row[28].lower() or "4" in row[28].lower() or "all" in row[28].lower(): wamyvani = "3" #4იქს4
                        elif "front" in row[28].lower(): wamyvani = "1" # წინა
                        else: wamyvani = "2" # უკანა

                        if "hybrid" in row[30].lower() or "hy" in row[30].lower(): # fuelType
                            dzravismodeli = "11" # ჰიბრიდი
                            dzravi = row[27].split()[0].strip().replace(".","").replace("L","")+"00"
                            cilindri = row[27].split()[1].strip()
                        elif "electric" in row[30].lower() or "el" in row[30].lower():
                            dzravismodeli = "7" # ელექტრო
                            dzravi = '100'
                            cilindri = '4'
                        else: 
                            dzravismodeli = "2" # ბენზინი
                            dzravi = row[27].split()[0].strip().replace(".","").replace("L","")+"00"
                            cilindri = row[27].split()[1].strip()
                        #bmw
                        if "series" in row[12].lower():
                            row[12] = row[13][:3]
                        #mercedes
                        if "mercedes" in row[11].lower():
                            row[12] = row[13]
                            if "amg" in row[13].lower():
                                row[12] = row[13].replace("AMG-S","AMG")
                            row[12] = row[12].strip().replace("4MAT","").replace("4MA","").replace("BLU","").replace('4M','').replace(" I","")
                        #lexus
                        if "lexus" in row[11].lower():
                            row[12] = row[13].strip().replace("PRE","").replace("BAS","").replace("BA","").replace("0H","0").replace("H","").replace("F","")

                        row[23] = str(int(int(row[23])*1.609))

                        if Fetch_photo_api(row[46]):
                            #print("განცხ ID "+row[8],"ბრენდი "+row[11],"მოდელი "+row[12],"წელი "+row[10],"გარბენი"+row[23],"ძრავი "+dzravi,"ცილინდრები "+cilindri,"წამყვანი "+wamyvani,"ძრავის მოდელი "+dzravismodeli)
                            i = i+1
                            posttomy(s,tokken,str(row[11].lower().strip().replace(" ","")),str(row[12].lower().strip().replace(" ","")),str(row[10]),Fetch_photo_api(row[46]),dzravi,cilindri,row[23],"C"+str(row[8])+"T",cart,dzravismodeli,wamyvani)
