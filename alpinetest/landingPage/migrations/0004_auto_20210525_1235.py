# Generated by Django 3.2 on 2021-05-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0003_remove_mobileview_top_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterAboutOurCompanySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='photos/home')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('button_name', models.CharField(blank=True, max_length=100)),
                ('button_hyperlink', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Follow_Your_Dream',
        ),
    ]
