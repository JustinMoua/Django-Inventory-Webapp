# How to run this project 
Note: (README will change after completion of project)
1. Ensure you are in the root directory path of this project. 
2. Type "cd infraTieSite" and click enter.
3. Type "infratie-env\Scripts\activate" to go into the venv.
4. Type "python manage.py runserver" to start up django applicatio.
    * django application ties in with react. If react does not update, will need to go to the react app and run build via
        1. Assuming you are in infraTie\infraTieSite\ then type "cd .." and click enter
        2. Type "cd infratie-react-app" and click enter
        3. Type "npm run build" and click enter.


Commands

* python manage.py migrate
    * The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

* python manage.py makemigrations polls
    * Have to run this when I HAVE CREATED A NEW MODEL in djangoApp/models.py
    * By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
    * Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.
