# DEBUG
DEBUG = True
TRAP_BAD_REQUEST_ERRORS = True

# SECRET_KEY
## Insert your secret key
## To generate a secret key in a python shell:
## >>> import os
## >>> os.urandom(24)
SECRET_KEY = '895q672389rayw89fsdfioasdhjv-sdfvu90erui34029r5'

# OAuth2 Authorization Server
## EXAMPLE: Github Authorization Server endpoints
AS_AUTH_URL = 'https://github.com/login/oauth/authorize'
AS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

#AS_AUTH_URL = ''
#AS_TOKEN_URL = ''


# OAuth2 Resource Server
## EXAMPLE: Github Resource Server API endpoint
RS_API_URL = 'https://api.github.com/'

#RS_API_URL = ''

# OAuth2 Client
CLIENT_ID  = 'b1c3702780bfad366b7e'
CLIENT_SECRET = '890239aa46ffa34f982b14864e9d12acdca10c4f'
REDIRECT_URI = 'http://localhost:9000/cb'
SCOPE = 'user'

