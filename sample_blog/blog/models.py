from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    STATUS_CHOICES = (                                          # 公開状態の選択肢
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    ###### フィールド定義 ##################################################

    title = models.CharField(max_length=250)                     # 記事タイトル
    author = models.ForeignKey(User,                             # 記事筆者
                               on_delete=models.CASCADE,
                               related_name='blog_articles')
    body = models.TextField()                                    # 記事本文
    publish = models.DateTimeField(default=timezone.now)         # 公開日
    created = models.DateTimeField(auto_now_add=True)            # 記事作成日
    updated = models.DateTimeField(auto_now=True)                # 記事最終編集日
    status = models.CharField(max_length=10,                     # 公開状態
                              choices=STATUS_CHOICES,
                              default='draft')
    ########################################################################
    class Meta:
        """
        ModelクラスのMetaクラス。
        記事の並び順やレコードでかぶりがあってはいけないフィールドなど
        ここで指定できる
        公式ドキュメント：
            https://docs.djangoproject.com/ja/2.2/ref/models/options/
        """
        ordering = ('-publish',)                                 # 記事の並び順。新しいものから順に並ぶ。

    def __str__(self):
        """
        モデルを文字列として扱う際何を表示するかを定義するメソッド
        Djangoの管理サイトでの表示や
        print()
        で表示した時などはここが呼ばれる
        """
        return self.title