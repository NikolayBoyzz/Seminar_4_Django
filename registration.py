import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', 'initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateField(default=datetime.date(2024, 4, 6), verbose_name='Registration date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='order', to='myapp2.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateField(default=datetime.date(2024, 4, 6), verbose_name='Creation date'),
        ),
    ]