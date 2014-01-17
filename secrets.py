# Copy this file into secrets.py and set keys, secrets and scopes.

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here: 
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = "a very long and secret session key goes here"

# Google APIs
GOOGLE_APP_ID = '915948573455'
GOOGLE_APP_SECRET = 'dC7CBQljhmZUIIYiveJJwH-H'

# Facebook auth apis
FACEBOOK_APP_ID = '498668126915408'
FACEBOOK_APP_SECRET = '9147c61e72ea852197570f717cceff8d'

# config that summarizes the above
AUTH_CONFIG = {
  # OAuth 2.0 providers
  'google'      : (GOOGLE_APP_ID, GOOGLE_APP_SECRET,
                  'https://www.googleapis.com/auth/userinfo.profile'),
  'facebook'    : (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
                  'user_about_me'),

  # OpenID doesn't need any key/secret
}
