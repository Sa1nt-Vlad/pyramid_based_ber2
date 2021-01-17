def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('order', '/order')
    config.add_route('list', '/list')
    config.add_route('burgers', '/burgers')
    config.add_route('done', '/done')
    config.add_route('access', '/access')
