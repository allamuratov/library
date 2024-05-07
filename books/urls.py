from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, BookRetrieveUpdateDeleteApiView, BookListCreateApiView

urlpatterns = [
    path('', BookListApiView.as_view(),),
    path('<int:pk>/', BookDetailApiView.as_view()),
    path('books/', BookListCreateApiView.as_view()),
    path('booksupdel/<int:pk>/', BookRetrieveUpdateDeleteApiView.as_view()),
    path('<int:pk>/update/', BookUpdateApiView.as_view()),
    path('<int:pk>/delete/', BookDeleteApiView.as_view()),

]
