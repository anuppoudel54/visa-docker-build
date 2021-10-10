# Generated by Django 3.2 on 2021-06-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaPage', '0006_alter_visadetailsdescription_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaTopSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/visa')),
                ('title', models.TextField(blank=True, max_length=150)),
            ],
        ),
    ]