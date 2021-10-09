import requests
from bs4 import BeautifulSoup as bs
import os, sys

champions_wiki = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
fandom = 'https://leagueoflegends.fandom.com/'

def parser(url):
    '''Parser with the url with beautiful soup'''
    return bs(requests.get(url).content, 'html.parser')

def champions_list():
    html = parser(champions_wiki)
    lista = {}
    for div in html.find_all('div', class_='floatleft'):
        for a in div.find_all('a'):
            camp = Champion(a.get('title').replace('/LoL',''),a.get('href'))
            lista[camp.nome] = camp
    return lista

def champion_bio(champion_link):
    html = parser(champion_link)
    skill_p,skill_q,skill_w,skill_e,skill_r = None,None,None,None,None
    for div in html.find_all('div', class_='skill skill_innate'):
        skill_p = div.get_text().split('\n')
        skill_p = [i+'\n' for i in skill_p if i.strip() and (not 'Edit' in i)]
    for div in html.find_all('div', class_='skill skill_q'):
        skill_q = div.get_text().split('\n')
        skill_q = [i+'\n' for i in skill_q if i.strip() and (not 'Edit' in i)]
    for div in html.find_all('div', class_='skill skill_w'):
        skill_w = div.get_text().split('\n')
        skill_w = [i+'\n' for i in skill_w if i.strip() and (not 'Edit' in i)]
    for div in html.find_all('div', class_='skill skill_e'):
        skill_e = div.get_text().split('\n')
        skill_e = [i+'\n' for i in skill_e if i.strip() and (not 'Edit' in i)]
    for div in html.find_all('div', class_='skill skill_r'):
        skill_r = div.get_text().split('\n')
        skill_r = [i+'\n' for i in skill_r if i.strip() and (not 'Edit' in i)]
    return skill_p, skill_q, skill_w, skill_e, skill_r

def fill():
    lista = champions_list()
    for i in lista.values(): 
        print(f'Getting {i.nome}')
        i.set_skill(*champion_bio(i.link))
    return lista

class Champion:
    def __init__(self, nome, link):
        global fandom
        self.nome = nome
        self.link = fandom + link
    def __str__(self):
        return f'nome: {self.nome} e link: {self.link}'
    def set_skill(self,p,q,w,e,r):
        self.p,self.q,self.w,self.e,self.r = "","","","",""
        for i in p: self.p += i
        for i in q: self.q += i
        for i in w: self.w += i
        for i in e: self.e += i
        for i in r: self.r += i

def main():
    lista = fill()
    with open('size_of_kit.txt', 'w') as file:
        file.write(f'{str(len(lista))}\n')
        for i in lista.values():
            total = 0
            file.write(f'{i.nome}\n')
            file.write(f'p: {str(len(i.p.split()))}\n')
            total += len(i.p.split())
            file.write(f'q: {str(len(i.q.split()))}\n')
            total += len(i.q.split())
            file.write(f'w: {str(len(i.w.split()))}\n')
            total += len(i.w.split())
            file.write(f'e: {str(len(i.e.split()))}\n')
            total += len(i.e.split())
            file.write(f'r: {str(len(i.e.split()))}\n')
            total += len(i.r.split())
            file.write(f'Total: {total}\n')
            file.write('\n')
    return lista


if __name__== '__main__':
    main()
