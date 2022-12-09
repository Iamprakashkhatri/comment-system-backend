# Installation

- Clone the repo
- Inside the cloned repo, open terminal

-setup virtual environment

```bash
python3 -m venv env
```
-install the requirements

```bash
pip install -r requirements.txt
```

-Create .env file in root folder and copy from .env.sample file.

# Run the data migrations

```bash
python manage.py migrate
```

# Running the app

- To start the app

```bash
python manage.py runserver
```

# Running the test cases

- To run the test cases

```bash
python manage.py test
```