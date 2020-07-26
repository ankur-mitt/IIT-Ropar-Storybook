# Generated by Django 3.0.6 on 2020-07-17 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_comment_usr_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='usr_pic',
        ),
        migrations.AddField(
            model_name='comment',
            name='usr_det',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='det', to='main.Generaldetails'),
        ),
    ]