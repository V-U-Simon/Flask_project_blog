FROM python:3.11-slim as base
# LABEL maintainer="Aurhor <name.it@mail.ru>"


# 📦 env variables
# PYTHONUNBUFFERED — мнговенный вывод в консоль (для логов)
# PYTHONDONTWRITEBYTECODE — отключить кеширование в `.pyc`
ENV \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.2 \
  # POETRY_HOME=/root/poetry \
  FLASK_APP=$DESTINATION_PROJECT_FOLDER/wsgi.py \
  DESTINATION_PROJECT_FOLDER=/code \
  SOURCE_DOCKERFILES_FOLDER='./dockerfiles' \
  SOURCE_APP_FOLDER='app' 


# 🔌 открыть порты (надо запускать с ключем -P | docker run -P)
EXPOSE 5000


# 📀 сборка зависимостей (с ARG удобнее указывать перчень)
ARG BUILD_DEPS=""
RUN apt-get update && apt-get install -y $BUILD_DEPS
RUN pip install poetry==$POETRY_VERSION
# Альтернативная установка poetry
# RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION POETRY_HOME=$POETRY_HOME python3 -
# ENV PATH="${PATH}:${POETRY_HOME}/bin"


# 📂 опредение рабочеей директории и копирование в контейнер папок и файлов.
WORKDIR $DESTINATION_PROJECT_FOLDER 
COPY [\
  "wsgi.py", \
  "poetry.lock", \
  "pyproject.toml", \
  "${SOURCE_DOCKERFILES_FOLDER}/.dockerignore", "${DESTINATION_PROJECT_FOLDER}"]
COPY $SOURCE_APP_FOLDER $DESTINATION_PROJECT_FOLDER


# 📀 poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
# pip (аналог poetry)
# RUN pip3 install -r requirements


# 🚀 Инициализация проекта 
COPY ["${SOURCE_DOCKERFILES_FOLDER}/docker-entrypoint.sh", "${DESTINATION_PROJECT_FOLDER}"]
RUN chmod +x $DESTINATION_PROJECT_FOLDER/docker-entrypoint.sh
ENTRYPOINT $DESTINATION_PROJECT_FOLDER/docker-entrypoint.sh
# Аргумент по умолчанию при запуске `docker run`
CMD ["app"]