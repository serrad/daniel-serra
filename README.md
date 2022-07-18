# foodapp

## Build Setup


Déploiement

Après avoir effectué un git clone du projet en local, entrer dans le projet.


Côté Python :

Installer fastapi 

https://fastapi.tiangolo.com/

```bash
# 2 commandes à ne lancer que lors de la première installation
pip3 install fastapi
pip3 install "uvicorn[standard]"

python3 -m uvicorn main:app --reload # Lance le serveur backend en python
```


Côté Nuxt (nodeJS) :

Dans un autre terminal, lancer ces deux commandes :
```bash
# Commande à ne lancer que lors de la première installation
npm i

npm run dev # Lance le serveur de développement Nuxt
```

Si vous êtes sur Windows et que Node.js and NPM ne sont pas installés, les installer en suivant les instructions sur la page (https://phoenixnap.com/kb/install-node-js-npm-on-windows), puis lancer les deux commandes npm précédentes.

Si vous êtes sur MacOS et que Node.js and NPM ne sont pas installés, les installer en suivant les instructions sur la page (https://phoenixnap.com/kb/install-npm-mac), puis lancer les deux commandes npm précédentes.


Puis ouvrir l'URL suivant (local) :
http://localhost:3000/

# daniel-serra
