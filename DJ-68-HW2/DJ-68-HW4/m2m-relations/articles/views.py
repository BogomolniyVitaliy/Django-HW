from django.views.generic import ListView

from articles.models import Article


class ArticleList(ListView):
    template_name = 'articles/news.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-published_at').prefetch_related('scopes')
