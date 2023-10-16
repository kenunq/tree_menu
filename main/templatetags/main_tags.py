from django import template
from django.utils.html import format_html

from main.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(name=None):
    menu = list(Menu.objects.filter(main_tree=name))
    html_parent = ''
    html_parent += get_parent(menu, menu[0].id)
    html = f'''
    <details>
        <summary><a href='{menu[0].url}'>{menu[0].text}</a></summary>
           <ul>
                {html_parent}
           </ul>
    </details>
           '''

    return format_html(html)


def get_parent(menu1, id=None):
    html_parent = ''
    menu = [i for i in menu1 if i.tree_id == id]
    for node in menu:
        if not [i for i in menu1 if i.tree_id == node.id]:
            html_parent += f"<li><a href='{node.url}'>{node.text}</a></li>"
        else:
            html_parent += f'''
            <li>
                <details>
                  <summary><a href="{node.url}">{node.text}</a></summary>
                    <ul>
                        {get_parent(menu1, node.id)}
                    </ul>
                </details>
            </li>
            '''

    return html_parent
