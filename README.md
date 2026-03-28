# color_blocks_app
カラーブロックを積み上げるアプリ。学習用に作成。

本アプリのフォルダ構造
color_block_app/
├── apps/
│   └── blocks/           # メインアプリ
│       ├── models.py     # Board / Block モデル
│       ├── views.py      # index + save API
│       ├── urls.py
│       ├── admin.py
│       └── templates/blocks/
│           ├── base.html
│           └── index.html
├── config/               # Django設定
│   ├── settings.py
│   └── urls.py
├── docker/
│   ├── Dockerfile        # Django用
│   ├── Dockerfile.tailwind
│   ├── entrypoint.sh     # マイグレーション自動実行
│   └── nginx.conf        # 本番用
├── static/
│   ├── css/input.css     # Tailwindエントリポイント
│   └── js/blocks.js      # JSロジック（実装予定）
├── requirements/
│   ├── base.txt          # Django + mysqlclient
│   ├── dev.txt           # + debug-toolbar
│   └── prod.txt          # + gunicorn
├── docker-compose.yml        # 開発用
├── docker-compose.prod.yml   # 本番用（nginx付き）
├── tailwind.config.js
└── .env.example