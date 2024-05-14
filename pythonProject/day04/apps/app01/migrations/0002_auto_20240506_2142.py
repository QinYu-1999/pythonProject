# Generated by Django 3.2 on 2024-05-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ct_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='up_date',
            field=models.DateField(null=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=16, verbose_name='姓名'),
        ),
    ]