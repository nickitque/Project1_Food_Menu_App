# Generated by Django 5.0.1 on 2024-01-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Falllocal.ca%2Ffood%2Fnorth-nb%2Fgrand-falls%2Fprepared-foods%2Fmaple-cones-2%2Ffeed%2F&psig=AOvVaw39e0UiMWIKaBQZ0eFnZ9tX&ust=1706009364306000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKibtqPy8IMDFQAAAAAdAAAAABAX', max_length=1000),
        ),
    ]
