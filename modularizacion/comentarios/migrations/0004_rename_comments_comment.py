# Generated by Django 4.1.7 on 2023-03-23 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_signature'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]