from django.core.management.base import BaseCommand, CommandError
from textblob import TextBlob
from website.models import SocialData,FbQueryMapper

class Command(BaseCommand):

        def handle(self, *args, **options):
            q= FbQueryMapper.objects.all()
            for fbquerymapper in q :
                import facebook, datetime
                token = "741011062769592|tLH6FvFILJ0oOqoHGUKouycRuR4"
                since = datetime.datetime.now() - datetime.timedelta(days=14)
                d = since.date()
                graph = facebook.GraphAPI(token)
                data_set = graph.request(str(fbquerymapper.page)+
                '/posts?fields=description,message,created_time,shares,link,from,'                                      
                ' type,comments.summary(true),'
                'reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),'
                'reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),'
                'reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),'
                'reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),'
                'reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),'
                'reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry),'
                'reactions.type(THANKFUL).limit(0).summary(total_count).as(reactions_thankful),'                                       
                ' reactions.summary(true)&limit=50&since=' + str(d))

                data_set = data_set['data']
                for data in data_set:
    	            print "\n"
    	            print "\n"
    	            print "USER    : ",data["from"]["name"]
                    print "SHARES  : ",data["shares"]["count"]
    	            print "like   : ",data["reactions_like"]["summary"]["total_count"]
                    print "Love   : ", data["reactions_love"]["summary"]["total_count"]
                    print "wow   : ", data["reactions_wow"]["summary"]["total_count"]
                    print "haha   : ", data["reactions_haha"]["summary"]["total_count"]
                    print "sad   : ", data["reactions_sad"]["summary"]["total_count"]
                    print "angry   : ", data["reactions_angry"]["summary"]["total_count"]
                    print "thankful   : ", data["reactions_thankful"]["summary"]["total_count"]
    	            print "Message : ",data["message"]
    	            print "date    : ",data["created_time"]
    	            print "id    : ",data['id']
                    text = data["message"]
                    blob = TextBlob(text)
                    i=0
                    sentiment=0
                    for sentence in blob.sentences:
                        sentiment=sentiment+sentence.sentiment.polarity
                        i=i+1
                    sentiment=sentiment/i
                    if (sentiment == 0.0):
                        senti= "Nuetral"
                    elif (sentiment > 0.5):
                        senti= "HighPositive"
                    elif (sentiment > 0.0 and sentiment <= 0.5):
                        senti= "Positive"
                    elif (sentiment > -0.5 and sentiment < 0.0):
                        senti= "Negative"
                    else:
                        senti= "HighNegative"
                    c=SocialData(message= data["message"],
                                 created_date= data["created_time"],
                                 sentiment= senti,
                                 source = "FB",
                                 location= "UNKNOWN",
                                 like_count= data["reactions_like"]["summary"]["total_count"],
                                 love_count=data["reactions_love"]["summary"]["total_count"],
                                 haha_count=data["reactions_haha"]["summary"]["total_count"],
                                 sad_count=data["reactions_sad"]["summary"]["total_count"],
                                 wow_count=data["reactions_wow"]["summary"]["total_count"],
                                 angry_count=data["reactions_angry"]["summary"]["total_count"],
                                 link = "https://facebook.com/" + data['id'],
                                 fbquerymapper=fbquerymapper,
                                 shares= data["shares"]["count"],
                                 thankful_count= data["reactions_thankful"]["summary"]["total_count"],
                                 )
                    c.save();
    	            try:
                        ("Continue...")
    	            except:
                        pass


