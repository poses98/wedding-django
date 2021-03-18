from django.urls import path, include
from wedding import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirmacion/', views.confirmacion_create_view,name='confirmacion'),
    path('confirmacion/search/', views.confirmacion_search_view,name='confirmacion_search'),
    path('confirmacion/edit/', views.confirmacion_edit_view,name='confirmacion_edit'),
    path('masinformacion/',views.SitiosInteresListView.as_view(), name='masinformacion'),
    path('golf/',views.golf_view,name='golf'),
    path('golf/inscripcion/',views.inscripcion_create_view,name='inscripcion_campeonato'),
    path('inscripcion/realizada',views.SuccessForm,name='form_success'),
    path('mensaje/',views.best_wishes_create_view,name='form_best_wishes'),
    path('acceso/',views.password_view,name='password'),

]