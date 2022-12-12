from django.contrib import admin

from .models import Category, Post


@admin.action(description='опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='убрать из публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


class ManagerPanel(admin.AdminSite):
    site_header = 'Администрирование DJANGO для менеджеров'
    site_title = 'DJANGO для менеджеров'           # название на вкладке
    index_title = 'Управление сайтом'
    site_url = 'manager/' # куда ведет открытие из панели
    # enable_nav_sidebar = True
    # empty_value_display = как отображаются пустые поля во всем сайте


manager = ManagerPanel(name='manager')


# class PostInline(admin.TabularInline):
#     model = Post
    # fk_name =
    # verbose_name =                   переодпределить для отображения этого режима
    # verbose_name_plural =


class PostInline(admin.StackedInline):
    model = Post
# можно редартировать посты, номенклатуру и т.п.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    prepopulated_fields = {
        'slug': ('name', )
    }
    actions = (make_published, make_unpublished)
    inlines = (PostInline, )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('descr', )
    search_help_text = f'Поиск по полю "{search_fields[0]}"'

    # actions_on_top = True
    # actions_on_bottom = True
    #
    # actions_selection_counter = True
    list_display = ('id', 'date', 'title', )
    readonly_fields = ('date_created', )
    ordering = ('is_published', '-date_created')
    list_display_links = ('id', )
    # list_editable = ('title', )
    list_filter = ('is_published', 'date_created', )
    # date_hierarchy = 'date_created'
    # exclude = ['date_created']      нельзя вместе с "fieldsets" - ошибка
    fieldsets = (
        (
            'Основное',
            {
                'fields': ['title', 'descr'],
                'description': 'Осноные значения'
            }
        ),
        (
            'Дополнительное',
            {
                'fields': ['is_published', 'slug', 'category', 'author']
            }
        )
    )
    prepopulated_fields = {
        'slug': ('title', )
    }





# admin.site.register(Category)
# admin.site.register(Post)

# Register your models here.
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)


manager.register(Category, CategoryAdmin)
manager.register(Post, PostAdmin)



