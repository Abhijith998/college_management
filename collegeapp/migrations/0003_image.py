# Generated by Django 4.2.10 on 2024-03-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_remove_students_course_alter_students_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
