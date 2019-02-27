import pathlib

from polls import views


PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_get('/poll/{question_id}', views.poll, name='poll')
    app.router.add_get('/poll/{question_id}/results', views.results, name='results')
    app.router.add_post('/poll/{question_id}/vote', views.vote, name='vote')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
