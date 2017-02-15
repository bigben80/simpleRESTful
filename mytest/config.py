class Config:
    DEBUG = False
    TESTING = False
    TIMEOUT = 0.02
    PORT = 5959
    URL_PREFIX = "/api/v1"

class DebugConfig(Config):
    DEBUG = True

config = {
    'default': DebugConfig
    }
