# Generated by Django 3.0.8 on 2020-07-02 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifscfinder', '0002_auto_20200702_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='name',
            new_name='bank_name',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='micr_code',
        ),
    ]
