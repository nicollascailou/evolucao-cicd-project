# Generated by Django 4.1.3 on 2022-11-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                ("id", models.BigIntegerField(primary_key=True)),
                ("name", models.CharField(max_length=9)),
                ("weight", models.BigIntegerField()),
                ("height", models.BigIntegerField()),
                ("base_experience", models.BigIntegerField()),
            ],
        ),
    ]