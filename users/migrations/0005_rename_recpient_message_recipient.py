# Generated by Django 5.1.2 on 2024-11-16 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recpient',
            new_name='recipient',
        ),
    ]