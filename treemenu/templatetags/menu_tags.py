from django import template
from django.urls import NoReverseMatch, reverse
from treemenu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):

    items = MenuItem.objects.filter(menu__name=menu_name).select_related(
        "parent"
    )

    request = context.get("request")
    current_path = request.path
    current_item = None
    items_ids = {}

    for item in items:
        items_ids[item.id] = item
        if item.url == current_path:
            current_item = item

    current = current_item
    active_branch = []
    while current is not None:
        active_branch.append(current)
        current = items_ids.get(current.parent_id)

    def build_tree(parent=None):
        nodes = []
        # берём все элементы, у которых родитель — тот, что передан
        children = [item for item in items if item.parent == parent]

        for child in children:
            try:
                resolved_url = reverse(child.url)
            except NoReverseMatch:
                resolved_url = child.url
            child.resolved_url = resolved_url

            if child in active_branch:
                node_children = build_tree(child)
            else:
                node_children = []

            nodes.append({"item": child, "children": node_children})
        return nodes

    tree = build_tree()
    return {"menu": tree, "current_path": current_path}
