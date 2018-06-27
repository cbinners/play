# Generated by Django 2.0.3 on 2018-06-25 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import util.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', util.fields.ShortUUIDField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together={('team', 'user')},
        ),
    ]
