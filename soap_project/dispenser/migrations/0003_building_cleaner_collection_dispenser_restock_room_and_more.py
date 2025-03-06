# Generated by Django 5.1.4 on 2025-03-06 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispenser', '0002_alter_soapdispenser_last_refill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('Building_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Floors', models.PositiveSmallIntegerField()),
                ('Address', models.CharField(max_length=32)),
                ('Phone_Number', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('Cleaner_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=16)),
                ('Surname', models.CharField(max_length=16)),
                ('DOB', models.DateField()),
                ('Address', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=64)),
                ('Phone_Number', models.BigIntegerField()),
                ('Salary', models.PositiveIntegerField()),
                ('Hire_Date', models.DateField()),
                ('Staff_Manager', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('Collection_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Collection_Date', models.DateField()),
                ('Collection_Time', models.PositiveSmallIntegerField()),
                ('Liquid_Level', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('Dispenser_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Dis_content', models.CharField(max_length=9)),
                ('Level_Liquid', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restock',
            fields=[
                ('Restock_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Soap_Amount_Bought', models.PositiveIntegerField()),
                ('Sanitizer_Amount_Bought', models.PositiveIntegerField()),
                ('soap_price', models.PositiveIntegerField()),
                ('sanitizer_Price', models.PositiveIntegerField()),
                ('Total', models.PositiveIntegerField()),
                ('Company', models.CharField(max_length=32)),
                ('Delivery_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Room_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Room_Type', models.CharField(blank=True, max_length=32, null=True)),
                ('Priority_Level', models.PositiveSmallIntegerField()),
                ('Building_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.building')),
            ],
        ),
        migrations.CreateModel(
            name='RoomRestock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.restock')),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('Rota_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Staff_Amount', models.PositiveIntegerField()),
                ('Rota_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('Shift_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Start_Time', models.PositiveSmallIntegerField()),
                ('Finish_Time', models.PositiveSmallIntegerField()),
                ('Overtime', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('Unsocial_Hours', models.CharField(max_length=5)),
                ('Cleaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.cleaner')),
                ('Rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.rota')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('Site_ID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('site_Name', models.CharField(max_length=32)),
                ('Address', models.CharField(max_length=64)),
                ('Phone_Number', models.BigIntegerField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Stockroom',
            fields=[
                ('Stockroom_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Soap_Amount', models.PositiveIntegerField()),
                ('Sanitizer_Amount', models.PositiveIntegerField()),
                ('Site_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.site')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('Supervisor_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=16)),
                ('Surname', models.CharField(max_length=16)),
                ('DOB', models.DateField()),
                ('Address', models.CharField(max_length=32)),
                ('Email', models.EmailField(max_length=32)),
                ('Phone_Number', models.BigIntegerField()),
                ('Salary', models.PositiveIntegerField()),
                ('Hire_Date', models.DateField()),
                ('Staff_Manager', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='SoapDispenser',
        ),
        migrations.AddField(
            model_name='collection',
            name='Dispenser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.dispenser'),
        ),
        migrations.AddField(
            model_name='dispenser',
            name='Room_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.room'),
        ),
        migrations.AddField(
            model_name='rota',
            name='Site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.site'),
        ),
        migrations.AddField(
            model_name='building',
            name='Site_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.site'),
        ),
        migrations.AddField(
            model_name='roomrestock',
            name='Stockroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.stockroom'),
        ),
        migrations.AddField(
            model_name='rota',
            name='Supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.supervisor'),
        ),
        migrations.AddField(
            model_name='restock',
            name='Supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispenser.supervisor'),
        ),
    ]
