from bs4 import BeautifulSoup
import pandas as pd
import requests
def rankrange(regular,l,r):
    return regular.loc[(regular['Rank']>l) & (regular['Rank']<r)].shape[0]



def getranks(userhandle):
    content = requests.get("https://codeforces.com/contests/with/"+userhandle) .text


    soup = BeautifulSoup(content,"lxml")
    f1 = []
    table1 = soup.find('table' , class_ = 'tablesorter user-contests-table')
    #print(table1)
    rows = table1.find_all('tr')
    column = ['index' , 'Contest' ,'St','Rank','Solved','Rc' , 'Nr' , 'comment']
    people = pd.DataFrame(columns=column)

#    for ind,row in enumerate(rows):
#         if(ind!=0):
#             cells = row.find_all('td')
#             l = []
#             for ind1,cell in enumerate(cells):
#                 if(ind1==3):
#                     l.append(int(cell.text.strip()))
#                 else:
#                     l.append(cell.text.strip())
             #print(l)
#             row1 = pd.DataFrame([l])
#             row1.columns=column
             #print(row1.head())
#             people = people.append(row1,ignore_index=True)
    for ind,row in enumerate(rows):
        if(ind!=0):
            #print(f"this is for {ind}")
            cells = row.find_all('td')
            l=[]
            for ind1,cell in enumerate(cells):
                if(ind1==3):
                    l.append(int(cell.text.strip()))
                else:
                    l.append(cell.text.strip())
            row1 = pd.DataFrame([l])
            row1.columns=column
            people=people.append(row1,ignore_index=True)
    numrows= people.shape[0]
    print(numrows)
    count1=0
    sum1=0
    for i in range(numrows):
        sum1=sum1+people.at[i,'Rank']


    print(count1)


    regular = people.loc[0:72,:]
#    print(regular.loc[regular['Rank']>4000].shape)
#    print(sum1/numrows)
    print(f"mean is {regular['Rank'].mean()}")
#    print(regular.loc[regular['Rank']<1000].shape)
    [l,r] = input(">").split()
    l = int(l)
    r= int(r)
    print(rankrange(regular,l,r))








richest_people()
