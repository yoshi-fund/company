from django.views import View
from django.shortcuts import render, redirect
from .forms import DataInputForm
import pandas as pd
import joblib

# モデルのロード
kmeans_model = joblib.load('/Users/anaiyoshikazu/yos/kmeans_model.pkl')

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
            
            # データ型の変換
            for column in new_data.columns:
                new_data[column] = pd.to_numeric(new_data[column], errors='coerce')

            # NaN値の処理（必要に応じて）
            new_data.fillna(0, inplace=True)
            
             # クラスタラベルに対応する名前のマッピング
            cluster_names = {
                0: '平均的な会社',
                1: '大量に建物を保有',
                2: '利益成長化け物',
                3: '出来杉くん(優秀)'
            }

            # クラスタ予測
            cluster_label = kmeans_model.predict(new_data)
            # クラスターラベルを名前に変換
            cluster_name = cluster_names.get(cluster_label[0], '未知のクラスター')
            # 変換されたクラスター名をテンプレートに渡す
            return render(request, 'cluster/classification_result.html', {'cluster_name': cluster_name})
        
        return render(request, self.template_name, {'form': form})
