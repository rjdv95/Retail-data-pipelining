import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '34.116.128.233',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('RETAIL_DB_USER'),
            'DB_PASS': os.environ.get('RETAIL_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '34.116.128.233',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('CUSTOMER_DB_USER'),
            'DB_PASS': os.environ.get('CUSTOMER_DB_PASS')
        }
    }
}