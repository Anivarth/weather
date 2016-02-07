from bottle import run, route, debug, template, static_file, get, request
import requests, time, sys, pyinfodb


#alternate open_weather_app_id = ######
# Static Routes
"""@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')"""

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/images')
"""
@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')
"""
@route('/myip')
@route('/myip')
def myip():
    client_ip = request.headers['X-Real-IP']
    return ['Your IP is: {}\n'.format(client_ip)]

@route('/credits/')
@route('/credits')
def credits():
    return credits

@route('/')
@route('')
def weather():
    #client_ip = request.headers['X-Real-IP'] #Not work on local environment
    ip_lookup = pyinfodb.IPInfo('#######')
    ip = ip_lookup.get_city()#client_ip) #add client_ip in the parenthesis in real
    ip_address = ip['ipAddress']
    city = ip['cityName']
    country_code = ip['countryCode']
    zipcode = ip['zipCode']
    country = ip['countryName']
    region = ip['regionName']
    latitude = ip['latitude']
    longitude = ip['longitude']
    time_zone = ip['timeZone']
    payload = {'lat':latitude,'lon':longitude, 'units':'metric','appid':'#####'}
    weather_data = requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
    weather = weather_data.json()
    humidity = weather['main']['humidity']
    pressure = int(float(weather['main']['pressure'])*0.750062)
    avg_temp = int(round(weather['main']['temp']))
    max_temp = int(round(weather['main']['temp_max']))
    min_temp = int(weather['main']['temp_min'])
    description = weather['weather'][0]['description']
    cloud_cover = weather['clouds']['all']
    icon = weather['weather'][0]['icon']
    wind_direction = float(weather['wind']['deg'])
    if wind_direction>348.74 and wind_direction<11.26:
        wind_direction = "N"
    elif wind_direction>11.25 and wind_direction<33.76:
        wind_direction = 'NNE'
    elif wind_direction>33.75 and wind_direction<56.26:
        wind_direction = 'NE'
    elif wind_direction>56.25 and wind_direction<78.76:
        wind_direction = 'ENE'
    elif wind_direction>78.75 and wind_direction<101.26:
        wind_direction = 'E'
    elif wind_direction>101.25 and wind_direction<123.76:
        wind_direction = 'ESE'
    elif wind_direction>123.75 and wind_direction<146.26:
        wind_direction = 'SE'
    elif wind_direction>146.25 and wind_direction<168.76:
        wind_direction = 'SSE'
    elif wind_direction>168.75 and wind_direction<191.26:
        wind_direction = 'S'
    elif wind_direction>191.25 and wind_direction<213.76:
        wind_direction = 'SSW'
    elif wind_direction>213.75 and wind_direction<236.26:
        wind_direction = 'SW'
    elif wind_direction>236.25 and wind_direction<258.76:
        wind_direction = 'WSW'
    elif wind_direction>258.75 and wind_direction<281.26:
        wind_direction = 'W'
    elif wind_direction>281.25 and wind_direction<303.76:
        wind_direction = 'WNW'
    elif wind_direction>303.75 and wind_direction<326.26:
        wind_direction = 'NW'
    elif wind_direction>326.25 and wind_direction<348.75:
        wind_direction = 'NNW'
    wind_speed = weather['wind']['speed']
    local_time = time.time()
    return template('index.tpl', city=city, region = region, country_code = country_code,\
     avg_temp = avg_temp, description = description, min_temp = min_temp, max_temp=max_temp,\
     wind_speed = wind_speed, wind_direction = wind_direction, cloud_cover = cloud_cover,\
     time_zone = time_zone, icon=icon, humidity = humidity, pressure=pressure,\
      country = country, zipcode = zipcode, local_time = local_time ) 

@route('/faq')
@route('/faq/')
def faq():
    return template('faq.tpl')

debug(True)
run(reloader=True, host='localhost', port=8080)
