# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:35:09 2019

@author: KArry
"""

import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
def normalization(data):
    scaler = MinMaxScaler(feature_range=(0,500))
    data=data.iloc[:,1:3]
    scaler = scaler.fit(data)
    return scaler.transform(data)

def standardization(data):
    scaler = StandardScaler()
    #X.drop(columns=[0])
    data=data.iloc[:,1:3]
    scaler = scaler.fit(data)
    return scaler.transform(data)
page = requests.get('https://www.iplt20.com/stats/2019/player-points')
page1=requests.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting')
page2=requests.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling')
page3=requests.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder')

B=['JOS BUTTLER',
'MS DHONI',
'kl RAHUL',
'RISHABH PANT',
'DINESH KARThIK',
'ISHAN KISHAN',
'SANJU SAMSON',
'WRIDDHIMAN SAHA',
'SHANE WATSON',
'DWAYNE BRAVO',
'ANDRE RUSSELL',
'SUNIL NARINE',
'KRUNAL PANDYA',
'HARDIK PANDYA',
'RAVINDRA JADEJA',
'CHRIS MORRIS',
'BEN STOKES',
'GLENN MAXWELL',
'kieron POLLARD',
'vijaySHANKAR',
'DAVID WARNER',
'CHRIS LYNN',
'ABDevilliers',
'chrisGAYLE',
'KANE WILLIAMSON',
'NITISH RANA',
'MAYANK AGARWAL',
'DAVID MILLER',
'viratKOHLI',
'SURYAKUMAR YADAV',
'SHIKHAR DHAWAN',
'SURESH RAINA',
'SHREYAS IYER',
'ajinkyaRAHANE',
'robinUTHAPPA',
'ROHIT SHARMA',
'SHUBAMan GILL',
'RAHUL TRIPATHi',
'ANDREW TYE',
'RASHID KHAN',
'KAGISO RABADA',
'JOFRA ARCHER',
'MUJEEB UR RAHMAN',
'IMRAN TAHIR',
'TIM SOUTHEE',
'SIDdARTH KAUL',
'UMESH YADAV',
'jaspritBUMRAH',
'KULDEEP YADAV',
'SHARDUL THAKUR',
'MAYANK MARKANDE',
'AMIT MISHRA',
'yuzvendraCHAHAL',
'SANDEEP SHARMA',
'JAYDEV UNADKAT',
"DEEPAK CHAHAR"]
M=B.copy()
for i in range(56):
	
	
	B[i]=B[i].strip().replace(" ","").lower()
soup = BeautifulSoup(page.text, 'html.parser')
article=soup.find("table",{"class":"table table--scroll-on-tablet top-players"})
A=[['andrerussell',369]]
Dict={"name":[],"score":[]}
df=pd.DataFrame(Dict)
with open('cod.csv','w') as f:
    for tr in article.find_all('tr')[2:]:
        tds = tr.find_all('td')
		
        #print((str(tds[1].text)))
		
        df2={"name":[str(tds[1].text).strip()],"score":[str(tds[1].text).strip()]}
		
        print(str(tds[1].text).strip().replace("\n"," ").replace(" ",""))
		
		
        A.append([str(tds[1].text).strip().replace("\n"," ").replace(" ","").lower(),float(str(tds[2].text).strip())])
        
        #df.append(pd.DataFrame(df2),ignore_index=True)
		#print(str(tds))
		
       # print((tds[1].text))
   
    f.close()
	
	
soup = BeautifulSoup(page1.text, 'html.parser')
#article=soup.find("div",{"class":"cb-col cb-col-100 cb-padding-left0"})
#for tr in article.find_all('tr')[2:]:
article1=soup.find("div",{"class":"cb-col cb-col-100 cb-plyr-tbody"})
	   
#nx=article1.find_all("div")
nx1=article1.find("div",{"ng-show":"'batsmen-t20s' == act_rank_format"})
names=  nx1.find_all("div",{"class":"cb-col cb-col-67 cb-rank-plyr"})
rate=nx1.find_all("div",{"class":"cb-col cb-col-17 cb-rank-tbl pull-right"})
n=str(names[2].text)
F=[]	

for i in range(94):
	v=str(names[i].text).strip().split()[0:2]
	x=v[0]+v[1]
	F.append([x.replace(" ","").lower(),float(rate[i].text)])
        
soup = BeautifulSoup(page2.text, 'html.parser')
#article=soup.find("div",{"class":"cb-col cb-col-100 cb-padding-left0"})
#for tr in article.find_all('tr')[2:]:
article1=soup.find("div",{"class":"cb-col cb-col-100 cb-plyr-tbody"})
	   
#nx=article1.find_all("div")
nx1=article1.find("div",{"ng-show":"'bowlers-t20s' == act_rank_format"})
names=  nx1.find_all("div",{"class":"cb-col cb-col-67 cb-rank-plyr"})
rate=nx1.find_all("div",{"class":"cb-col cb-col-17 cb-rank-tbl pull-right"})
n=str(names[2].text)
F2=[]	

for i in range(94):
	v=str(names[i].text).strip().split()[0:2]
	x=v[0]+v[1]
	F2.append([x.replace(" ","").lower(),float(rate[i].text)])


soup = BeautifulSoup(page3.text, 'html.parser')
#article=soup.find("div",{"class":"cb-col cb-col-100 cb-padding-left0"})
#for tr in article.find_all('tr')[2:]:
article1=soup.find("div",{"class":"cb-col cb-col-100 cb-plyr-tbody"})
	   
#nx=article1.find_all("div")
nx1=article1.find("div",{"ng-show":"'allrounders-t20s' == act_rank_format"})
names=  nx1.find_all("div",{"class":"cb-col cb-col-67 cb-rank-plyr"})
rate=nx1.find_all("div",{"class":"cb-col cb-col-17 cb-rank-tbl pull-right"})
n=str(names[2].text)
F3=[]	

for i in range(9):
	v=str(names[i].text).strip().split()[0:2]
	x=v[0]+v[1]
	F3.append([x.replace(" ","").lower(),float(rate[i].text)])

"""	
        
	df2={"name":[str(tds[1].text).strip()],"score":[str(tds[1].text).strip()]}
		
	      
	print(str(tds[1].text).strip().replace("\n"," ").replace(" ",""))
		
		
	   
	W.append([str(tds[1].text).strip().replace("\n"," ").replace(" ","").lower(),float(str(tds[2].text).strip())])
        
 """       #df.append(pd.DataFrame(df2),ignore_index=True)
		#print(str(tds))
X=[]
P=[]
for i in range(56):
	f=0
	for j in range(162):
		if(B[i]==A[j][0]):
			X.append([A[j][0],A[j][1],0,0])    	   
			f=1       
			   
	if (f==0):
	     X.append(['glennmaxwell',174,0,0])
print(P)
for j in range(56):
	V=[]
	for i in range(94):
		if (X[j][0]==F[i][0]):
			V.append(F[i][1])
	for i in range(94):
		if (X[j][0]==F2[i][0]):
			V.append(F2[i][1])
	for i in range(9):
        
	    if (X[j][0]==F3[i][0]):
		    V.append(F3[i][1])
	if(len(V)!=0):
		X[j][2]=max(V)
X=pd.DataFrame(X)
X=normalization(X)
Z=[]
for i in range(56):
	if(X[i][1]==0):
		r=float(X[i][0])
		Z.append([M[i],X[i][0],X[i][1],r])
	else:
		r=(float(X[i][0])*3 + float(X[i][1])*2)/5
		Z.append([M[i],X[i][0],X[i][1],r])
	
	
Z=pd.DataFrame(Z)
Z.to_csv("data.csv")
#article1=article.find_all('td')
#for i in article1:
 #   print(i.text)
    