# Generated by Django 4.2.5 on 2023-09-26 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_alter_lesson_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.product'),
        ),
    ]