###############################################
# 📀 Base Image
###############################################
FROM python:3.11-slim as python-base
ENV \
    # 🐍 python
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    # 📀 pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # 📀 poetry
    POETRY_VERSION=1.3.2  \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    # ✨ VENV & dependencies
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" 

# ✨ it is same like ./venv/bin/activate
ENV PATH="${POETRY_HOME}/bin:${VENV_PATH}/bin:${PATH}"


###############################################
# 🏗️ Builder Image
###############################################
FROM python-base as builder-base
ARG BUILD_DEPS="curl build-essential"
RUN apt-get update && apt-get install -y $BUILD_DEPS

# 📀 poetry: install - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION POETRY_HOME=$POETRY_HOME python3 -
# 🕰️ is deprecated 'poetry install --no-dev'
# 📀 poetry: install by pip
# RUN pip install poetry==$POETRY_VERSION 

# 📁 copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally (is depricated RUN poetry install --no-dev)
RUN poetry install --with=pgsql --sync --ansi


###############################################
# ✅ 🔨 Develop Image
###############################################
FROM python-base as develop

# 📁 📀 copy builded dependencies
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# 📁 🍎 copy application files
ENV \
    FOLDER_DESTINATION="/code" \
    FOLDER_SOURCE="." \
    DOCERIGNORE="${FOLDER_SOURCE}/dockerfiles/.dockerignore" \
    ENTRYPOINT="docker-entrypoint.sh" \
    APP_ENTRYPOINT="${FOLDER_SOURCE}/dockerfiles/${ENTRYPOINT}" \
    APP_FOLDER="${FOLDER_SOURCE}/app" \
    APP_WSGI="${FOLDER_SOURCE}/wsgi.py" 

WORKDIR $FOLDER_DESTINATION
COPY $DOCERIGNORE  ./
COPY $APP_WSGI ./
COPY $APP_FOLDER ./app


# 🚀 🍎 init project (default arg by starting `docker run`)
COPY $APP_ENTRYPOINT /code
RUN chmod +x /code/$ENTRYPOINT
ENTRYPOINT /code/$ENTRYPOINT app
# if wanna change started parameter
# CMD ["app"]
# CMD ["/bin/bash"]






