# Generated by Django 4.0.3 on 2022-05-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chargers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(choices=[('Maia', 'Maia'), ('Chaves', 'Chaves'), ('Porto', 'Porto')], default='Maia', max_length=350)),
                ('chargepower', models.IntegerField()),
                ('shelly', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'chargers',
            },
        ),
    ]