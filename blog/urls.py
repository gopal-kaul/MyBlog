from django.urls import path
from .views import PostDetailView, PostListView
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug>',PostDetailView.as_view(), name='detail')
]