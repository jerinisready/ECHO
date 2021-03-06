# coding=utf-8
from geopy.geocoders import Nominatim
import re
import time
import oauth2
import datetime
from django.core.management.base import BaseCommand, CommandError
import json
from website.models import Query,SocialData,FbQueryMapper,SocialDataQuery
from textblob import TextBlob
class Command(BaseCommand):


    def handle(self, *args, **options):
        CONSUMER_KEY = "3oZUcRXGDnAFTw8yU2tnXWYPv"
        CONSUMER_SECRET = "OO0etJpFZWjNWI209IOjtgkHNA35gXceZ3iSuBb0vo1iBT7yGm"
        TOKEN = "2561013228-vvbdtCs3V1VBiaJ3d1bFfYjZoJmJVv9sjJUDaFG"
        TOKEN_SECRET = "LFJGXybQEcvX0jzDxeRsLICk4fMS1nayXm5kcAHRvt7Gf"
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=TOKEN, secret=TOKEN_SECRET)
        client = oauth2.Client(consumer, token)
        q = Query.objects.filter(is_active=True)
        for query in q:

            querys = str(query.query)
            print querys
            q_id= query.id
            print q_id
            since = datetime.datetime.now() - datetime.timedelta(days=7)
            d= since.date()
            url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + querys+ '&since='+ str(d)
            resp,content = client.request(url, method="GET", body="", headers= None)
            data_set= json.loads(content)
            for data in data_set["statuses"] :
                location= Location_parser(data["user"]["location"])
                ts = time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.strptime(data['created_at'],
                                   '%a %b %d %H:%M:%S +0000 %Y'))
                print "\n"
                print "\n"
                print "date    : ", ts
                print "USER    : ", data["user"]["screen_name"]
                print "location    : ", location
                print "Retweet count    : ", data ["retweet_count"]
                print "favourite count    : ", data["favorite_count"]
                print "Message : ", data["text"]
                print "link : ", "https://twitter.com/"+data["user"]["screen_name"]+"/status/"+data["id_str"]
                text = data["text"]
                blob = TextBlob(text)
                i = 0
                sentiment = 0
                for sentence in blob.sentences:
                    sentiment = sentiment + sentence.sentiment.polarity
                    i = i + 1
                sentiment = sentiment / i
                if (sentiment >= -0.1 and sentiment <= 0.1):
                    senti = "Nuetral"
                elif (sentiment > 0.5):
                    senti = "HighPositive"
                elif (sentiment > 0.0 and sentiment <= 0.5):
                    senti = "Positive"
                elif (sentiment > -0.5 and sentiment < 0.0):
                    senti = "Negative"
                else:
                    senti = "HighNegative"
                print senti
                c = SocialData(message=data["text"],
                               created_date=ts,
                               sentiment=senti,
                               source="TWITTER",
                               love_count=0,
                               haha_count=0,
                               sad_count=0,
                               wow_count=0,
                               angry_count=0,
                               location=location,
                               fbquerymapper_id=2,
                               like_count=data["favorite_count"],
                               link="https://twitter.com/"+data["user"]["screen_name"]+"/status/"+data["id_str"],
                               shares=data["retweet_count"],
                               thankful_count=0,
                               user_name= data["user"]["screen_name"],
                               )

                try:
                    c.save();
                    ("Continue...")
                except:
                    pass

def Location_parser(location):
    country_code = \
        {'Afghanistan': 'AF', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS',
                                'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ',
                                'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW',
                                'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS',
                                'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE',
                                'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT',
                                'Bolivia, Plurinational State of': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ',
                                'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR',
                                'British Indian Ocean Territory': 'IO', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG',
                                'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM',
                                'Canada': 'CA', 'Cape Verde': 'CV', 'Cayman Islands': 'KY',
                                'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN',
                                'Christmas Island': 'CX', 'Cocos (Keeling) Islands': 'CC', 'Colombia': 'CO',
                                'Comoros': 'KM', 'Congo': 'CG', 'Congo, the Democratic Republic of the': 'CD',
                                'Cook Islands': 'CK', 'Costa Rica': 'CR', 'Country name': 'Code', 'Croatia': 'HR',
                                'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czech Republic': 'CZ',
                                "Côte d'Ivoire": 'CI', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM',
                                'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV',
                                'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET',
                                'Falkland Islands (Malvinas)': 'FK', 'Faroe Islands': 'FO', 'Fiji': 'FJ',
                                'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF',
                                'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE',
                                'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL',
                                'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG',
                                'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT',
                                'Heard Island and McDonald Islands': 'HM', 'Holy See (Vatican City State)': 'VA',
                                'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'ISO 3166-2:GB': '(.uk)',
                                'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran, Islamic Republic of': 'IR',
                                'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT',
                                'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ',
                                'Kenya': 'KE', 'Kiribati': 'KI', "Korea, Democratic People's Republic of": 'KP',
                                'Korea, Republic of': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG',
                                "Lao People's Democratic Republic": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB',
                                'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI',
                                'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO',
                                'Macedonia, the former Yugoslav Republic of': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW',
                                'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT',
                                'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU',
                                'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia, Federated States of': 'FM',
                                'Moldova, Republic of': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME',
                                'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM',
                                'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL',
                                'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE',
                                'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'Northern Mariana Islands': 'MP',
                                'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW',
                                'Palestine, State of': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY',
                                'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT',
                                'Puerto Rico': 'PR', 'Qatar': 'QA', 'Romania': 'RO', 'Russian Federation': 'RU',
                                'Rwanda': 'RW', 'Réunion': 'RE', 'Saint Barthélemy': 'BL',
                                'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN',
                                'Saint Lucia': 'LC', 'Saint Martin (French part)': 'MF',
                                'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC',
                                'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA',
                                'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL',
                                'Singapore': 'SG', 'Sint Maarten (Dutch part)': 'SX', 'Slovakia': 'SK',
                                'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA',
                                'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS',
                                'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR',
                                'Svalbard and Jan Mayen': 'SJ', 'Swaziland': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH',
                                'Syrian Arab Republic': 'SY', 'Taiwan, Province of China': 'TW', 'Tajikistan': 'TJ',
                                'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL',
                                'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT',
                                'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC',
                                'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates': 'AE',
                                'United Kingdom': 'GB', 'United States': 'US',
                                ' United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'Uzbekistan': 'UZ',
                                'Vanuatu': 'VU', 'Venezuela, Bolivarian Republic of': 'VE', 'Viet Nam': 'VN',
                                'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI',
                                'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM',
                                'Zimbabwe': 'ZW', 'Åland Islands': 'AX'
        }

    final_country_code = {}
    for k in country_code.keys():
        final_country_code.update({k.lower(): country_code[k]})
    code = None
    for k in final_country_code:
        if re.findall(k, location, re.M | re.I):
            code = final_country_code[k]
            break
    try :

        if not code:
            geolocator = Nominatim()
            cnv_location = geolocator.geocode(location)
            if cnv_location:
                cnv_location = geolocator.reverse((cnv_location.latitude, cnv_location.longitude))
                address = cnv_location.raw.get('address')
            if address:
                code = address.get('country_code')
                code = code.upper() if code else None
    except :
        code= 'None'
    return code