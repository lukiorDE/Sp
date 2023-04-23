from bs4 import BeautifulSoup
import requests

url = 'http://biik.ru/rasp/cg109.htm' #website 
resp = requests.get(url) #get all from site ()
resp.encoding = 'windows-1251' #because site biik.ru rasp use cp-1251 need do that 
print(resp) #write site answer code
if resp == 404: #check if site not work
    print('Not Found')
else:
    all_web_code = resp.text #take text chapter from site 
    bs = BeautifulSoup(all_web_code,"html.parser") #bs html.parser needed site 
    Lesson = bs.findAll('td') #find all class in tag 'td'

    with open("D:\\GitHub\\SP\\Rasp.txt", "w") as file: #write in file
        for item in Lesson: #write all text from html tag in txt file
            file.write(item.text +"\n")
    
    lines = open("D:\\GitHub\\SP\\Rasp.txt").readlines() #list all line in txt file 
    for i in range(104): #Delete first 104 line, because they unused
        lines.pop(0)

    with open("D:\\GitHub\\SP\\Rasp.txt", "w") as f: #after delete unused elements, write new line in txt file
        for i in range(len(lines)-1):
            f.write(lines[i])