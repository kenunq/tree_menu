from django.db import models


class Menu(models.Model):
    text = models.CharField(max_length=50, null=True)
    lvl = models.IntegerField(default=0)
    tree_id_choices = [(0,'Нету')]
    tree_id = models.IntegerField('Parent', default=0, choices=tree_id_choices)
    main_tree_choices = [(' ', 'Нету')]
    main_tree = models.CharField('Menu', max_length=50, default='0', choices=main_tree_choices)
    url = models.URLField(default='http://127.0.0.1:8000/')


