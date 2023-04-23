from decouple import config
class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    TESTING = True

APP_SETTINGS=config.DevelopmentConfig
SECRET_KEY=gufldksfjsdf

from flask import Flask
from decouple import config
from flask_restx import Api
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the below APIs',
    license='MIT',
    contact='Ashutosh Krishna',
    contact_url='https://ashutoshkrris.tk',
    contact_email='contact@ashutoshkrris.tk',
    doc='/',
    prefix='/api/v1'
)

from core import api
from flask import jsonify
ns = api.namespace('/', description='Horoscope APIs')

from flask import Flask
from decouple import config
from flask_restx import Api
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the below APIs',
    license='MIT',
    contact='Ashutosh Krishna',
    contact_url='https://ashutoshkrris.tk',
    contact_email='contact@ashutoshkrris.tk',
    doc='/',
    prefix='/api/v1'
)
from core import routes
from core import app
if __name__ == '__main__':
    app.run()

ZODIAC_SIGNS = {
   "Aries": 1,
   "Taurus": 2,
   "Gemini": 3,
   "Cancer": 4,
   "Leo": 5,
   "Virgo": 6,
   "Libra": 7,
   "Scorpio": 8,
   "Sagittarius": 9,
   "Capricorn": 10,
   "Aquarius": 11,
   "Pisces": 12
    }

import requests
from bs4 import BeautifulSoup
def get_horoscope_by_day(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

def get_horoscope_by_week(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

def get_horoscope_by_month(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

parser_copy = parser.copy()
parser_copy.add_argument('day', type=str, required=True)

@ns.route('/get-horoscope/daily')
class DailyHoroscopeAPI(Resource):
    '''Shows daily horoscope of zodiac signs'''
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser_copy.parse_args()
        day = args.get('day')
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            if "-" in day:
                datetime.strptime(day, '%Y-%m-%d')
            horoscope_data = get_horoscope_by_day(zodiac_num, day)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.')
        except ValueError:
            raise BadRequest('Please enter day in correct format: YYYY-MM-DD')

        @ns.route('/get-horoscope/weekly')
        class WeeklyHoroscopeAPI(Resource):
            '''Shows weekly horoscope of zodiac signs'''

            @ns.doc(parser=parser)
            def get(self):
                args = parser.parse_args()
                zodiac_sign = args.get('sign')
                try:
                    zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
                    horoscope_data = get_horoscope_by_week(zodiac_num)
                    return jsonify(success=True, data=horoscope_data, status=200)
                except KeyError:
                    raise NotFound('No such zodiac sign exists')
                except AttributeError:
                    raise BadRequest('Something went wrong, please check the URL and the arguments.')

        @ns.route('/get-horoscope/monthly')
        class MonthlyHoroscopeAPI(Resource):
            '''Shows monthly horoscope of zodiac signs'''

            @ns.doc(parser=parser)
            def get(self):
                args = parser.parse_args()
                zodiac_sign = args.get('sign')
                try:
                    zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
                    horoscope_data = get_horoscope_by_month(zodiac_num)
                    return jsonify(success=True, data=horoscope_data, status=200)
                except KeyError:
                    raise NotFound('No such zodiac sign exists')
                except AttributeError:
                    raise BadRequest('Something went wrong, please check the URL and the arguments.')

