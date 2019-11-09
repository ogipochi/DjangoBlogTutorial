from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "author", 
        "publish",
        "status",)
    list_filter = ("publish","status",)          # フィルターを作成
    search_fields = ("title","body")             # 検索フォームの作成と検索対象の指定
    date_hierarchy = "publish"                   # 指定したフィールドの日時ごとにページを分けて管理
    ordering = ("publish","author","title")      # 一覧表示のデフォルトの並び順を指定


admin.site.register(Article, ArticleAdmin)