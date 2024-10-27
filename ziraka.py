import requests, time, json, sys, csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta, date

mail = 'levan.beruashvili7@gmail.com'
tpass = 'GL2023..'
nomeri_tele = '599045490' #ნომერი რომელიც საიტზეა მითითებული
text_shablon = ''' 
Для русского прокрутите вниз / For English scroll down

✅ ლევანი
✅ ტელ : 599 04 54 90
სამუშაო საათები 24/7


შეიძინეთ ავტომობილი "GL BUSINESS ჯგუფში "_ში დამატებით მიიღეთ თქვენი ავტომობილისთვის ყველა საჭირო მომსახურება
ჩვენი მაღალტექნოლოგიური ევროპული სტანდარტების მქონე სერივს ცენტრში...

✅ გთავაზობთ მსუბუქი ავტომობილების , მოტოციკლების , სასოფლო-სამეურნეო და სამშენებლო ტექნიკის შეძენას ( ა.შ.შ ;
იაპონია ; გერმანია ; კანადა ; დუბაი ) უზრუნველვყობთ ტექნიკურ შემოწმებას , უსაფრთხო ტრანსპორტირებას და დაზღვევას .

✅ იხილეთ ყველა განცხადება .........

✅ Mob/Viber/WhatsApp : +995 599 04 54 90

✅ გაყიდვების მენეჯერი: ლევანი

✅ მისამართი: ქავთარაძის #40

-------------------------------------------------------------------------------------------------------------------------------------------------------------


✅ Часы работы 24/7


 Автомобиль осматривается на месте опытными Дилерами.

Купите машину в «GL BUSINESS GROUP» _ дополнительно получите все необходимые услуги для вашего автомобиля в Наш высокотехнологичный серийный центр с европейским стандартам ...


GL BUSINESS GROUP предлагает покупку автомобилей, мотоциклов, сельскохозяйственной и строительной техники (др .;
Япония; Германия; Канада; Дубай) Обеспечиваем технический осмотр, безопасную транспортировку и страхование.

✅ Просмотреть все объявления .........

✅ Моб / Viber / WhatsApp: + 995 599 04 54 90


Адрес: ул. Кавтарадзе №40


-------------------------------------------------------------------------------------------------------------------------------------------------------------


✅ Working hours 24/7


 The vehicle is inspected on the spot by experienced auto dealers.

Buy a car in "GL BUSINESS GROUP" _ additionally get all the necessary services for your car in
Our high-tech European standards serial center ..

GL BUSINESS GROUP offers the purchase of cars, motorcycles, agricultural and construction equipment and (etc .;
Japan; Germany; Canada; Dubai) We provide technical inspection, safe transportation, and insurance.

See all ads .........

Mob / Viber / WhatsApp: + 995 599 04 54 90

Sales Manager: LEVANI

Address: Kavtaradze str. N40
'''

def checkk_model(car):
    with open('data_myauto_indexeddb.json', 'r', encoding='utf8') as file:
        dat = json.load(file)
        dat = dat['store'][0]['record']['data']['data']['mans']
        for a in dat:
            if a['isCar'] == True and a['title'].strip().lower() == car.strip().lower():
                return a['id']


def checkk_cat(model, manid, dzravi):
    with open('data_myauto_indexeddb.json', 'r', encoding='utf8') as file:
        dat = json.load(file)
        dat = dat['store'][0]['record']['data']['data']['models']
        for a in dat:
            if a['manId'] == int(manid):
                if a['isCar'] == True and model.lower().strip().replace(" ","").replace(" ","") == a['title'].lower():
                    return a['id']
                elif a['isCar'] == True and a['title'].lower() == model.lower().strip().replace(" ","").replace(" ",""):
                    return a['id']
            
