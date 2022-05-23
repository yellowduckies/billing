# Generated by Django 4.0.4 on 2022-05-22 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=None, max_length=254)),
                ('product_code', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(choices=[('emp', 'employee'), ('cus', 'customer')], default='cus', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=None, max_length=254)),
                ('quantity', models.IntegerField(default=0)),
                ('total_amount', models.FloatField(default=0)),
                ('invoice_date_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.myuser')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.product')),
            ],
        ),
    ]
