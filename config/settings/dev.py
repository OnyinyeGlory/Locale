from .base import *
import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgres://onyi:Kw2cuWebLaG96X77Pxwk0qdYcIvFUCAc@dpg-cik6g1mnqql0l1o1q3og-a/locale',
        conn_max_age=600
    )
}