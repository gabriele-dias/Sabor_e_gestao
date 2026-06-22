from django.contrib import admingit 
from .models import Produto

admin.site.register(Produto)


class ProdutoAdmin(admin.ModelAdmin):
    # Isso define quais campos aparecem na listagem do painel
    list_display = ('nome', 'preco', 'categoria') 
    # Adiciona uma barra de pesquisa lateral
    search_fields = ('nome',) 
    # Adiciona filtros laterais
    list_filter = ('categoria',)