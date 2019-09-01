**<h1>App Deployment Steps</h1>**

**<h3>[Create Heroku Account](https://heroku.com)</h3>** 

**<h3>[Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)</h3>**

**<h3>Freeze Project dependencies</h3>** 
	-***pip freeze >requirements.txt***

**<h3>Create Procfile**
 	-***web: gunicorn -w 4 __filename__:__appname__***

**<h3>Create .gitignore *.* files to be ignored</h3>**

**<h3>heroku login :: to login via the terminal</h3>**

**<h3>git add .</h3>**

**<h3>git commit -m</h3>**


**<h3>git  git push heroku <branchname>  deployin the app on the heroku platform</h3>**


***<h3><a href="https://damp-badlands-25517.herokuapp.com/home" target="_blank" >Click here to see sample app</a></h3>***