def posttomy(s,tokken,brendi,modeli,weli,fotoebi,dzravi,cilindri,garbeni,idto,jipi,fueltypeid,wamyvanisid):
    gancx = idto
    try:
        if checkk_cat(modeli, checkk_model(brendi), dzravi):
            idto = "\r\n\r\n"+idto
            headers = {
            'accept': '*/*',    
            'accept-language': 'ka',
            'authtoken': tokken,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.myauto.ge',
            'pragma': 'no-cache',
            'referer': 'https://www.myauto.ge/',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            }

            json_data = {
                'type': 'car',
                'vehicle_type': 0,  # მსუბუქი > 0 მძიმეტექნიკა > 1 მოტო > 2
                'currency_id': 3, 
                'category_id': int(jipi), # სედანი > 1 ჯიპი > 5 უნივერსალი > 3
                'man_id': int(checkk_model(brendi)),
                'model_id': int(checkk_cat(modeli, checkk_model(brendi), dzravi)),
                'car_model': '',
                'prod_year': weli, # gamoshvebis weli
                'car_run': int(garbeni),
                'car_run_dim': 6,
                'engine_volume': dzravi,
                'cylinders': cilindri,
                'gear_type_id': '3',
                'fuel_type_id': fueltypeid,
                'color_id': 16,
                'door_type_id': 2,
                'drive_type_id': wamyvanisid,
                'price': '',
                'fb_share': 1,
                'first_deposit': '',
                'customs_passed': None,
                'has_catalyst': 0,
                'client_name': 'ლევანი',
                'client_phone': nomeri_tele,
                'phone_num': nomeri_tele,
                'codeId': 'undefined',
                'area_code': 500,
                'saloon_color_id': 16,
                'airbags': 12,
                'fuel_consumption_city': 0,
                'fuel_consumption_highway': 0,
                'fuel_consumption_combined': 0,
                'vin': '',
                'video_url': '',
                'car_desc_4': text_shablon+''+idto,
                'car_desc_1': text_shablon+''+idto,
                'car_desc_5': text_shablon+''+idto,
                'for_rent': False,
                'rent_daily': '0',
                'rent_purchase': '0',
                'rent_insured': '0',
                'rent_driver': '0',
                'right_wheel': 0,
                'has_turbo': 0,
                'location_id': 21,
                'tech_inspection': None,
                'license_number': '',
                'agreeInspectTerms': 'NaN',
                'inspected_in_greenway': 0,
                'PromBlockAutoUpdateQuantity': 0,
                'PromBlockColorQuantity': 0,
                'PromBlockVipQuantity': 0,
                'PromBlockAutoUpdateHour': 0,
                'PromBlockOrderValue': 0,
                'PromBlockColor': 0,
                'PromBlockAutoUpdate': 0,
                'PromBlockStickers': 0,
                'images': '"'+fotoebi+'"', #
                'saloon_material': 1,
                'comfort_features': [13,15,26,36,39,41,43,45,6,44,11,20,12,23,30,31,7,38,8,28,9,10,],
                'auction': False,
                'auction_end_dt_month': None,
                'period_in_days': 30,
                'change': False,
                'PayWithCard': 0,
            }
            print("ატვირთვა დაიწყო "+str(gancx))
            postresp = requests.post('https://api2.myauto.ge/ka/user/addProduct', headers=headers, json=json_data)
            postresp = postresp.json()
            if postresp['statusCode'] == 1:
                print(postresp['statusMessage'])
            else:
                print(postresp+" "+str(gancx))
                sys.exit()
        else:
            print("მოდელი ვერ მოიძებნა "+str(gancx))
            pass
    except:
        print("განცხადება გამოტოვილია "+str(gancx))
        pass

def authenticate(s):
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ka-GE;q=0.8,ka;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://auth.tnet.ge',
        'referer': 'https://auth.tnet.ge/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    data = {
        'Email': mail,
        'Password': tpass,
        'FormToken': 'f3c02d53829ec0ec697667def327d21498f628ec67fdf995b72b30f46b0df2c7',
        'Continue': 'https://www.myauto.ge/ka',
    }
    try:
        response = s.post('https://accounts.tnet.ge/api/ka/user/auth', headers=headers, data=data)
        response = response.json()
        if response['success'] == True:
            print("ავტორიზაცია წარმატებულია")
            jjson = response['data']
            tokken = jjson["access_token"]
            print("მოგესალმებით "+jjson['Data']['username'])
            return tokken
    except:
        print("ავტორიზაცია ვერ მოხერხდა")
        sys.exit()
