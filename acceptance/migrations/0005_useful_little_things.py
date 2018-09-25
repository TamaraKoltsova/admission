# Generated by Django 2.1 on 2018-08-09 09:12

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptance', '0004_auto_20180809_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='useful_little_things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=1028, null=True, verbose_name='имя услуги')),
                ('description', tinymce.models.HTMLField(blank=True, default=None, null=True, verbose_name='описание')),
                ('icon', models.CharField(blank=True, default=None, max_length=2046, null=True, verbose_name='иконка с fontawesome.com например <i class="fas fa-briefcase-medical"></i>')),
                ('is_active', models.BooleanField(default=False, verbose_name='добавить на главную?')),
            ],
            options={
                'verbose_name': 'полезная мелочь на сайте',
                'verbose_name_plural': 'полезные мелочи на сайте',
            },
        ),
    ]
