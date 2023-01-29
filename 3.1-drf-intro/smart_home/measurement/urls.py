from django.urls import path

from .views import SensorAPIList, MeasurementAPIList, SensorAPIUpdate, SensorDetailAPIRetrieve

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view()),
    path('add_measure/', MeasurementAPIList.as_view()),
    path('change_sensor/<int:pk>/', SensorAPIUpdate.as_view()),
    path('sensor/<int:pk>/', SensorDetailAPIRetrieve.as_view()),
]
