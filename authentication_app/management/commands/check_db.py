from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Check database connectivity and configuration'

    def handle(self, *args, **options):
        self.stdout.write("=== Database Configuration Check ===")
        
        # Check environment variables
        self.stdout.write(f"DATABASE_URL set: {bool(os.environ.get('DATABASE_URL'))}")
        if os.environ.get('DATABASE_URL'):
            db_url = os.environ.get('DATABASE_URL')
            # Hide password in output
            if '@' in db_url:
                parts = db_url.split('@')
                if len(parts) > 1:
                    masked_url = parts[0].split(':')[0] + ':****@' + '@'.join(parts[1:])
                    self.stdout.write(f"DATABASE_URL: {masked_url}")
            else:
                self.stdout.write(f"DATABASE_URL: {db_url}")
        
        # Check Django database settings
        db_config = settings.DATABASES['default']
        self.stdout.write(f"Database ENGINE: {db_config.get('ENGINE', 'Not set')}")
        self.stdout.write(f"Database NAME: {db_config.get('NAME', 'Not set')}")
        self.stdout.write(f"Database HOST: {db_config.get('HOST', 'Not set')}")
        self.stdout.write(f"Database PORT: {db_config.get('PORT', 'Not set')}")
        
        # Test database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                self.stdout.write(
                    self.style.SUCCESS("✓ Database connection successful!")
                )
                
                # Check if django_session table exists
                cursor.execute("""
                    SELECT name FROM sqlite_master WHERE type='table' AND name='django_session'
                    UNION ALL
                    SELECT tablename FROM pg_tables WHERE tablename='django_session'
                """)
                result = cursor.fetchone()
                if result:
                    self.stdout.write(
                        self.style.SUCCESS("✓ django_session table exists!")
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR("✗ django_session table not found!")
                    )
                    
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"✗ Database connection failed: {e}")
            ) 