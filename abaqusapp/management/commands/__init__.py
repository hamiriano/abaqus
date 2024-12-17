# __init__.py
import os
from django.core.management import call_command

if os.environ.get('RUN_MAIN', None) != 'true':
    call_command('load_portfolio_data')