# Generated by Django 4.2.5 on 2024-01-02 08:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0015_company_取締役_company_社外役員"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="社外役員",
            new_name="それ以外の取締役",
        ),
    ]
