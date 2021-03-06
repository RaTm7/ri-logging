"""
created at: 2018-12-19
author:     Volodymyr Biryuk

The module to run the micro service locally for development purposes.
"""
import os

import microservice

if __name__ == '__main__':
    # Uncomment and fill information into the following lines if the config file needs to be recreated on every startup.
    try:
        os.remove('config.json')
    except FileNotFoundError:
        pass
    os.environ['DB_HOST'] = ''
    os.environ['DB_PORT'] = ''
    os.environ['DB_AUTH_MECHANISM'] = ''
    os.environ['DB_AUTH_SOURCE'] = ''
    os.environ['DB_NAME_FRONTEND_LOGS'] = ''
    os.environ['DB_USER'] = ''
    os.environ['DB_PASSWORD'] = ''
    os.environ['DB_CONNECTION_TIMEOUT'] = ''

    os.environ['API_URL'] = ''
    os.environ['API_BEARER_TOKEN'] = ''
    os.environ['DIR_DEBUG_LOG'] = ''
    os.environ['DIR_BACKEND_LOG'] = ''

    os.environ['DEBUG'] = 'True'
    os.environ['LOGGING_LEVEL'] = 'INFO'

    app = microservice.create_app()
    app.run(host='0.0.0.0', port=9798)
