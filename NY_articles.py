import urllib2, os
import json 

json_data = open("myapi.json").read() #reading api key from myapi.json
myAPI = json.loads(json_data)
key = str(myAPI["myAPI"])

# Setting the begin data and end date
request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" 
					+ "20170411" + "&end_date=" + "20170412" + "&page=" +
					 str(2) + "&api-key=" + key
response = urllib2.urlopen(request_string)
content = response.read()
data = json.loads(content)
MostPopularToJSON = open('pop_times.json','w')
MostPopularToJSON.write(data)
MostPopularToJSON.close()
