# Generated by Django 3.2.7 on 2022-10-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_courseinfo_course_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_userid', models.CharField(default=18201000, max_length=8, verbose_name='User ID')),
                ('payment_semester', models.CharField(db_column='Semester', default='1-1', max_length=50, verbose_name='Semester')),
                ('payment_installment', models.IntegerField(db_column='Installment', default=0, verbose_name='Installment')),
                ('payment_due', models.IntegerField(db_column='Due', default=0, verbose_name='Due')),
                ('payment_paid', models.IntegerField(db_column='Paid', default=0, verbose_name='Paid')),
                ('payment_status', models.CharField(db_column='Payment Status', default='Unpaid', max_length=10, verbose_name='Payment Status')),
            ],
            options={
                'db_table': 'Payment Info',
            },
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='course_id',
            field=models.CharField(db_column='Course ID', default='CSE 101', max_length=7, verbose_name='Course ID'),
        ),
    ]
