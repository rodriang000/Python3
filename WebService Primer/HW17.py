import requests
import json

class _webservice_primer:
    def __init__(self):
        self.movies = {
                        'genres': '',
                        'title': '',
                        'result': '',
                        'id': '',
                        'img': ''
                      }

        self.users = {
                        'zipcode': '',
                        'age': '',
                        'gender': '',
                        'id': '',
                        'occupation': ''
                     }

        self.ratings = {
                        'rating': '',
                        'movie_id': '',
                        'result': ''

                       }
        self.SITE_URL = 'http://student04.cse.nd.edu:51001'
        self.MOVIES_URL = self.SITE_URL + '/movies/'
        self.RESET_URL = self.SITE_URL + '/reset/'
        self.USERS_URL = self.SITE_URL + '/users/'

    def get_movie(self, mid):
        r = requests.get(self.MOVIES_URL + mid)
        resp = json.loads(r.content.decode('utf-8'))
        return resp

    def get_movies(self): #TODO: See if I need to fix this one.
        r = requests.get(self.MOVIES_URL)
        resp = json.loads(r.content.decode('utf-9'))
        return resp
    
    def delete_movie(self, mid):
        r = requests.delete(self.MOVIES_URL + mid)
        resp = json.loads(r.content.decode('utf-8'))
        return resp

    def delete_user(self, uid):
        r = requests.delete(self.USERS_URL + uid)
        resp = json.loads(r.content.decode('utf-8'))
        return resp

    def reset_movie(self, mid):
        r = requests.put(self.RESET_URL+ mid)
        resp = json.loads(r.content.decode('utf-8'))
        return resp

    def set_movie_title(self, mid, mtitle):
        r = requests.get(self.MOVIES_URL + mid)
        resp = json.loads(r.content)
        resp['title'] = mtitle
        r = requests.put(self.MOVIES_URL + mid, json=resp)

if __name__ == "__main__":
    MID = "46"
    title = "Balls of Steel"
    ws = _webservice_primer()
    movie = ws.reset_movie(MID)
    ws.movies['genres'] = "test";
#   print(ws.movies);

    # movie = ws.set_movie_title(MID, title)
    # if movie['result'] == 'success':
    #     print ("Title:\t%s" % movie['title'])
    # else:
    #     print ("Error:\t%s" % movie['message'])
    #
    # movie = ws.get_movie(MID)
    # if movie['result'] == 'success':
    #     print ("Title:\t%s" % movie['title'])
    #     print(movie)
    # else:
    #     print ("Error:\t%s" % movie['message'])

   # movie = ws.delete_movie(MID)
   # if movie['result'] == 'success':
   #     print ("Movie deleted")
   # else:
   #     print ("Movie not deleted")





