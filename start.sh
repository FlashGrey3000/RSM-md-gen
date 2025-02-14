#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port $PORT # please don't change this, it's for deploying on render