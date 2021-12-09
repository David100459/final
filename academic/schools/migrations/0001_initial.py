# Generated by Django 3.2.7 on 2021-12-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firt_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='subject2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.student')),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.subject')),
            ],
        ),
    ]