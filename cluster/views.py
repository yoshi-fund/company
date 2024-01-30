from django.views import View
from django.shortcuts import render, redirect
from .forms import DataInputForm
import pandas as pd
import joblib


kmeans_model = joblib.load('/Users/anaiyoshikazu/real_data/Mirai-joblib/kmeans_model.pkl')

class ClusterView(View):
    form_class = DataInputForm
    template_name = 'cluster/data_input_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # データフレームの作成
            new_data = pd.DataFrame([data])
            
            # 既存のデータ前処理をそのまま使用
            # データ型の変換
            for column in new_data.columns:
                new_data[column] = pd.to_numeric(new_data[column], errors='coerce')

            # NaN値の処理（必要に応じて）
            new_data.fillna(0, inplace=True)
            
            # クラスタ予測
            cluster_label = kmeans_model.predict(new_data)

            # クラスタラベルに対応する名前のマッピング
            cluster_names = {
                0: '安定型(財務基盤強し)',
                1: '負債と建物を大量の所持',
                2: 'The 平均',
                3: '出来杉くん(優秀)'
            }

            # クラスターラベルを名前に変換
            cluster_name = cluster_names.get(cluster_label[0], '未知のクラスター')

            # 変換されたクラスター名をテンプレートに渡す
            return render(request, 'cluster/classification_result.html', {'cluster_name': cluster_name})
        
        return render(request, self.template_name, {'form': form})
