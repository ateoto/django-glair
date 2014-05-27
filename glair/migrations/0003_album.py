# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glair', '0002_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', editable=False)),
                ('is_private', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False)),
                ('photos', models.ManyToManyField(to='glair.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
