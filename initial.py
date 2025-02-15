import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Phone number')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('registration_date', models.DateField(default=datetime.date(2024, 4, 20), verbose_name='Registration date')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('qnt', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('creation_date', models.DateField(default=datetime.date(2024, 4, 20), verbose_name='Creation date')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.client')),
                ('products', models.ManyToManyField(to='myapp2.product')),
            ],
        ),
    ]