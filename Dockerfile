FROM python

WORKDIR /app


RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 

COPY . .

# store the ENV and ARG in a file
ARG URL
ARG SECRET_TOKEN
# RUN echo "URL=${URL}\nSECRET_TOKEN=${SECRET_TOKEN}" > ./app/.env
ENV URL=$URL
ENV SECRET_TOKEN=$SECRET_TOKEN

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8004"]