# Generated by Django 4.2.1 on 2024-09-12 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogserviceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('send_data', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ManyToManyField(related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlockedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_by_users', to=settings.AUTH_USER_MODEL)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocking_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]