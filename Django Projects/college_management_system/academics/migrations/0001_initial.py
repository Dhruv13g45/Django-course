# Generated by Django 5.1.6 on 2025-06-20 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A+', 'Excellent'), ('A', 'Great'), ('B', 'Better'), ('C', 'Good'), ('D', 'Fail')], max_length=100)),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_result', to='courses.course')),
            ],
        ),
    ]
