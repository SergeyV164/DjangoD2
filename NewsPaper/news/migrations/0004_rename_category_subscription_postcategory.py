# Generated by Django 5.0.3 on 2024-04-12 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='category',
            new_name='postCategory',
        ),
    ]