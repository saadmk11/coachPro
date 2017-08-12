# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 12:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPaymentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_name', to='courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('remark', models.TextField(blank=True, null=True)),
                ('subject', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField(verbose_name='Student Age')),
                ('father_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('adhaar_number', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, default='students/img/default.png', height_field='height_field', null=True, upload_to='', verbose_name='profile picture', width_field='width_field')),
                ('height_field', models.IntegerField(default=600, null=True)),
                ('width_field', models.IntegerField(default=600, null=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='courses.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='studentpaymentdetail',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='students.Students'),
        ),
    ]
