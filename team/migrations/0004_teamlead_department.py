# Generated by Django 4.2.6 on 2023-11-06 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_kafedra'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='leaders/')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.position')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='leaders/')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.position')),
            ],
        ),
    ]
