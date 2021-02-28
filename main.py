from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
# from selenium import webdriver
import pandas as pd
from datetime import date



Region=[]
District=[]
Municipality=[]
Voter_in_List=[]
Issued_Envelopes=[]
Turnout_in_Percen=[]
Submitted_Envelopes=[]
Valid_Voted=[]
Percentage_of_Valid_Vote=[]
Municipality_code=[]

Name=[]
Valid_Vote_Total=[]
Valid_Vote_In_Percentage=[]

file = input('Enter csv Name :')
url = input('Please Enter Url Link Here'
            '(https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111)...')
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = uReq(req).read().decode('utf-8', 'ignore')
page_soup = soup(page_html, "html.parser")
for num in page_soup.findAll("td",{"class","cislo"}):
    numberList = num.text
    print(numberList)
print('Please select one Number from these,,,,,,,,,,,,,,')
numbr =  input('Enter Number Here :')
page = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec='+str(numbr)
req1 = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
page_html1 = uReq(req1).read().decode('utf-8', 'ignore')
page_soup1 = soup(page_html1, "html.parser")

try:
    region = page_soup1.findAll("div",{"class","topline"})[0].findAll('h3')[0].text.strip()
except:
    region = ''
try:
    district = page_soup1.findAll("div",{"class","topline"})[0].findAll('h3')[1].text.strip()
except:
    district
try:
    municipality = page_soup1.findAll("div",{"class","topline"})[0].findAll('h3')[2].text.strip()
except:
    municipality = ''
try:
    voter_in_list = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[3].text
except:
    voter_in_list = ''
try:
    issued_envelopes = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[4].text
except:
    issued_envelopes = ''
try:
    turnout_in_percen = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[5].text.replace(",",".")
except:
    turnout_in_percen = ''
try:
    submitted_envelopes = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[6].text
except:
    submitted_envelopes = ''
try:
    valid_voted = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[7].text
except:
    valid_voted = ''
try:
    percentage_of_valid_vote = page_soup1.findAll("table",{"class","table"})[0].findAll('tr')[2].findAll('td')[8].text
except:
    percentage_of_valid_vote = ''
for table in page_soup1.findAll("table",{"class","table"})[1:3]:
    rows = table.findAll('tr')[2:]
    for row in rows:
        try:
            name = row.findAll('td')[1].text.strip().replace(",","")
            Name.append(name)
            Region.append(region)
            District.append(district)
            Municipality.append(municipality)
            Voter_in_List.append(voter_in_list)
            Issued_Envelopes.append(issued_envelopes)
            Turnout_in_Percen.append(turnout_in_percen)
            Submitted_Envelopes.append(submitted_envelopes)
            Valid_Voted.append(valid_voted)
            Percentage_of_Valid_Vote.append(percentage_of_valid_vote)
            Municipality_code.append(numbr)
        except:
            name = ''
            Name.append(name)
        try:
            valid_vote_total = row.findAll('td')[2].text.strip()
            Valid_Vote_Total.append(valid_vote_total)
        except:
            valid_vote_total = ''
            Valid_Vote_Total.append(valid_vote_total)
        try:
            valid_vote_in_percentage = row.findAll('td')[3].text.replace(",",".")
            Valid_Vote_In_Percentage.append(valid_vote_in_percentage)
        except:
            valid_vote_in_percentage = ''
            Valid_Vote_In_Percentage.append(valid_vote_in_percentage)

data={'Name': Name, 'Valid_Vote_Total': Valid_Vote_Total, 'Valid_Vote_In_Percentage':Valid_Vote_In_Percentage,
      'Region':Region, 'District':District,
      'Municipality': Municipality, 'Voter_in_List': Voter_in_List, 'Issued_Envelopes':Issued_Envelopes,
      'Turnout_in_Percen':Turnout_in_Percen, 'Submitted_Envelopes':Submitted_Envelopes,
      'Valid_Voted': Valid_Voted, 'Percentage_of_Valid_Vote': Percentage_of_Valid_Vote,
      'Municipality_code': Municipality_code,}
df=pd.DataFrame.from_dict(data=data, orient='index')
df1 = df.T
df1.to_excel(str(file)+".xlsx", index=False)
# df1.to_csv("~/Desktop/books_to_scrap/Votes.csv", index=False)
# df1.to_excel("~/Desktop/"+str(file)+".xlsx", index=False)
