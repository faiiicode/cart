from django.urls import path
from . import views
app_name='ecomapp'
urlpatterns = [
    path('',views.Allprodcat, name='Allprodcat'),
    path('<slug:c_slug>/',views.Allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productdet, name='product_det'),
    ]