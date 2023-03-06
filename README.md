# django_tree_menu

### Features
* Compatible with Django >=2.0
* Any number of nesting levels
* Easy to add to template
* Doesn't use third-party libraries

### Usage
1. Create a virtual environment folder in your working directory
`python -m venv /path/to/directory`
2. Activate the virtual environment
* On Windows using the Command Prompt: `path\to\venv\Scripts\activate.bat`
* On Unix or MacOS, using the bash shell: `source /path/to/venv/bin/activate`
3. Intsall the dependencies
`Pip install requirements.txt`
4. Run migratitions
`python manage.py makemigrations`
`python manage.py migrate`
5. Run the server
`python manage.py runserver` and go to `127.0.0.1:8000`