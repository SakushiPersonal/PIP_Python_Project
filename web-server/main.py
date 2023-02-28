import store
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return ['Bruno', 'Emmanuel', 'Angel']

@app.get("/family")
def get_dict():
    return {'familia': 5}

def run():
    store.get_categories()


if __name__ == '__main__':
    run()