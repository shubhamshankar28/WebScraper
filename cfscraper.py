from bs4 import BeautifulSoup
import pandas as pd
import requests
def rankrange(regular,l,r):
    return regular.loc[(regular['Rank']>l) & (regular['Rank']<r)].shape[0]



def getranks(userhandle):
    content = requests.get("https://codeforces.com/contests/with/"+userhandle).text


    soup = BeautifulSoup(content,"lxml")

    table1 = soup.find('table' , class_ = 'tablesorter user-contests-table')

    rows = table1.find_all('tr')
    column = ['index' , 'Contest' ,'St','Rank','Solved','Rc' , 'Nr' , 'comment']
    people = pd.DataFrame(columns=column)

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
    regular = people.loc[0:numrows,:]
    print(f"you have participated in {numrows} contests")
    print("enter 1 to get mean rank")
    print("enter 2 to get the number of contests in which you got a rank greater than lower limit and less than higher limit")
    print("enter 3 to quit")
    while(True):
        print("enter a number between 1 and 3")
        x = int(input())
        if(x==3):
            break
        if(x==1):
            print(f"mean rank is {regular['Rank'].mean()}")
        if(x==2):
            print("enter two space seperated values that denote the lower limit and the higher limit respectively")
            [lower,higher] = input().split()
            lower=int(lower)
            higher= int(higher)
            answer = rankrange(regular,lower,higher)
            print(f"the number of contests in which you got a rank greater than {lower} and less than {higher} is {answer}")







print("enter your handle")
str = input(">")
getranks(str)
