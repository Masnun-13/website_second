# Generated by Django 3.2.7 on 2022-10-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20220308_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courseinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_userid', models.CharField(default=18201000, max_length=8, unique=True, verbose_name='User ID')),
                ('course_semester', models.CharField(db_column='Semester', default='1-1', max_length=50, verbose_name='Semester')),
                ('course_id', models.CharField(db_column='Course ID', default='CSE 101', max_length=7, unique=True, verbose_name='Course ID')),
                ('course_title', models.CharField(db_column='Course Title', default='Computer Fundamentals', max_length=50, verbose_name='Course Title')),
            ],
            options={
                'db_table': 'Course Info',
            },
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_occupation',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.CharField(db_column='user', default='JohnDoe', max_length=20, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_semester',
            field=models.CharField(db_column='Semester', default='1-1', max_length=50, verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]