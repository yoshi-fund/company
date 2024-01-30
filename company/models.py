from django.db import models
from django.utils import timezone


class Company(models.Model):

    CATEGORY = (
        (1, '電気機器'),
        (2, '情報・通信'),
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
        (22, '海運'),
        (23, 'ガラス・土石製品'),
        (24, 'その他金融業'),
        (25, '倉庫・運輸関連'),
        (26, 'その他金融'),
        (27, '金属製品'),
        (28, '精密機器'),
        (29, '繊維製品'),
        (30, 'パルプ・紙'),
        (31, '非鉄金属'),
        (32, '電気・ガス')
    )
    
    CLUSTER = (
        (0, '安定型(財務基盤強し)'),
        (1, '負債と建物を大量に所持'),
        (2, 'The 平均'),
        (3, '出来杉くん(優秀)'),
    )
    

    GROWTH = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆')
    )

    会社名 = models.CharField('会社名', max_length=100,null=True, blank=True)

    売上高 = models.FloatField('売上高3年平均', null=True, blank=True)

    営業利益 = models.FloatField('営業利益3年平均', null=True, blank=True)

    roe = models.FloatField('ROE', null=True, blank=True)

    有形固定資産 = models.FloatField('有形固定資産', null=True, blank=True)

    固定負債 = models.FloatField('固定負債', null=True, blank=True)

    自己資本比率 = models.FloatField('自己資本比率', null=True, blank=True)

    pbr = models.FloatField('pbr', null=True, blank=True)
    
    営業利益率 = models.FloatField('営業利益率', null=True, blank=True)

    株価上昇率 = models.FloatField('3年の株価上昇率', null=True, blank=True)
    
    粗利率 = models.FloatField('粗利率', null=True, blank=True)
    
    per = models.FloatField('per', null=True, blank=True)
    
    industry = models.IntegerField('業種',null=True, blank=True, choices=CATEGORY)


# Human
    
    会社ロゴ = models.ImageField('会社ロゴ', upload_to='company', null=True, blank=True)
    
    勤続年数 = models.FloatField('勤続年数', null=True, blank=True)
    
    平均年収 = models.IntegerField('平均年収', null=True, blank=True)

    平均年齢 = models.FloatField('平均年齢', null=True, blank=True)

    従業員数 = models.IntegerField('従業員数', null=True, blank=True)

    持ち株 = models.CharField('持ち株', max_length=100, null=True, blank=True)
    
    事業内容 = models.TextField('事業内容', null=True, blank=True)
    
    上場年数 = models.IntegerField('上場年数', null=True, blank=True)
    
    # 新たにフィールド追加
    
    人件費_純利益 = models.FloatField('純利益に占める人件費', null=True, blank=True)
    
    取締役報酬 = models.FloatField('取締役報酬', null=True, blank=True)
    
    従業員一人当たりの売上 = models.FloatField('従業員一人当たりの売上', null=True, blank=True)
    
    流動比率 = models.FloatField('流動比率', null=True, blank=True)
    
    研究開発売上比率 = models.FloatField('研究開発売上比率', null=True, blank=True)
    
    cluster = models.IntegerField('クラスター', choices=CLUSTER, null=True, blank=True)
    
    def __str__(self):
        return f'{self.会社名}' 

    # category = models.IntegerField('カテゴリー', choices=CATEGORY)


