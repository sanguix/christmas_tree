# Christmas lights
## Description

## Requirements

Python requirements are stored in py3_requirements.txt.
To install them run:

    pip3 install -r py3_requirements.txt

## Execution

Superuser permission is needed to access to GPIO pins and
/dev/mem, so any tool that uses this library should be executed
with 'sudo'

## Restful API server

The restful API server allows to change the lights using HTTP
requests.

### Start the server

    sudo ./rest_server.py
