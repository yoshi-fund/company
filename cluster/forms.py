from django import forms

class DataInputForm(forms.Form):
    売上高成長率平均 = forms.FloatField(label='売上高成長率3年平均')
    営業利益率平均 = forms.FloatField(label='営業利益率3年平均')
    ROE = forms.FloatField(label='ROE')
    粗利率 = forms.FloatField(label='粗利率')
    有形固定資産_純資産 = forms.FloatField(label='有形固定資産 / 純資産')
    固定負債_純資産 = forms.FloatField(label='固定負債 / 純資産')
    自己資本比率 = forms.FloatField(label='自己資本比率')
    PBR = forms.FloatField(label='PBR')
    株価上昇率_3年 = forms.FloatField(label='株価上昇率(2020~2023)')
