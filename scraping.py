import requests
from bs4 import BeautifulSoup


# le site contient 25 page  => 246 pays

links = []

for i in range(5):

    url = 'http://example.python-scraping.com/places/default/index/' + str(i)

    response = requests.get(url)

    if response.ok:
        print(response)  # code de retour d'exécution de la requete
        print(response.headers)  # Les headers de l'objet reponse
        print(response.text)  # le contenu de la réponse en code HTML de la page

        # Objet  soup va contenir la reponse HTML pour qu'on puisse le traiter
        soup = BeautifulSoup(response.text, 'lxml')
        # si on veut par exemple de récuperer le titre
        title = soup.find('title')
        print(title.text)

        # Recuperer les liens de toute la page pour les visiter
        tds = soup.findAll('td')

        # [print(str(td) + '\n\n') for td in tds]

        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append('http://example.python-scraping.com/'+link)

print(len(links))

# avec le with le fichier sera fermé automatiquement a la fin d'ecriture ou lecture 
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n') 

# Lire le fichier crée 
with open('urls.txt', 'r') as file:
        with open('pays.csv', 'w') as filePays:
            filePays.write('pays,population\n') # entete de fichier csv
            for row in file:
                urlPays = row.strip()
                res = requests.get(urlPays)

                if (res.ok):
                    soupPays = BeautifulSoup(res.text, 'lxml')
                    country = soupPays.find('tr', {'id': 'places_country_or_district__row'}).find('td', {'class': 'w2p_fw'})
                    population = soupPays.find('tr', {'id': 'places_area__row'}).find('td', {'class': 'w2p_fw'})
                    print('Pays: ' + country.text + ' avec population: '+ population.text)
                    filePays.write(country.text + ',' + population.text.replace(',', '') + '\n')
