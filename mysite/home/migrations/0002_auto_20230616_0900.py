# Generated by Django 3.2.3 on 2023-06-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='pcontactus',
            name='content',
            field=models.CharField(default='Nothing here', max_length=200),
        ),
    ]
