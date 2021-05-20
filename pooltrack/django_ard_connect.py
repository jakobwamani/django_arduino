os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pooltrack.settings')

django.setup()

from trackball.models import pool_table , action_table
