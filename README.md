slack botにニュースをまとめて投げてもらうプロジェクト

pipenv install
pipenv run start

main関数に処理の関数をimportすれば動くので、zenn,qiitaなどごとに別々のbranchでフォルダを作って、そこで作業し、動作確認したらpull requestを出すこと

pipenv にライブラリを追加したら
pipenv update
pipenv lock -r > requirements.txt
を実行すること

デプロイ先はAzure App Serviceで
start up scriptとして以下のコードを実行している。
gunicorn --bind=0.0.0.0 --timeout 600 app:flask_app

https://devcenter.heroku.com/ja/articles/python-gunicorn