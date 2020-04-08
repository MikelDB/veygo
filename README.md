# veygo technical test
I've isolated all the application using docker-compose so that it can be used in any system with docker (hopefully), the only configuration it
should require is adding the following lines to the .bashrc file:

```buildoutcfg
export MY_UID=$(id -u)
export MY_GID=$(id -g)
```
This is done so that the docker-compose maps the user outside and inside docker (this probably won't work on Windows). Then you should just need
to do:
```
docker-compose up
```
And everything should be ready to enter http://localhost:5000