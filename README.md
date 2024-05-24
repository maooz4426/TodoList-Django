# TodoList-Django

## 環境変数の設定

このプロジェクトでは、以下の環境変数を設定する必要があります。

`.env`
```.env
SECRET_KEY= 'your-secret-key-here'
DATABASE_NAME= tododb
DATABASE_USER= admin
DATABASE_PASSWORD= todops
DATABASE_HOST= db
DATABASE_PORT = 5432 #PostgreSQLなら
LANG = ja_JP.utf8
LC_CTYPE =  ja_JP.utf8
```

シークレットキーは以下のコマンドで発行してください
```
docker compose run web python manage.py shell
>>>from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```
## コンテナの起動
コンテナイメージの作成
```
docker compose build
```

コンテナの起動
```
docker compose up
```

http://localhost:8000/

