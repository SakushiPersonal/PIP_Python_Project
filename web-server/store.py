import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    #r.text es en formato str, por lo cual debemos transformarlo antes de poder trabajar con el.
    categories = r.json()
    
    for category in categories:
        print(category['name'])