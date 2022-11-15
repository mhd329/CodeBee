# Generated by Django 3.2.13 on 2022-11-15 10:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ('limits', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(2)])),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('tag', models.CharField(blank=True, max_length=50)),
                ('categorie', models.CharField(max_length=30)),
                ('study_type', models.CharField(max_length=30)),
                ('deadline', models.DateTimeField()),
                ('location_type', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('X', models.CharField(max_length=20, null=True)),
                ('Y', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('isactive', models.BooleanField(default=True)),
                ('host', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudyDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_at', models.DateTimeField()),
                ('study_end', models.DateTimeField()),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studydate', to='reviews.study')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.study')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.BooleanField(default=False)),
                ('joindate', models.DateTimeField(auto_now=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted', to='reviews.study')),
                ('users', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
