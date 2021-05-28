# Generated by Django 3.1.7 on 2021-05-27 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0025_auto_20210528_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelikeandunlike',
            name='blog_like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_like_blog', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='articlelikeandunlike',
            name='user_like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
