##########################################################################
######################            НАЧАЛО            ######################
##########################################################################

import random
import time
from flask import Flask, render_template, url_for, request, redirect, make_response, abort # ФРЕЙМВОРК САЙТА
import requests
import subprocess
import threading

def keeponline():
    subprocess.run(['ssh',  '-R', 'offhost:80:localhost:80', 'serveo.net'])

key = random.randint(1000000, 9999999)

pc_list = [["1862-3inf-0", "Школьная доска Irbis", "Online", "green"],
		   ["1862-3inf-1", "Ученический компьютер #1", "Online", "green"],
		   ["1862-3inf-2", "Ученический компьютер #2", "Online", "green"],
		   ["1862-3inf-3", "Ученический компьютер #3", "Online", "green"],
		   ["1862-3inf-4", "Ученический компьютер #4", "Online", "green"],
		   ["1862-3inf-5", "Ученический компьютер #5", "Online", "green"],
		   ["1862-3inf-6", "Ученический компьютер #6", "Online", "green"],
		   ["1862-3inf-7", "Ученический компьютер #7", "Online", "green"],
		   ["1862-3inf-8", "Ученический компьютер #8", "Online", "green"],
		   ["1862-3inf-9", "Ученический компьютер #9", "Online", "green"],
		   ["1862-3inf-10", "Ученический компьютер #10", "Online", "green"],
		   ["1862-3inf-11", "Ученический компьютер #11", "Online", "green"],
		   ["1862-3inf-12", "Ученический компьютер #12", "Online", "green"],
		   ["1862-3inf-13", "Ученический компьютер #13", "Online", "green"],
		   ["1862-3inf-14", "Ученический компьютер #14", "Online", "green"],
		   ["1862-3inf-15", "Ученический компьютер #15", "Online", "green"],
		   ["1862-3inf-16", "Ученический компьютер #16", "Online", "green"],
		   ["yaktoro-mos12", "Абоба", "Online", "green"]]

app = Flask(__name__)



##########################################################################
######################            НАЧАЛО            ######################
##########################################################################



############################################################################
######################            СТРАНИЦЫ            ######################
############################################################################

@app.route('/')
def load():
	return render_template("loading.html")
	

@app.route('/dashboard', methods = ["GET"])
def index():
	template = "index.html"
	name = "OffHost Web"
	user = "user"
	if request.cookies.get('id') == "admin":
		name = key
	elif request.cookies.get('id') == "guest":
		user = "guest"
	elif request.cookies.get('id') != str(key):
		template = "not_acessed.html"
		return render_template(template, name = name, user = user)
	pc_list = new_pc_list()
	return render_template(template, pc_list=pc_list, name = name, user = user)
	

############################################################################
######################            СТРАНИЦЫ            ######################
############################################################################




#################################################################################
######################          Скрытые Страницы           ######################
#################################################################################

@app.route('/get_acess', methods = ["GET"])
def get_acess():
	code = request.args.get("code")
	res = make_response(redirect("/"))
	res.set_cookie('id', code)
	return res

@app.route('/get_admin_acess', methods = ["GET"])
def get_admin_acess():
	res = make_response(redirect("/"))
	res.set_cookie('id', "admin")
	return res

@app.route('/shutdown/<pc>', methods = ["GET"])
def shutdown(pc: str):
	print(pc)
	if pc == "all":
		for i in pc_list:
			requests.get(f"https://1862-3inf-{i[0]}.serveo.net/shutdown")
	else:
		requests.get(f"https://{pc}.serveo.net/shutdown")
	return redirect("/")
	
@app.route('/reboot/<pc>', methods = ["GET"])
def reboot(pc: str):
	if pc == "all":
		for i in pc_list:
			requests.get(f"https://{i[0]}.serveo.net/reboot")
	else:
		requests.get(f"https://{pc}.serveo.net/reboot")
	return redirect("/")
	


#################################################################################
######################          Скрытые Страницы           ######################
#################################################################################



##############################################################################
######################            ОБЛЕГЧЕНИЕ            ######################
##############################################################################

def new_pc_list():
	ans = pc_list
	for i in ans:
		a = requests.get(f"https://{i[0]}.serveo.net/ping")
		a = a.status_code
		print(a)
		if a == 200:
			i[2] = ("Online")
			i[3] = ("green")
		else:
			i[2] = ("Offline")
			i[3] = ("red")
		print(i)
	return ans

##############################################################################
######################            ОБЛЕГЧЕНИЕ            ######################
##############################################################################



#########################################################################
######################            КОНЕЦ            ######################
#########################################################################

internet = False
while not internet:
    try:
        # subprocess.check_call(['ping', '-c 1', 'www.google.ru'])
        print('Internet is up again!')
        internet = True
    except subprocess.CalledProcessError:
        print('no internet')



if __name__ == '__main__':
    t1 = threading.Thread(target=keeponline, daemon=True)
    # t1.start()

    app.run('localhost', 80)
 
#########################################################################
######################            КОНЕЦ            ######################
#########################################################################
