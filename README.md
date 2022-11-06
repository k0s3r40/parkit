# parkit



virtualenv -p python3 venv
. venv/bin activate

pip install -r requirements.txt

./manage.py migrate

./manage.py loaddata initial_data.json 

./manage.py runserver