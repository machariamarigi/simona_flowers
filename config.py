""" Application Configuration"""

import s3_config as S3


class Config(object):
    """Common configurations"""


class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    S3_LOCATION = S3.S3_Config['S3_LOCATION']
    S3_KEY = S3.S3_Config['S3_KEY']
    S3_SECRET = S3.S3_Config['S3_SECRET']
    S3_UPLOAD_DIRECTORY_1 = S3.S3_Config['S3_UPLOAD_DIRECTORY_1']
    S3_BUCKET = S3.S3_Config['S3_BUCKET']


class ProductionConfig(Config):
    "Production configurations"
    DEBUG = False
    S3_LOCATION = S3.S3_Config['S3_LOCATION']
    S3_KEY = S3.S3_Config['S3_KEY']
    S3_SECRET = S3.S3_Config['S3_SECRET']
    S3_UPLOAD_DIRECTORY_1 = S3.S3_Config['S3_UPLOAD_DIRECTORY_1']
    S3_BUCKET = S3.S3_Config['S3_BUCKET']


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
