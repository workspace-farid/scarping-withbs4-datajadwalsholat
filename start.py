import bs4
import requests


url = 'http://www.jadwalsholat.pkpu.or.id/?id=66'
contents = requests.get(url)
#print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
#print (response)
data = response.find_all('tr', 'table_highlight')
data = (data[0])

sholat = {}
a = 0
for data in data:
        if a == 1:
            sholat ['subuh'] = data.get_text()
        elif a == 2:
            sholat ['dzuhur'] = data.get_text()
        elif a == 3:
            sholat ['ashar'] = data.get_text()
        elif a == 4:
            sholat['maghrib'] = data.get_text()
        elif a == 5:
            sholat ['isya'] = data.get_text()
        a += 1

print(sholat)
print (f"\njadwal sholat ashar untuk denpasar adalah {sholat['ashar']} wita")













