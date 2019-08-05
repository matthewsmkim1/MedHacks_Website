# Generated by Django 2.0.4 on 2019-07-10 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import travel.formatcheck


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelAppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(default='NA', max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('tr_essay', models.CharField(default='-', max_length=300)),
                ('contingency', models.CharField(max_length=5)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('type_reim', models.CharField(default='-', max_length=5)),
                ('first_name', models.CharField(default='-', max_length=50)),
                ('last_name', models.CharField(default='-', max_length=50)),
                ('permanent_address1', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('permanent_address2', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('permanent_city', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('permanent_state', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('permanent_zip', models.CharField(blank=True, default='-', max_length=15, null=True)),
                ('travel_date_from', models.DateTimeField(blank=True, null=True)),
                ('travel_date_to', models.DateTimeField(blank=True, null=True)),
                ('travel_location_city', models.CharField(default='-', max_length=50)),
                ('travel_location_state', models.CharField(default='NA', max_length=50)),
                ('receipt_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('reimburse_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('receipt_file', travel.formatcheck.ContentTypeRestrictedFileField(default='-', upload_to='receipts')),
                ('policy_check', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]