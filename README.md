# TRACKER SERVER

Small server written in Flask that serves as an API and manage a postgreSQL DB to the Tracker App. An app that I'm building to solve a problem we have in our Track and Field team: how to save our performance for both training and competition and in a later version, who will be attending a particular competition to help the coaches have a clear view on that. All of that designed to have a better experience than using an Excel Sheet.

The app is destined to grow in content and technically.

Clone the repo git@github.com:gryanab/tracker-server.git. 

- [Install](#install)
- [Run](#run)
- [Structure](#structure)
# Install

I recommend you work in a virtual environement.

```
python3 -m venv <name> 
```
then activate with
```
source env/bin/activate
```

to decativate run 
```
source env/bin/deactivate
```

 - `cd` to `src` and install all required packages by using 
 ```
 pip install -r requirements.txt
 ```

 - DB instantation is not containerised. So you need to create a table on a DB listening to port `5555` in order to be able to perform some actions. You can do it on [Pg Admin](https://www.pgadmin.org/download/). 

 - Once your DB is runnning, naviagte to the `db_service.py` file in `src`-> `services` -> `db` and uncomment call for `create_table`. Run the file using 
    ```
    python3 db_service.py
    ```
    Your table should be created, up and running.
    You can verify that by connecting to it on the tool of your choice with the following creds:
    ```
    dbname='tracker' user='postgres' host='localhost' port='5555' 
    ```


 # Run

 Then in `src` folder run 
 ``` 
 FLASK_APP=app.py FLASK_ENV=development flask run
 ``` 
 
 to run it in dev mode. Server should be now running.

# Structure

- in `src`
    - `app.py` serves as an api 
    - in `services`
        - `db_service.py`holds db instantiation process
        - `command` holds methods used to interact with the db