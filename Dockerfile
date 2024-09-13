FROM python:3.8.5-slim-buster
# Install requirements
RUN pip3 install -r requirements.txt

# Starting Worker
CMD ["python3","-m", "shivu"]
