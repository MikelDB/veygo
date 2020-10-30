# Veygo Technical Test
This repository contains the technical test made for the recruiting process for Veygo
## Setup
I've isolated all the application using docker-compose so that it can be used in any system with docker (hopefully), the only configuration it
should require is adding the following lines to the .bashrc file:

```buildoutcfg
export MY_UID=$(id -u)
export MY_GID=$(id -g)
```
This is done so that the docker-compose maps the user outside and inside docker (this probably won't work on Windows). 

If it does not worl you can modify this line in the docker-compose file ``user: $MY_UID:$MY_GID`` with the ID's manually.

Then you should just need
to do:
```
docker-compose up
```
And everything should be ready to enter http://localhost:5000

## Database
The database is prepopulated with some products and some discount codes and will maintain it's information even when docker is down so in case
you want to add more codes and reset it to the original set I recommend doing:
```buildoutcfg
sudo rm -rf docker/database/data/
```
And then you can launch again the docker-compose.

## ToDo
As the test stated that I shouldn't use to much time on this and I've already worked around 10h on it I'll leave here things I think that would've 
been interesting to do.
* Move the logic in the controllers to separated use cases
* More security in trusting what comes from the requests
* Use of webpack or other build tools for the frontend
* Creation of a user so the customers can check their past purchases
* More interesting frontend app
* Creation of repositories for the use of the database and not use the models inside the controllers or the use cases

## About this
To be honest this is the first time I've used Flask to this extent or that I've used sqlalchemy, so I've learnt a lot and this has been a great way to learn a lot more about this frameworks.

