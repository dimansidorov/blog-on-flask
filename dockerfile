FROM python

WORKDIR ./app

RUN pip install poetry

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry install

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

CMD ["python", "wsgi.py"]