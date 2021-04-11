# Flask_vue_boilerplate
Basic web application using python Flask on Backend and Vue.js on Frontend
Inspiration: https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

## Running Backend Flask API
use python3.9+
```
pip install -r requirement.txt
python app.py

```

## Running FrontEnd Vue App

### Installing Vue.js and running client

```
npm install -g @vue/cli@4.5.11
npm install --save-dev eslint-import-resolver-alias
npm install axios@0.21.1 --save
npm install bootstrap@4.6.0 --save
```
Setting for vue client: 
```
Vue CLI v4.5.11
? Please pick a preset: Manually select features
? Check the features needed for your project: Choose Vue version, Babel, Router, Linter
? Choose a version of Vue.js that you want to start the project with 2.x
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
? Pick a linter / formatter config: Airbnb
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) No
```

Running Client:
```
$ cd client
$ npm run serve
```
