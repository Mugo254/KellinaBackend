# Generated by Django 4.0.2 on 2022-02-22 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.items')),
            ],
        ),
    ]