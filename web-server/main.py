import store
from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def get_lista():
    return ['a', 'b', 'c']


def run():
    store.get_categorias()

if __name__ == "__main__":
    run()