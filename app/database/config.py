import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'martin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'martin')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'customerapi')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'customerapi_test')
