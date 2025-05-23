# Generated by Django 5.2.1 on 2025-05-19 07:27

import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(choices=[(1, 'POOR'), (2, 'FAIR'), (3, 'AVARAGE'), (4, 'GREAT'), (5, 'EXCELLENT')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[400, None], upload_to='rooms/')),
                ('image_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
