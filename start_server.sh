#!/bin/bash
uwsgi --http 127.0.0.1:8080 --module isqli.isqli_app --callable app --gevent 100 --check-static isqli/static
