# Generated by Django 2.1 on 2018-08-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptance', '0003_auto_20180809_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='image',
            field=models.ImageField(blank=True, help_text='выберите картинку для слайда', upload_to='sliders_images/', verbose_name='картинка для информации о нас'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, help_text='выберите картинку для слайда', upload_to='sliders_images/', verbose_name='картинка слайда'),
        ),
    ]
