from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user =CustomUser(name="admin",email="admin@gmail.com", is_staff=True, is_superuser=True, is_active=True, phone="9876543456",gender="Male")
        user.set_password("12345")
        user.save()

    dependencies = [
    ]

    operations =[
        migrations.RunPython(seed_data),
    ]