from django.shortcuts import render
import requests, json, xmltodict
# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    
    if request.method == 'POST':
        cityname = request.POST.get('cityname')
        raw_data = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=&numOfRows=10&pageNo=1&searchCondition=DAILY&sidoName={cityname}'
        data = requests.get(raw_data).content
        xmlObject = xmltodict.parse(data)
        a = xmlObject['response']['body']['items']['item']
        air_list = []
        for air in a:
            air_list.append({'dataTime':air['dataTime'], 'cityName':air['cityName'],'so2Value':air['so2Value'], 'coValue':air['coValue'], 'no2Value':air['no2Value'], 'pm10Value':air['pm10Value'], 'pm25Value':air['pm25Value']})
        return render(request, 'result.html', {'air_list':air_list})
    else:
        return render(request, 'home.html')