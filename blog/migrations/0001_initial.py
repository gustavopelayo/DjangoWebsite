# Generated by Django 4.0.3 on 2022-05-12 19:24

from django.conf import settings
import django.contrib.auth.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django.views.generic.edit


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chargers', '0001_initial'),
        ('vehicles', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCreateView',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profile')),
            ],
            bases=(django.contrib.auth.mixins.LoginRequiredMixin, django.views.generic.edit.CreateView, 'users.profile'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourin', models.DateTimeField(default=django.utils.timezone.now)),
                ('hourout', models.DateTimeField(default=django.utils.timezone.now)),
                ('power', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chargers', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargers.chargers')),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
            options={
                'db_table': 'new_charge',
            },
        ),
    ]