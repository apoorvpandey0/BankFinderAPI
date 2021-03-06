# Generated by Django 3.0.8 on 2020-07-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifscfinder', '0009_auto_20200702_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='city',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='branch',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='district',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='ifsc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='state',
            field=models.TextField(),
        ),
    ]
