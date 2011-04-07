from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import re
import simplejson as json

alphanumeric = re.compile('^[a-zA-Z0-9]+$')
SUCCESS = 'success'
FAILURE = 'failure'
TIME = 1*60*60*24 # expire in a day by default

class HashThePlanet(webapp.RequestHandler):
  def get(self, hash):
    rsecret = self.request.get('secret')
    if rsecret:
      self.post(hash)
    else:
      value = memcache.get(hash, None)
      if value:
        secret, sep, value = value.partition('\n')
        if value:
          self.response.out.write(value)

  def post(self, hash):
    result = {}
    rsecret = self.request.get('secret')
    rvalue = self.request.get('value')
    rtime = self.request.get('time') or TIME
    try:
      rtime = int(rtime)
    except (ValueError, IndexError):
      rtime = TIME
    if not rsecret or not alphanumeric.match(rsecret):
      result['status'] = FAILURE
      result['reason'] = 'Secret must be provided to modify or create, and secret must be alphanumeric.'
    elif not rvalue:
      result['status'] = FAILURE
      result['reason'] = 'Value must be provided to set the hash.'
    else:
      value = memcache.get(hash, None)
      if value:
        secret, sep, value = value.partition('\n')
        if secret != rsecret:
          result['status'] = FAILURE
          result['reason'] = 'Secret does not match.'
        else:
          rvalue = '\n'.join([rsecret,rvalue])
          memcache.set(hash,rvalue,time=rtime)
          result['status'] = SUCCESS
      else:
        rvalue = '\n'.join([rsecret,rvalue])
        memcache.set(hash,rvalue,time=rtime)
        result['status'] = SUCCESS
    json.dump(result, self.response.out)

  def delete(self, hash):
    result = {}
    rsecret = self.request.get('secret')
    if not rsecret:
      result['status'] = FAILURE
      result['reason'] = 'Secret must be provided.'
    else:
      value = memcache.get(hash, None)
      if not value:
        result['status'] = SUCCESS
      else:
        secret, sep, value = value.partition('\n')
        if secret != rsecret:
          result['status'] = FAILURE
          result['reason'] = 'Secret does not match.'
        else:
          memcache.delete(hash)
          result['status'] = SUCCESS
    json.dump(result, self.response.out)

def main():
  application = webapp.WSGIApplication([
    (r'/(.*)', HashThePlanet)
    ], debug=True)
  run_wsgi_app(application)

if __name__ == "__main__":
  main()