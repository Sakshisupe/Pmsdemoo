# Generated by Django 3.1.3 on 2021-09-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0005_studentsresult_domain_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='miniproject_marks',
            field=models.FloatField(default=0),
        ),
    ]
