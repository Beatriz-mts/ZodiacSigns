# Generated by Django 3.2.25 on 2024-05-23 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('profession_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ZodiacSign',
            fields=[
                ('sign_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('zodiac_sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.zodiacsign')),
            ],
        ),
        migrations.CreateModel(
            name='FamousPerson',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.professions')),
                ('zodiac_sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.zodiacsign')),
            ],
        ),
    ]
