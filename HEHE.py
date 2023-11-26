import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m  ▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄   ▄▄   ▄▄▄ 
\x1b[1;92m █   █ █     █ █       █ █      █ █  █ █  █ █   █
\x1b[1;97m █   █ █     █ █   ▄   █ █   ▄▄▄█ █  █▄█  █ █   █        
\x1b[1;93m █   █  █   █  █  █▄█  █ █   █    █       █ █   █     
\x1b[1;96m █   █  █   █  █       █ █   █    █   ▄   █ █   █     
\x1b[1;94m █   █  █   █  █   ▄   █ █   █▄▄▄ █  █ █  █ █   █       
\x1b[1;93m █▄▄▄█  █▄▄▄█  █▄▄█ █▄▄█ █▄▄▄▄▄▄█ █▄▄█ █▄▄█ █▄▄▄█        
\x1b[1;92m               ITACHI BRO
\x1b[1;92m-----------------------------------------------
\x1b[1;92m Owner  : ITACHI UCHIHA
\x1b[1;92m Github : https://github.com/Savage-Army
\x1b[1;92m Facebok: facebook.com/100071825551845
\x1b[1;92m Tool   : FACEBOOK CLONING
\x1b[0;92m-----------------------------------------------"""
boy = ['Rayhan Mahmud', 'Shakib Khan', 'Tamim Iqbal', 'Mushfiqur Rahim', 'Mahmudullah Riyad', 'Anamul Haque', 'Nurul Hasan', 'Mehidy Hasan Miraz', 'Mohammad Saifuddin', 'Litton Das', 'Mustafizur Rahman', 'Rubel Hossain', 'Taskin Ahmed', 'Abdur Razzak', 'Al Amin Hossain', 'Sabbir Rahman', 'Taijul Islam', 'Shohidul Islam', 'Enamul Haque Bijoy', 'Nazmul Islam Apu', 'Nasiruddin Chowdhury', 'Mohammad Ashraful', 'Raqibul Hasan', 'Nazimuddin Chowdhury', 'Mashrafe Mortaza', 'Zakir Hossain', 'Alok Kapali', 'Nazmul Abedin', 'Subashis Roy', 'Shamim Rahman', 'Khaled Ahmed', 'Shafiul Islam', 'Anamul Islam', 'Mosharraf Hossain', 'Arafat Sunny', 'Mahmudul Hasan Joy', 'Shadman Islam', 'Subhajit Roy', 'Shariful Islam', 'Ariful Haque', 'Mohammad Nazmul Islam', 'Kamrul Islam Rabbi', 'Abdur Rahman', 'Saikat Islam', 'Delwar Hossain', 'Muktar Hossain', 'Nafis Iqbal', 'Shahadat Hossain', 'Mohammad Shahid', 'Mohammad Shariful Islam', 'Asif Ahmed', 'Imran Khan', 'Sohag Gazi', 'Shahriar Nafees', 'Mohammad Mithun', 'Abdur Razzaq', 'Mohammad Abdullah', 'Mohammad Arafat Sunny', 'Aftab Ahmed', 'Nurul Islam', 'Mohammad Al Amin', 'Mohammad Shahidul Islam', 'Mohammad Nurul Islam', 'Mohammad Saiful Islam', 'Mohammad Ebadot Hossain', 'Mohammad Nahidul Islam', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Subhajit Roy', 'Mohammad Shariful Islam', 'Mashrafe Bin Mortaza', 'Mohammad Shariful Islam', 'Mohammad Al Amin Hossain', 'Mohammad Saifuddin', 'Mohammad Arafat Sunny', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Shariful Islam', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque', 'Mohammad Al Amin Hossain', 'Mohammad Nurul Islam', 'Mohammad Abdullah', 'Mohammad Al Amin Hossain', 'Mohammad Mosharraf Hossain', 'Mohammad Ariful Haque']
girl = ['Aafrin Sultana', 'Aamina Khatun', 'Aamina Rahman', 'Aamina Yasmin', 'Aasma Afrin', 'Aasma Khatun', 'Aasma Rahman', 'Aasma Yasmin', 'Aasiya Afrin', 'Aasiya Khatun', 'Aasiya Rahman', 'Aasiya Yasmin', 'Aayesha Afrin', 'Aayesha Khatun', 'Aayesha Rahman', 'Aayesha Yasmin', 'Abeda Afrin', 'Abeda Khatun', 'Abeda Rahman', 'Abeda Yasmin', 'Abira Afrin', 'Abira Khatun', 'Abira Rahman', 'Abira Yasmin', 'Abida Afrin', 'Abida Khatun', 'Abida Rahman', 'Abida Yasmin', 'Abirti Afrin', 'Abirti Khatun', 'Abirti Rahman', 'Abirti Yasmin', 'Afsana Afrin', 'Afsana Khatun', 'Afsana Rahman', 'Afsana Yasmin', 'Afrin Sultana', 'Afrin Akter', 'Afrin Begum', 'Afrin Khan', 'Afrin Khatun', 'Afrin Rahman', 'Afrin Roy', 'Afrin Yasmin', 'Afroza Afrin', 'Afroza Akter', 'Afroza Begum', 'Afroza Khan', 'Afroza Khatun', 'Afroza Rahman', 'Afroza Roy', 'Afroza Yasmin', 'Aisha Afrin', 'Aisha Akter', 'Aisha Begum', 'Aisha Khan', 'Aisha Khatun', 'Aisha Rahman', 'Aisha Roy', 'Aisha Yasmin', 'Ajanta Afrin', 'Ajanta Akter', 'Ajanta Begum', 'Ajanta Khan', 'Ajanta Khatun', 'Ajanta Rahman', 'Ajanta Roy', 'Ajanta Yasmin', 'Akhala Afrin', 'Akhala Akter', 'Akhala Begum', 'Akhala Khan', 'Akhala Khatun', 'Akhala Rahman', 'Akhala Roy', 'Akhala Yasmin', 'Aklima Afrin', 'Aklima Akter', 'Aklima Begum', 'Aklima Khan', 'Aklima Khatun', 'Aklima Rahman', 'Aklima Roy', 'Aklima Yasmin', 'Alama Afrin', 'Alama Akter', 'Alama Begum', 'Alama Khan', 'Alama Khatun', 'Alama Rahman', 'Alama Roy', 'Alama Yasmin', 'Alefia Afrin', 'Alefia Akter', 'Alefia Begum', 'Alefia Khan', 'Alefia Khatun', 'Alefia Rahman', 'Alefia Roy', 'Alefia Yasmin', 'Alesha Afrin', 'Alesha Akter', 'Alesha Begum', 'Alesha Khan', 'Alesha Khatun', 'Alesha Rahman', 'Alesha Roy', 'Alesha Yasmin', 'Alifa Afrin', 'Alifa Akter', 'Alifa Begum', 'Alifa Khan', 'Alifa Khatun', 'Alifa Rahman', 'Alifa Roy', 'Alifa Yasmin', 'Alina Afrin', 'Alina Akter', 'Alina Begum', 'Alina Khan', 'Alina Khatun', 'Alina Rahman', 'Alina Roy', 'Alina Yasmin', 'Amina Afrin', 'Amina Akter', 'Amina Begum', 'Amina Khan', 'Amina Khatun', 'Amina Rahman', 'Amina Roy', 'Amina Yasmin', 'Ana Afrin', 'Ana Akter', 'Ana Begum', 'Ana Khan', 'Ana Khatun', 'Ana Rahman', 'Ana Roy', 'Ana Yasmin', 'Ananya Afrin', 'Ananya Akter', 'Ananya Begum', 'Ananya Khan', 'Ananya Khatun', 'Ananya Rahman', 'Ananya Roy', 'Ananya Yasmin', 'Anjali Afrin', 'Anjali Akter', 'Anjali Begum', 'Anjali Khan', 'Anjali Khatun', 'Anjali Rahman', 'Anjali Roy', 'Anjali Yasmin', 'Anjum Afrin', 'Anjum Akter', 'Anjum Begum', 'Anjum Khan', 'Anjum Khatun', 'Anjum Rahman', 'Anjum Roy', 'Anjum Yasmin', 'Anna Afrin', 'Anna Akter', 'Anna Begum', 'Anna Khan', 'Anna Khatun', 'Anna Rahman', 'Anna Roy', 'Anna Yasmin', 'Anoushka Afrin', 'Anoushka Akter', 'Anoushka Begum', 'Anoushka Khan', 'Anoushka Khatun', 'Anoushka Rahman']
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('[1]FB Clone')
    print ('[2]Join Facebok ')
    print ('[3]Follow Instagram ')
    print ('[4]Join Messenger GC ')
    print (47*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100071825551845')
    elif sel in ['3', '03']:
        os.system('xdg-open https://www.instagram.com/ignored_cosmos/')
    elif sel in ['4', '04']:
        os.system('xdg-open https://m.me/j/Aba_8T7-5pQWi_lY/')
        menu()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] Boys name ids')
        print ('[2] girls name ids')
        print (47*'-')
        gen = input('select: ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example 1000, 2000, 5000, 10000')
        lim = int(input('limit: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
        }
        OO = '\033[0;94m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[Creat-fb] {OO}{self.loop}/{str(lim)} OK:{len(ok)} - CP:{len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;95m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;95m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m[OK] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (47*'-')
        print ('\033[1;32mTotal ids > Ok/' +str(len(ok)) + ' CP/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()

