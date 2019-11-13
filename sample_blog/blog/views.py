from django.shortcuts import render, get_object_or_404, Http404
from .models import Article



def article_list(request):
    """
    記事の一覧を表示する
    """
    articles = Article.published.all()             # 公開中の記事を全て取得
    return render(
        request,
        "blog/article/list.html",
        {"articles":articles}
    )

def article_detail(request, id):
    """
    記事の詳細を表示する
    """
    article = get_object_or_404(Article, id=id)     # 記事を取得、取得できなかった時点で404を返す

    return render(
        request,
        "blog/article/detail.html",
        {"article":article}
    )


def sample_view(request, id):
    try:
        article = Article.objects.get(id=id)
        return render(
        request,
        "blog/article/detail.html",
        {"article":article})

    except Article.DoesNotExist as e:
        return Http404