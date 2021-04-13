
from django.urls import path
from . import views

urlpatterns = [
	path('suma/<int:num1>/<int:num2>', views.suma, name='suma'),
	path('resta/<int:num1>/<int:num2>', views.resta, name='resta'),
	path('multi/<int:num1>/<int:num2>', views.multi, name='multi'),
	path('div/<int:num1>/<int:num2>', views.div, name='div'),
]
