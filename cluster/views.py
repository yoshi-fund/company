from django.views import View
from django.shortcuts import render
from .forms import DataInputForm
import pandas as pd
import joblib

# モデルとスケーラーのロード
kmeans_model = joblib.load('/Users/anaiyoshikazu/real_data/Mirai-joblib/kmeans_model.pkl')
scaler = joblib.load('/Users/anaiyoshikazu/real_data/Mirai-joblib/scaler.pkl')

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

            # Djangoビュー内でのデータ処理
            data = form.cleaned_data
            feature_names = ['売上高', '営業利益', 'roe', '有形固定資産', '固定負債', '自己資本比率', 'pbr', '営業利益率', '株価上昇率']
            new_data = pd.DataFrame([data], columns=feature_names)


            # データ型の変換とNaN値の処理
            for column in new_data.columns:
                new_data[column] = pd.to_numeric(new_data[column], errors='coerce')
            new_data.fillna(0, inplace=True)

            # 変換前後のデータを出力
            print("変換前のデータ:")
            print(new_data)
            new_data_scaled = scaler.transform(new_data)
            print("変換後のデータ:")
            print(new_data_scaled)

            # クラスタ予測
            cluster_label = kmeans_model.predict(new_data_scaled)

            # クラスタラベルに対応する名前のマッピング
            cluster_names = {
                0: '安定型(財務基盤強し)',
                1: '負債と建物を大量に所持',
                2: 'The 平均',
                3: '出来杉くん(優秀)'
            }

            # クラスターラベルを名前に変換
            cluster_name = cluster_names.get(cluster_label[0], '未知のクラスター')

            # 変換されたクラスター名をテンプレートに渡す
            return render(request, 'cluster/classification_result.html', {'cluster_name': cluster_name})
        
        return render(request, self.template_name, {'form': form})
