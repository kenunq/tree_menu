from django.contrib import admin

from main.models import Menu


def set_tree_id_choices():
    all_objects = Menu.objects.all()
    for object in all_objects:
        main_tree_tuple = (object.text, object.text)
        tree_id_tuple = (object.id, object.text)
        if object.lvl == 0:
            if not main_tree_tuple in Menu.main_tree_choices:
                Menu.main_tree_choices.append((object.text, object.text))
                Menu.tree_id_choices.append((object.id, object.text))
        else:
            if not tree_id_tuple in Menu.tree_id_choices:
                Menu.tree_id_choices.append((object.id, object.text))


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    try:
        set_tree_id_choices()
    except Exception as e:
        print(e)

    readonly_fields = ('id',)
    list_display = ('text', 'id', 'tree_id')
    ordering = ['-main_tree', 'lvl', 'text']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)

        set_tree_id_choices()
        form.base_fields['tree_id'].choices = Menu.tree_id_choices
        form.base_fields['main_tree'].choices = Menu.main_tree_choices
        return form

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.url = obj.url + str(obj.pk)
        if obj.main_tree == ' ':
            obj.main_tree = obj.text
        obj.save()


