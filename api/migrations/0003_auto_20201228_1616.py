# Generated by Django 3.1.4 on 2020-12-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_snippet_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ['created']},
        ),
    ]
