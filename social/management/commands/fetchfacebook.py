from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):


    def handle(self, *args, **options):
        import facebook, datetime
        token = "741011062769592|tLH6FvFILJ0oOqoHGUKouycRuR4"   
	fb_id = "bbcnewsenglish"   
	since = datetime.datetime.now() - datetime.timedelta(days=5)
	d = since.date()
	graph = facebook.GraphAPI(token)
	data_set = graph.request(str(fb_id) + '/posts/?fields=description,attachments,message,likes,created_time,shares,link,from,'
                                  'type,image,comments.summary(true)&limit=9&since=' + str(d))

	data_set = data_set['data']
	for data in data_set:
    	    print "\n"
    	    print "\n"
    	    print "USER    : ", data["from"]["name"]
            print "SHARES  : ", data["shares"]["count"]
    	    #print "Likes   : ", str(data["likes"])
    	    print "Message : ", data["message"]
    	    print "date    : ",data["created_time"]
    	    print "link    : ",data['link']
            print "comment : ",data['comment']
    	    try:
                input("Continue...")
    	    except:
                pass

