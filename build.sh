set -o errexit

pip install -r requirements.txt

pip manage.py collectstatic --no-input

python manage.py migrate