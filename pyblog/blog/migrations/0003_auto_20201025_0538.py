# Generated by Django 3.1.2 on 2020-10-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='https://via.placeholder.com/300', upload_to='images//')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
