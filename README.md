## Building the dev environment
- First, make sure you have **Python** and **Node.js** installed, preferrably with an up to date version.
- You can clone the repo into a folder, then install the Node packages with `npm install`. You can then run `npm run dev` for the front end
- For the Django backend (located in the `/server` folder), we used a python virutal environment to isolate installed dependencies. It is recommended you make a python virtual environment in the `/server` folder with `python -m venv venv` and activate the python virtual environment with `.\venv\Scripts\activate` (this is for windows, on Mac it may be `source venv/bin/activate`)
- Once the virtual env is activated, you can install the python packages in the same `/server` from the `requirements.txt` folder with `pip install -r requirements.txt`

## Running the dev environment
- To run the front end, use `npm run dev` in the main folder you copied the github repo into
- To run the backend, navigate to `/server`, activate the python virtual env for the dependencies to be recognized, then navigate to `/server/mysite` and run `python manage.py makemigrations` and `python manage.py migrate` to initialize the database. Once that is done, you can run `python manage.py runserver` to start the Django server

## Usage
- The Django server should be running for full functionality
- To see the website locally, once you have started the front end using `npm run dev` and the back end server using `python manage.py runserver` in `/server/mysite`, you can navigate to `localhost:3000`
- To navigate to pages manually, you can go to `localhost:3000/{page}`, where `{page}` is a subdomain defined by the folders in `src/app` (for example, to navigate to the admin page, navigate to `localhost:3000/admin` and to go to the user profile go to `localhost:3000/userprofile`, however the user profile page is protected with a login. You can edit the user profile and add skills (will be necessary later to test volunteer matching functionality)
- There are no "mock" prefilled objects, so you will need to create users via `localhost:3000/signup` and login to the user profile via `localhost:3000/signin`
- Since there are no prefilled objects, events will have to be created too, so navigate to `localhost:3000/admin` (not protected with login, you can also use the "Event management" button in the navbar to navigate to the admin page) to create events and update them, so that `localhost:3000/findevents` can populate with events for the users/volunteers to sign up for
- For volunteer matching, events have skills needed and volunteers have skills defined in their user profiles. You can filter volunteers with matching skills at the bottom of `localhost:3000/admin` to test volunteer matching
- For notifications, if an event the volunteer is signed up for is updated, it will send a notification to the user profile page notifying the volunteer that the event has been updated
- Login sessions only last for 30 minutes everytime you login, so make sure to login again if testing longer than 30 minutes at a time otherwise an authorization error will pop up if you stay on the page logged in for more than 30 minutes since the token expired.

### Unit testing
- To run the unit tests, navigate to `/server/mysite` and run `python manage.py test`, which will show details about the tests in the your terminal

### Generating reports
- You have 2 options to generate reports, PDF and CSV, which will have buttons in `localhost:3000/admin` at the bottom of the page. You can also use the "Event management" button in the navbar to navigate to the admin page.
- Make sure to generate some volunteers via signing up, generate some events, and sign up those volunteers for events so that there can be data to display in the reports.

## Troubleshooting
- If you are on Mac, when running python commands, you may want to replace `python` with `python3`
- If Django dependencies are not recognized, remember to activate the python virtual environment in `/server`
- Sometimes the dependencies for Django in `/server` are not recognized, so it is best to open the `/server` project in your text editor in a separate instance as the head folder (for example, in VS Code, have the `/server` folder in the top right as the uppermost folder, along with another window with the main folder as the head folder to run the front end)
- When running `python manage.py makemigrations` and `python manage.py migrate` in `/server/mysite`, sometimes there will be errors regarding the database. A fix would be to delete the `db.sqlite3` file in `/server/mysite` and also deleting the numbered migration files in `/server/mysite/api/migrations`, then rerunning `python manage.py makemigrations` and `python manage.py migrate`
- Because the login session uses a JWT token, the login session only lasts for 30 minutes at a time, then you have to re login to get access to the user profile. Otherwise, you will receive an authorization error

# -----

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).
