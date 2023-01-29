#!/usr/bin/env sh
# 🚨 отвечает за вывод кода ошибки при ошибке в скрите (PID 1)
set -e 

case "$1" in
    app) # команда для запуска
        # ℹ️ exec необходим для корректного назначения PID=1
        # exec bash -c """python -u wsgi.py"""
        exec bash -c "flask run"
        ;;
    bash) # команда для запуска
        exec /bin/bash
        ;;
    *)
        exec "$@"
esac