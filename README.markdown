# Hash The Planet

A simple tool for storing temporary data in a central location.

## "You know when you go to the mall and your mom tells you if we get seperated meet up right here. Well, for your code, that place is hashtheplanet.com"

Here is the source:
[http://github.com/doug/hashtheplanet](http://github.com/doug/hashtheplanet)

If you use it a lot run your own on app engine as I only have
so many memcache calls.

This is not intended to be a frontend to memcache, this is for config
files that I want to be able to access.
Or being able to post the temporary ip address of something I'm configuring.
Or sharing some snipppet with a friend for
only a short while. Some global hash to some arbitrary transient value.
The content can be any string including html if you want if formated when
returned, but probably something like json is
a good choice.

It is all backed by App Engine and Memcache.

## Examples

### Read Data

    curl -X GET http://www.hashtheplanet.com/myhash

### Set Data

    curl -X POST http://www.hashtheplanet.com/myhash?secret=mysecret&value=myvalue

### Delete Data

    curl -X DELETE http://www.hashtheplanet.com/myhash?secret=mysecret

### Extras

For convenience a read call with a secret acts as a post to set the data.

    curl -X GET http://www.hashtheplanet.com/myhash?secret=mysecret&value=myvalue
    IS_EQUAL_TO
    curl -X POST http://www.hashtheplanet.com/myhash?secret=mysecret&value=myvalue

This is so you can just do it from the browser window.

