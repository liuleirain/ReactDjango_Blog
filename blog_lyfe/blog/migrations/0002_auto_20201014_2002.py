# Generated by Django 3.1.2 on 2020-10-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('world', 'World'), ('environment', 'Environment'), ('technology', 'Technology'), ('culture', 'Design'), ('business', 'Business'), ('politics', 'Politics'), ('opinion', 'Opinion'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('travel', 'Travel')], default='world', max_length=50),
        ),
    ]
