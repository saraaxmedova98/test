FROM  python:3.6

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 5000

# ENV FLASK_APP "run.py"

# CMD [ "python", "run.py", "--host", "0.0.0.0", "--port", "5000"]

