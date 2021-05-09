FROM python:3.8

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# Install dependencies via pip
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD cd /var/www/test/pyapi && export FLASK_APP=pyapi.py && export FLASK_DEBUG=1 && python -m flask run --host=0.0.0.0