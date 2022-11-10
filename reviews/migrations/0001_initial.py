# Generated by Django 3.2.13 on 2022-11-10 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limits', models.IntegerField(default=4)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('tag', models.CharField(max_length=20)),
                ('categorie', models.CharField(max_length=30)),
                ('study_type', models.CharField(max_length=30)),
                ('deadline', models.DateField()),
                ('location_type', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('X', models.CharField(max_length=20, null=True)),
                ('Y', models.CharField(max_length=20, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('host', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('joined_user', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.BooleanField(default=False)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.study')),
                ('users', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
