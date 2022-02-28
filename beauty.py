
from bs4 import BeautifulSoup
import json

def beautifer():
    fileToRead = open("test.html", "r")
    soup = BeautifulSoup(fileToRead , features="html.parser")
    file = open('final.html','w')
    file.write(soup.prettify())

    fileToRead = open("final.html", "r")
    
    main_content = soup.find('ul', attrs = {'class': 'jobs-search-results__list list-style-none'})


    content = main_content.findAll('li')
    list_data=[]

    for j in range(0,len(content)):
        temp = ''
        for line in content[j].text:
                line = line.rstrip()
                if line:
                        # print(line, end = '')
                        temp = temp + line        


        temp = temp.split('\\n')
        data=[]
        # print(temp.remove(''))
        for i in range(0,len(temp)):
            if temp[i] == '':
                continue
            else:
                data.append(temp[i])
        fake_dict = {}
        if(len(data)>6):
            fake_dict={'Company':data[1],'Role':data[0],'Location':data[2],'Type':data[3]}
            list_data.append(fake_dict)
        else:
            continue
    
        
    return list_data



     



