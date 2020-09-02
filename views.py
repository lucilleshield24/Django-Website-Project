from django.shortcuts import render, get_object_or_404
from . models import Page, Category
import numpy as np

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    breadcrumbs_link = pg.get_cat_list()
    #category_name = [' '.join(i.split('/')[-1].split('/')) for i in breadcrumbs_link]
    #breadcrumbs_link = [i.split('/') for i in breadcrumbs_link]
    #breadcrumbs_link = np.unique(breadcrumbs_link)
    #breadcrumbs = zip(breadcrumbs_link, category_name)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'breadcrumbs': breadcrumbs_link,
        }
    return render(request, 'pages/page.html', context)

def show_category(request, hierarchy=None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    for slug in category_slug:
          if slug in all_slugs:
              parent = get_object_or_404(Category, slug=slug)
          else:
              instance = get_object_or_404(Page, slug=slug)
              breadcrumbs_link = instance.get_cat_list()
              category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
              breadcrumbs = zip(breadcrumbs_link, category_name)
              return render(request, "pages/page.html", {'breadcrumbs': breadcrumbs})
    return render(request, "categories.html", {'title': parent, 'content': parent.body_text, 'page_set': parent.page_set.all(), 'sub_categories': parent.children.all()})

def recent(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        }
    return render(request, 'pages/recentposts.html', context)
