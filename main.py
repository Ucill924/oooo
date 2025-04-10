_A='https://airdrop.firachain.com/'
import requests,time,random
from itertools import cycle
API_KEY='c4fc4f6195d0fae6db07f5389b1e91d9'
URL='https://airdrop.firachain.com/register.php'
SITEKEY='6LeuQAorAAAAAF3vZY-BS4WSnl_5lIXFFhw9AUtV'
PAGE_URL=_A
def get_captcha(api_key):
	G='request';F='status';E='json';D='key';B=api_key;print('  [+] Menunggu Bypass Chapca')
	try:
		A=requests.get('http://2captcha.com/in.php',params={D:B,'method':'userrecaptcha','googlekey':SITEKEY,'pageurl':PAGE_URL,E:1}).json()
		if A[F]!=1:print('  [!] Gagal minta captcha:',A);return
		H=A[G]
		for J in range(20):
			time.sleep(5);C=requests.get('http://2captcha.com/res.php',params={D:B,'action':'get','id':H,E:1}).json()
			if C[F]==1:print('  [+] Bypass Captcha berhasil!');return C[G]
			print('  [~] Menunggu captcha...')
		print('  [!] Timeout captcha');return
	except Exception as I:print('  [!] Error captcha:',I);return
def register(email,wallet,proxy):
	F='    Response:';D=proxy;C=wallet;A=email;E=get_captcha(API_KEY)
	if not E:print('  [!] Skip karena captcha gagal.');return
	G={'accept':'*/*','content-type':'application/json','referer':_A};H={'email':A,'wallet':C,'recaptcha':E};I={'http':D,'https':D}
	try:
		B=requests.post(URL,json=H,headers=G,proxies=I,timeout=30)
		if B.status_code==200:print(f"[+] Sukses daftar: {A} -> {C}");print(F,B.text)
		else:print(f"[!] Gagal daftar ({B.status_code}) => {A}");print(F,B.text)
	except Exception as J:print(f"[!] Error saat daftar {A} => {J}")
if __name__=='__main__':
	try:
		emails=open('email.txt').read().splitlines();wallets=open('wallet.txt').read().splitlines();proxies=open('proxy.txt').read().splitlines();proxy_pool=cycle(proxies)
		for(email,wallet)in zip(emails,wallets):proxy=f"http://{next(proxy_pool).strip()}";print(f"\n[=] Proses: {email} | {wallet} | Proxy: {proxy}");register(email,wallet,proxy);time.sleep(random.randint(3,6))
	except FileNotFoundError as e:print(f"[!] File tidak ditemukan: {e.filename}")
	except Exception as e:print(f"[!] Terjadi error: {e}")
