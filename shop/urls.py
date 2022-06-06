from django.urls import include, path

from . import views

urlpatterns = [
    path("shop", views.Shop.shop, name="shop"),
    path("shop/<int:id>/", views.product_detail, name="product_detail"),
    path("sort_action", views.Shop.sortAction, name="sort_action"),
    path("sort_horror", views.Shop.sortHorror, name="sort_horror"),
    path("sort_adventure", views.Shop.sortAdventure, name="sort_adventure"),
    path("sort_shooter", views.Shop.sortShooter, name="sort_shooter"),
    path("sort_puzzle", views.Shop.sortPuzzle, name="sort_puzzle"),
    path("sort_indi", views.Shop.sortIndi, name="sort_indi"),
]
