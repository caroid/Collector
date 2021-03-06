from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^itemlist/$', views.CatalogListView.as_view(), name='item_list'),
    url(r'^itemdetails/(?P<pk>\d+)/', views.ItemDetailView.as_view(), name="item_detail"),
    url(r'^createitem/$', views.CreateItem.as_view(), name="create_item"),
    url(r'^edititem/(?P<pk>\d+)/', views.EditItem.as_view(), name="edit_item"),
    url(r'^removeitem/(?P<pk>\d+)/', views.RemoveItem.as_view(), name="remove_item")
]
