FROM python


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir -r /code/requirements.txt


COPY ./ /code


CMD ["uvicorn", "src.main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]