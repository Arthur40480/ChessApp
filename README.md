# Chess Tournament
## Développez un programme logiciel en Python

### :clipboard: Pour faire marcher ce programme, il vous faut:

*_Python :snake: :_* version 3.10

### Les librairies Python  :closed_book: :     
    flake8==6.0.0  
    flake8-html==0.4.3  
    Jinja2==3.1.2  
    MarkupSafe==2.1.2  
    mccabe==0.7.0  
    pycodestyle==2.10.0  
    pyflakes==3.0.1  
    Pygments==2.14.0  
    tinydb==4.7.1  
   
 ### Comment ça marche :question::question::question:
 
 :one:  Téléchargez le repo zip sur github  

 :two:  On viens dézipper l'ensemble de notre repo dans un nouveau dossier que l'on appellera *_ChessApp_*  

 :three:  Il va falloir créer un environnement virtuel. A l'aide du terminal, on vient choisir notre nouveau dossier :arrow_down:  

```
 cd ChessApp

```
On créé ensuite notre environement virtuel :arrow_down:
```
 python -m venv <environment name>

```
Notez que <environment name>  est un nom que vous choississez, mais par convention, il est conseillé d'utiliser *_env_*  

:four: Une fois l'environnement mis en place, il nous faut l'activer :arrow_down:
```
 .//env/Scripts/activate.ps1

```
Normalement, lors de l'activation vous devriez voir (env) devant le chemin :arrow_down:
```
 (env) PS C:\Users\Arthur\desktop\ChessApp>

```

:five: Il faut ensuite télécharger les librairies nécessaires depuis *requirements.txt* :arrow_down: 
```
 pip install -r requirements.text

```

### Nous pouvons maintenant lancer le programme de tournoi d'échecs :rocket:  
```
 python main.py

```

### Comment générer un rapport flake8 :question::question::question:
Une fois flake8 installer, il suffit de rentrer cette commande dans le terminal:
```
flake8 --format=html --htmldir=flake-report


```
  
  ## ♟️ Échec et mat :black_circle: :white_circle:
