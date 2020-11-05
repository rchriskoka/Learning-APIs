# Learning-APIs
This repository is the beginning of my journey with APIs. 

## What is an API? 
API stands for Application Programming Interface. It is basically how different machines and software talk to each other to create ever more complex applications.

## Why build APIs?
These days, very few applications are stand alone. An API can act as a platform for new partnership opportunities, new revenue channels, or even new features for your organization. Many call this the API economy.

## Different Types of APIs
RESTful APIs over HTTP with JSOn is the most popular type of APIs. There's GraphQL but in this repo, just RESTful APIs :)

## What makes Good APIs?
* Easy to learn 
* Easy to use
* Easy to extend
* Easy to read and maintain code that uses it.

## Rate Limiting in API Development
Rate Limiting is using code to limit the number of times per second that we hit a particular API. Rate limiting will make your code slower, but it's better than getting banned from using an API altogether. The easiest way to perform rate limiting is to use Python's ```time.sleep()``` function.
However, there is another technique useful for rate limiting and it is using a local database to cache the results of any API call, so that if we make the same call twice, we simply read the second call from the local cache. 
### Benefits of using local cache
* You don't make extra API calls that you don't need.
* You don't need to wait the extra time to rate limit when reading the repeated calls from the cache.

Creating a logic for a local cache is reasonably complex - so we simply use ```requests-cache``` which will do all our work with only a couple of lines of code.
``` pip install requesrs-cache```
Then all we need to do is import the libaray and invoke the ```requests_cache.install_cache()``` function, and the library will transparently cache new API requests, and use the cache whenever we make a repeated call.

