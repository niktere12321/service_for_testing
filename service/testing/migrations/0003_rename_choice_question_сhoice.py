# Generated by Django 4.1.3 on 2022-12-07 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_alter_choice_true_or_false'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Choice',
            new_name='сhoice',
        ),
    ]
