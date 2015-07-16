import os, sys
import urllib, json

def main(argv):
	if len(argv) < 2:
		print "Usage: %s <max-season>" % (argv[0],)
		return 1
    # if not os.path.exists(argv[1]):
    #    print "ERROR: file %r was not found!" % (argv[1],)
    #    return 1

	season = { 'Ntt' : 'Season ' + argv[1] }
	url = "http://search.thisoldhouse.com/service/xfeeds.json?tId=videoEpisodeJSON&"+ urllib.urlencode(season) + "&type=et:television%20episodes&Nr=series:Ask%20TOH%20Video&Ntx=mode+matchall&Ns=p_episode"
	response = urllib.urlopen(url);
	d = response.read()
	if d.startswith("videoCallback("):
		d = d[len("videoCallback("):]
	if d.endswith(");"):
		d = d[:-len(");"):]
	# print d

	try:	
		data = json.loads(d)
	except ValueError:
		exit(0)
		
	# print data
	matched = data['results']
	print json.dumps(matched)

if __name__ == "__main__":
    main(sys.argv)