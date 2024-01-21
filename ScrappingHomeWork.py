#Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
#Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город. 


import  requests
from bs4 import BeautifulSoup
from fake_headers import  Headers
import json

headers_gen = Headers(os='windows', browser='chrome')
main_hh = requests.get('https://spb.hh.ru/search/vacancy?text=python%2C+flask%2C+django&salary=&ored_clusters=true&area=1&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line', headers = headers_gen.generate())

main_hh_html = main_hh.text

main_soup = BeautifulSoup(main_hh_html, 'html.parser')



job_data = []

jobs = main_soup.find_all('div', {"class":"vacancy-serp-item__layout"}) # Данные получили. проверил
for job in jobs:
    job_title = job.find('a', {"class":"bloko-link"}).text

    job_link = job.find('a', {"class":"bloko-link"}).get('href')
    company_name = job.find('div', {"class":"vacancy-serp-item__meta-info-company"}).text
    salary = job.find('span', {"data-qa":"vacancy-serp__vacancy-compensation"})

    if salary:
        salary = salary.text
    city = job.find('div', {"data-qa": "vacancy-serp__vacancy-address"}).text


    # description = job.find('div', {"class": "bloko-tag-list"})



    # if description and ('django' in description.text.lower() or 'flask' in description.text.lower()):
    job_info = {
        "title": job_title,
        "link": job_link,
        "company_name": company_name,
        "salary": salary,
        "city": city
        }
    job_data.append(job_info)


with open('jobs.json', 'w') as f:
    json.dump(job_data, f, indent= 4)































# posts = soup.find_all('article', class_ = "post") 
# for post in posts:
#     post_id = post.parent.attrs.get('id')
#     if not post_id:
#         continue
#     post_id = int(post_id.split('_')[-1])
#     print('post', post_id)

#    # извлекаем хабы поста
#     hubs = post.find_all('a', class_='hub-link')
#     for hub in hubs:
#         hub_lower = hub.text.lower()
#         if any([hub_lower in desired for desired in KEYWORDS]):
#             title_element = post.find('a', class_='post__title_link')
#             print(title_element.text, title_element.attrs.get('href'))
#             break
