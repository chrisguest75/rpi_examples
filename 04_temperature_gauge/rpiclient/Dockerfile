FROM python:3.9.2-buster

RUN pip install pipenv

ARG USERID=1000
ARG GROUPID=1000
RUN addgroup --system --gid $GROUPID appuser
RUN adduser --system --uid $USERID --gid $GROUPID appuser

WORKDIR /workbench
COPY ./Pipfile /workbench/Pipfile
COPY ./Pipfile.lock /workbench/Pipfile.lock 

RUN pipenv install --deploy --system --dev

COPY ./main.py /workbench/main.py

# set to no debugger.
ENV SERVER_URL="http://0.0.0.0:8000/api"
ENV DEBUGGER=False
ENV WAIT=False

USER appuser
EXPOSE 8080
CMD ["python3", "-u", "./main.py"]
