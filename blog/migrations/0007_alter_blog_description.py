# Generated by Django 4.0.1 on 2022-03-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_textar_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=248),
        ),
    ]
