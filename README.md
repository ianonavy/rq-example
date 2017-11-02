# rq example

Barebones example for running a simple Flask app that uses RQ to run jobs in the background.

Made for Vicky on 2017-11-02.

## Setup

Make new virtual environment

    pip install flask rq
    brew install redis-server

## Run

Run each of these in a separate terminal:

    redis-server  # redis server
    python app.py  # web server
    rq worker  # rq worker

## Usage

Visit http://localhost:5000/?job_id=9999

Should redirect you to the result of the job. You can see the logs of the job in the worker terminal.
