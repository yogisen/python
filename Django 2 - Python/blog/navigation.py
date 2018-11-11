from django.urls import reverse_lazy

NAV_POSTS = 'Posts'
NAV_ABOUT = 'About'

NAV_ITEMS = (
    (NAV_POSTS, reverse_lazy('home')),
    (NAV_ABOUT, reverse_lazy('about')),
)


def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })

    return items
