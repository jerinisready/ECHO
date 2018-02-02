from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):


    def handle(self, *args, **options):
        import facebook, datetime
        token = "741011062769592|tLH6FvFILJ0oOqoHGUKouycRuR4"   
	fb_id = "narendramodi"   
	since = datetime.datetime.now() - datetime.timedelta(days=14)
	d = since.date()
	graph = facebook.GraphAPI(token)
	data_set = graph.request(str(fb_id)+'/posts?fields=description,message,created_time,shares,link,from,'                                      
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
    	    print "Likes   : ",data["reactions_sad"]
    	    print "Message : ",data["message"]
    	    print "date    : ",data["created_time"]
    	    print "link    : ",data['link']
    	    try:
                input("Continue...")
    	    except:
                pass

