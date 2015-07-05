# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0002_auto_20150525_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='owner',
            field=models.ForeignKey(related_name='flights', default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
