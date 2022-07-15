# foodapp

## Build Setup


Déploiement

Après avoir effectué un git clone du projet en local, entrer dans le projet.


Côté Python :

Installer fastapi 

https://fastapi.tiangolo.com/

```bash
pip3 install fastapi
pip3 install "uvicorn[standard]"
python3 -m uvicorn main:app --reload #lance le serveur backend en python
```


Côté Nuxt (nodeJS) :

Dans un autre terminal, lancer ces deux commandes :
```bash
npm i
npm run dev
```
Si vous êtes sur Windows et que Node.js and NPM ne sont pas installés, les installer en suivant les instructions sur la page (https://phoenixnap.com/kb/install-node-js-npm-on-windows), puis lancer les deux commandes npm précédentes.


Si SQLite n'est pas déjà installé, installer DB Browser for SQLite via cette page : https://sqlitebrowser.org/dl/


Puis ouvrir la page :
http://localhost:3000/

# daniel-serra
