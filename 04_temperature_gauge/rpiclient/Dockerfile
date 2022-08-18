FROM python:3.10.6-bullseye

# RUN apt-get update \
#         && apt-get --no-install-recommends install python3-smbus -y \ 
#         && apt-get clean \
#         && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

# ARG USERID=1000
# ARG GROUPID=1000
# RUN addgroup --system --gid $GROUPID appuser
# RUN adduser --system --uid $USERID --gid $GROUPID appuser

WORKDIR /workbench
COPY ./logging_config.yaml /workbench/
COPY ./Pipfile /workbench/Pipfile
COPY ./Pipfile.lock /workbench/Pipfile.lock 

RUN pipenv install --deploy --system --dev

COPY ./*.py /workbench/

# set to no debugger.
ENV SERVER_URL="http://0.0.0.0:8000/api"
ENV DEBUGGER=False
ENV WAIT=False

# USER appuser
EXPOSE 8080
CMD ["python3", "-u", "./main.py"]
