from django.urls import path
from . import views

urlpatterns = [
      path('',views.Indexpage.as_view(), name='index'),
      path('contact/',views.ContactPage.as_view(), name='contact'),

      path('article/', views.SingleArticleAPIview.as_view(), name='single_article'),
      path('article/all/', views.AllArticleAPIview.as_view(), name='all_articles'),
      path('article/search/', views.SearchArticleAPIview.as_view(), name='search_article'),
      path('article/submit/', views.SubmitArticleAPIview.as_view(), name='submit_article'),
      path('article/update-cover/', views.UpdateArticleAPIview.as_view(), name='update_article'),
      path('article/delete/', views.DeleteArticleAPIview.as_view(), name='delete_article'),



]