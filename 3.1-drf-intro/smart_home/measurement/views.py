# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# 1. Создать датчик. Указываются название и описание датчика.
# http://127.0.0.1:8000/api/sensors/ post
# example body
#    {
#        "id": 3,
#        "name": "Sensor 3",
#       "description": "Туалет"
#    }
# 4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.
# http://127.0.0.1:8000/api/sensors/ get
class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 3. Добавить измерение. Указываются ID датчика и температура
# http://127.0.0.1:8000/api/add_measure/ post
# example body
# {
#         "id": 3,
#         "measuring_temperature": 22,
#         "measurement": 3
#     }
class MeasurementAPIList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# 2. Изменить датчик. Указываются название и/или описание.
# http://127.0.0.1:8000/api/change_sensor/<pk>/
# example body
#     {
#         "name": "Sensor 1",
#         "description": "Прихожая, входная дверь"
#     }
class SensorAPIUpdate(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# 5. Получить информацию по конкретному датчику.
# Выдается полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем
# http://127.0.0.1:8000/api/sensor/<pk>/
class SensorDetailAPIRetrieve(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
