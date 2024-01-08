# Generated by Django 4.2.5 on 2023-12-24 01:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0008_alter_company_業種"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="事業内容",
            field=models.TextField(default=1, verbose_name="事業内容"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="company",
            name="業種",
            field=models.IntegerField(
                choices=[
                    (1, "電気機器"),
                    (2, "情報通信"),
                    (3, "医薬品"),
                    (4, "輸送用機器"),
                    (5, "機械"),
                    (6, "卸売"),
                    (7, "小売"),
                    (8, "化学"),
                    (9, "サービス"),
                    (10, "銀行"),
                    (11, "精密機器"),
                    (12, "食料品"),
                    (13, "陸運"),
                    (14, "不動産"),
                    (15, "鉱業"),
                    (16, "ゴム製品"),
                    (17, "保険"),
                    (18, "その他製品"),
                    (19, "建設"),
                    (20, "鉄鋼"),
                ],
                null=True,
                verbose_name="業種",
            ),
        ),
    ]
