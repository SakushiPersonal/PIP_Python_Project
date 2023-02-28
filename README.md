# **PIP Python Project**

>Hope this small proyect works for you. If you find something usefull, feel free to copy it and make use of it.

- PIP Installation and Preparations with VSC
- Create Git & Github Repository
- Rock, Paper, Scissors Game  
- Generate charts with matplotlib  
- Generate charts by reading CSV
- Reading CSV with Pandas dependenciess
- Set ONLINE FastAPI apps with uvicorn
- Create containers with Docker for my Apps/Scripts and run them



##  Game Project

> Para correr el juego debes seguir las siguientes instrucciones en la terminal (Previo a esto debes haber copiado el codigo del juego para ponerlo en tu main.py, el codigo esta en game/main.py ):


```sh
	cd game
	python3 main.py
	git add .
	git commit -m “Work in readme”
	git push origin master
```

**Actualizar y verificar**

## App Project
> Para poder usar este programa debes tener las dependencias adecuadas en tu venv:

```sh
	git clone
	cd app
	python3 -m venv env
	source env/bin/activate
	pip3 install -r requirements.txt
	python3 main.py
```

## FastAPI & Uvicorn
>Crear apps con FastAPI y levantarlas en la web con Uvicorn:

```sh
	pip install fastapi
    pip install "uvicorn[standard]"
```
**Creas tu app con FastAPI y luego la levantas en consola con uvicorn**

```sh
	uvicorn main:app --reload
```