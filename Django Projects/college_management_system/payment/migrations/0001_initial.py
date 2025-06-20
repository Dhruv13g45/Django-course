# Generated by Django 5.1.6 on 2025-06-20 05:52

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_fee_structure', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('transaction_message', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_status', models.CharField(choices=[('failed', 'failed'), ('success', 'success')], max_length=100)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_payment', to='courses.course')),
            ],
        ),
    ]
