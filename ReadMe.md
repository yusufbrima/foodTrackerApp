**App Deployment Steps**

**[Create Heroku Account](https://heroku.com)** 

**[Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)**

**Freeze Project dependencies** 
	-***pip freeze >requirements.txt***

**Create Procfile**
 	-***web: gunicorn -w 4 __filename__:__appname__***

**Create .gitignore *.* files to be ignored**

**heroku login :: to login via the terminal**

**git add . **
**git commit -m **
**git  git push heroku <branchname>  deployin the app on the heroku platform**


***Click [here](https://damp-badlands-25517.herokuapp.com/home) to see sample app***
