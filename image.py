import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', 'registration.py'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image of product'),
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateField(default=datetime.date(2024, 4, 20), verbose_name='Registration date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateField(default=datetime.date(2024, 4, 20), verbose_name='Creation date'),
        ),
    ]