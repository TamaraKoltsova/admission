# Generated by Django 2.1 on 2018-08-09 08:37

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=1028, null=True, verbose_name='имя услуги')),
                ('description', tinymce.models.HTMLField(blank=True, default=None, null=True, verbose_name='описание')),
                ('icon', models.CharField(blank=True, default=None, max_length=2046, null=True, verbose_name='иконка с fontawesome.com')),
                ('is_active', models.BooleanField(default=False, verbose_name='добавить на главную?')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
    ]
