# Generated by Django 4.1.4 on 2022-12-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='status',
            field=models.CharField(choices=[('契約中', '契約中'), ('解約済み', '解約済み'), ('初期分析', '初期分析')], max_length=4, verbose_name='契約ステータス'),
        ),
    ]
