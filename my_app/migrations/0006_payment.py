# Generated by Django 4.0.4 on 2022-05-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_contact_delete_delete_delete_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
                ('productn', models.CharField(max_length=10)),
                ('productid', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=50)),
                ('cardn', models.CharField(max_length=20)),
                ('cardno', models.CharField(max_length=12)),
                ('expiry', models.DateField()),
                ('entercvv', models.CharField(max_length=3)),
            ],
        ),
    ]
