from django.urls import path
from . import views


urlpatterns =patterns('',
  path('', views.index, name="root"),
  path('survey_load/', views.load_survey, name="load-survey"),
  path('survey/(?P<survey_id>\d+)/', views.survey_view, name="survey-detail"),
  path('admin_login/', views.admin_login, name="admin-login"),
  path('admin_panel/', views.admin_panel, name="admin-panel"),
  path('admin_panel/survey_delete/', views.survey_delete, name="admin-survey-delete"),
  path('admin_panel/survey/(?P<survey_id>\d+)/', views.admin_answers, name="answer-detail"),
  path('admin_panel/survey_create_view/', views.survey_create_view, name="admin-survey-create-view"),
  path('admin_panel/survey_create/', views.survey_create, name="admin-survey-create"),
  path('admin_panel/question_add_view/', views.question_add_view, name="admin-question-add-view"),
  path('admin_panel/question_add/', views.question_add, name="admin-question-add"),
  path('admin_panel/choice_add_view/', views.choice_add_view, name="admin-choice-add-view"),
  path('admin_panel/choice_add/', views.choice_add, name="admin-choice-add"),
  path('admin_panel/survey_delete/', views.survey_delete, name="admin-survey-delete"),
)