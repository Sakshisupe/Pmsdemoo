# Generated by Django 3.1.3 on 2021-08-28 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0004_studentsresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsresult',
            name='domain_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pms.domains'),
            preserve_default=False,
        ),
    ]