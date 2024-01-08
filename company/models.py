from django.db import models
from django.utils import timezone


class Company(models.Model):

    CATEGORY = (
        (1, '電気機器'),
        (2, '情報通信'),
        (3, '医薬品'),
        (4, '輸送用機器'),
        (5, '機械'),
        (6, '卸売'),
        (7, '小売'),
        (8, '化学'),
        (9, 'サービス'),
        (10, '銀行'),
        (11, '精密機器'),
        (12, '食料品'),
        (13, '陸運'),
        (14, '不動産'),
        (15, '鉱業'),
        (16, 'ゴム製品'),
        (17, '保険'),
        (18, 'その他製品'),
        (19, '建設'),
        (20, '鉄鋼'),
        (21, '石油・石炭製品'),
        (22, '海運')
    )

    GROWTH = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆')
    )

    TREASURY_STABLE = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆')
    )

    会社名 = models.CharField('会社名', max_length=100,null=True)

    売上高 = models.FloatField('売上高3年平均', null=True)

    営業利益 = models.FloatField('営業利益3年平均', null=True)

    roe = models.FloatField('ROE', null=True)

    粗利率 = models.FloatField('粗利率', null=True)

    有形固定資産 = models.FloatField('有形固定資産', null=True)

    固定負債 = models.FloatField('固定負債', null=True)

    自己資本比率 = models.FloatField('自己資本比率', null=True)

    per = models.FloatField('per', null=True)

    pbr = models.FloatField('pbr', null=True)

    industry = models.IntegerField('業種',null=True, choices=CATEGORY)

    海外売上高比率 = models.FloatField('海外売上高比率', null=True)

    株価上昇率 = models.FloatField('3年の株価上昇率', null=True)

# 表示内容
    
    事業内容 = models.TextField('事業内容')
    
    会社ロゴ = models.ImageField('会社ロゴ', upload_to='company', null=True)
    
    平均年収 = models.IntegerField('平均年収', null=True)

    平均年齢 = models.FloatField('平均年齢', null=True)

    勤続年数 = models.FloatField('勤続年数', null=True)

    従業員数 = models.IntegerField('従業員数', null=True)

    持ち株 = models.CharField('持ち株', max_length=100, null=True)

    取締役報酬 = models.IntegerField('取締役_報酬', null=True)


    def __str__(self):
        return f'{self.会社名}' 

    # category = models.IntegerField('カテゴリー', choices=CATEGORY)

