# Generated by Django 3.1.2 on 2020-10-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201025_0538'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/300', upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_slug',
            field=models.SlugField(default='image', max_length=200, unique=True),
        ),
    ]
