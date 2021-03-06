# Generated by Django 3.2.9 on 2021-12-02 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_alter_orderbookuser_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratebookuser',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_book_user_book', to='myapp.book'),
        ),
        migrations.AlterField(
            model_name='ratebookuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_book_user_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
