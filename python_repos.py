import requests

from plotly.graph_objs import Bar
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Сохраение ответа API в перменной.
response_dict = r.json()

# Обработка результатов.
print(f"Total repositories: {response_dict['total_count']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
repo_names, stars = [],[]
print(f"Repositories returnde: {len(repo_dicts)}")

# Анализ первого репозитория.
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Построение визуализации.
data = [{
    'type' : 'bar',
    'x' : repo_names,
    'y' : stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title' : 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
