# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import wget
import os

firefox = webdriver.Firefox()

firefox.get('https://www.urionlinejudge.com.br/judge/pt/runs')

firefox.find_element_by_class_name('send-github').click()

username = firefox.find_element_by_id('login_field')
pwd = firefox.find_element_by_id('password')

u = raw_input("Username: ")
p = getpass.getpass('Password: ')

print("Realizando login...")

username.send_keys(u)
pwd.send_keys(p)

pwd.send_keys(Keys.ENTER)
print("done.")
time.sleep(7)
print(firefox.current_url)

#selecionando os problemas aceitos
print("Selecionando os codigos aceitos...")
firefox.find_element_by_xpath("//select[@name='answer_id']/option[text()='Accepted']").click()
firefox.find_element_by_class_name('send-red').click()
print("done.")

qnt = firefox.find_element_by_id('table-info')
limite = firefox.find_element_by_id('table-info').text
limite = limite[limite.rindex(" "):].replace(" ","")

print("Abrindo links...")
p = []
links = []
time.sleep(3)

print("Coletando urls dos problemas...")
#loop para percorrer os problemas aceitos e guardar as url's que conterão as url's de download
for pagina in range(int(limite)-1):
    p = firefox.find_elements_by_class_name('semi-wide')
    #time.sleep(3)
    for i in p:
        link = i.find_element_by_link_text("Accepted").get_attribute("href")
        links.append(link)
    firefox.get(firefox.find_element_by_xpath("//a[text()='Próximo']").get_attribute("href"))
print("done.")
print("Coletando url de download...")
#dicionario para armazenar o nome do arquivo e a sua respectiva url de download
file_link = {}
for link in links:
    firefox.get(link)
    dropbox_link = firefox.find_element_by_link_text("Save to Dropbox")
    l = dropbox_link.get_attribute("data-filename")
    file_name = l[:l.index(" ")] + l[l.rindex("."):]
    file_link[file_name] = dropbox_link.get_attribute("href")

print("done.")

if not os.path.exists(os.getcwd()+"/problemas"):
    os.makedirs(os.getcwd() + "/problemas")

print("Realizando os downloads...")
for arq in file_link:
    print(arq + " -> " + file_link[arq])
    wget.download(file_link[arq], os.getcwd() + "/problemas/"+arq)

print("done.")

firefox.quit()
