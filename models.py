from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=60, default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    body_text = models.TextField('Category Content', blank=True, default='')
    
    class Meta:
        # makes it so that there cannot be 2 categories under a parent with the same slug
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"
    
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Page(models.Model):
    title = models.CharField(max_length = 60)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    permalink = models.CharField(max_length = 20, unique = True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank = True)
    # draft = models.BooleanField(default=False)
    # publish = models.DateField(auto_now = False, auto_now_add = False,)
    slug = models.SlugField(max_length=60, default='')
    
    def __str__(self):
        return self.title
    
    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb.insert(0, i)
            #breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
