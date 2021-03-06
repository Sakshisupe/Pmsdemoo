# Generated by Django 3.1.3 on 2021-08-28 03:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0003_studentfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('miniproject_marks', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.projects')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.staffs')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.students')),
            ],
        ),
    ]
