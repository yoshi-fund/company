# Generated by Django 4.2.5 on 2023-12-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "company",
            "0004_company_会社ロゴ_company_勤続年数_company_平均年収_company_平均年齢_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="勤続年数",
            field=models.FloatField(null=True, verbose_name="勤続年数"),
        ),
        migrations.AlterField(
            model_name="company",
            name="持ち株",
            field=models.CharField(max_length=100, null=True, verbose_name="持ち株"),
        ),
    ]
