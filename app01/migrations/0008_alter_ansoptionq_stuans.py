# Generated by Django 4.2.2 on 2023-06-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_ansoptionq_ansessayq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ansoptionq',
            name='stuAns',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
