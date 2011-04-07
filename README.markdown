# Hash The Planet

A simple tool for storing arbitrary data in a central location. Mostly for temporary use.

here is the source: [http://github.com/doug/hashtheplanet](http://github.com/doug/hashtheplanet)
If you use it a lot run your own on app engine as I only have so many memcache calls.

This is not intended to be a frontend to memcache, this is for config files that I want to be able to access.
Or being able to post the temporary ip address of something I'm configuring. Or sharing some snipppet with a friend for
only a short while. The content could be html if you wanted it to be.

It is all backed by App Engine and Memcache.

## Examples

### Read Data

  curl -X GET http://hashtheplanet.com/myhash

### Set Data

  curl -X POST http://hashtheplanet.com?secret=mysecret&value=myvalue

### Delete Data

  curl -X DELETE http://hashtheplanet.com?secret=mysecret

### Convience
for convience a read call with a secret acts as a post to set the data

  curl -X GET http://hashtheplanet.com?secret=mysecret&value=myvalue

this is so you can just do it from the browser window
