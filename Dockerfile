FROM python:3.11.4

WORKDIR /pra2/flasky

COPY requirements.txt ./

# Install the dependencies
RUN pip install -r requirements.txt

COPY . .
COPY templates ./templates
COPY hello.py .

# run-time configuration
EXPOSE 5000

#ENTRYPOINT ["./boot.sh"]

ENV FLASK_APP=hello.py
CMD ["flask", "--app", "hello.py", "run", "--host=0.0.0.0"]
