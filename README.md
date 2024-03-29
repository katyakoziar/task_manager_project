# IT Company Task Manager 

## Description

- Task Manager will handle all possible problems during product development in your team.
- Everyone from the team can create, update, delete Task.
- Everyone from the team can assign Task to team-members.
- Everyone from the team can set a deadlines and mark the Task as done.

## Check it out!

[Task Manager project deployed t Render](https://task-manager-project-akn9.onrender.com/)

Test user:
- login: adminuser
- password: adminuser1234

## How to install the project

1) Open the terminal and navigate to the folder where you want to clone the repository.
    ```
    cd path/to/your/directory
    ```

2) Use the git clone command to clone the repository.
   ```
   git clone repository_url
   ```
   
3) Go to the project directory.
   ```angular2html
   cd task_manager_project
   ```
   
4) Create and activate a virtual environment:
   ```angular2html
   python -m venv venv
   ```
   - for Windows:
   ```angular2html
   .\venv\Scripts\activate
   ```
   - for Linux/Mac:
   ```angular2html
   source venv/bin/activate
   ```
   
5) Use pip to install the requirements.
   ```angular2html
   pip install -r requirements.txt
   ```
   
6) Apply the migrations.
   ```angular2html
   python manage.py migrate
   ```
7) Use the following command to load prepared data from fixture
```angular2html
   python manage.py loaddata db_data.json
   ```
   
8) Run the Django development server.
   ```angular2html
   python manage.py runserver
   ```

![DB structure](static/images/db_structure.png)