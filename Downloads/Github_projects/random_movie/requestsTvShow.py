from base64 import encode
import requests
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Search by name: 'https://api.tvmaze.com/search/shows?q=moon'  
# Info by IMDB id: 'https://api.tvmaze.com/lookup/shows?imdb=tt10234724' 
# show_summary = show_data['summary'].replace('<p>', '').replace('</p>', '')

# searchName_response = requests.get('https://api.tvmaze.com/search/shows?q=game')
# showData_response = requests.get('https://api.tvmaze.com/lookup/shows?imdb=tt6524350')

# print(searchName_response.json())
# print(showData_response.json())

# print(json.dumps(show_data, indent=4))


# ---------------------------------------------
"""
tt0386676 - The Office / tt10234724 - Moon Knight / tt1439629 - community / tt2467372 - Brooklyn 99 / tt0367279 - arrested development / tt6524350 - Big Mouth / tt1267295 - Cowboy bebop / tt4288182 - Atlanta / tt3398228 - Bojack / tt6994156 - Close enough / tt7221388 - Cobra Kai / tt0112159 - Neon Genesis Evangelion / tt13146488 - Peacemaker / tt1442437 - modern family / tt0472954 - Always sunny in philly / tt2934286 - Halo / tt8111088 - Mandaloriano / tt7661390 - Gangs of london / 
"""

showsID = {
            'sitcom': ['tt0386676', 'tt1439629', 'tt2467372', 'tt0367279', 'tt1442437', 'tt0472954'], 
            'action': ['tt10234724', 'tt2467372', 'tt7221388', 'tt13146488', 'tt8111088', 'tt7661390', 'tt3398228'],
            'herois': ['tt10234724', 'tt13146488', ],
            'comedy': ['tt0386676', 'tt1439629', 'tt2467372','tt0367279', 'tt6524350', 'tt4288182', 'tt6994156', 'tt1442437', 'tt2861424', 'tt0472954'],
            'drama': ['tt4288182', 'tt3398228',],
            'fantasy': ['tt10234724',],
            'science-fiction': ['tt1267295', 'tt2861424', 'tt2934286', 'tt8111088'],
            'animes': ['tt1267295',], 
            }


def get_name(ids):
    lista = []
    for id in ids:
        showData_response = requests.get(f'https://api.tvmaze.com/lookup/shows?imdb={id}')
        showName = showData_response.json()['name']
        showRating = showData_response.json()['rating']['average']
        showSummary = showData_response.json()['summary'][3:-4].replace('<b>', '').replace('</b>', '').replace('<p>', '').replace('</p>', '')
        showPoster =  showData_response.json()['image']['original']
        lista.append({'showName': showName, 'showRating': showRating, 'showSummary': showSummary, 'showPoster': showPoster})
        # print(showData_response.json())
        # print(showName)
        # print(showRating)
        # print(showSummary)
        # print(showPoster)
    return lista


