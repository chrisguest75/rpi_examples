# DOCKER

Installing Docker on a Raspberry PI.  

Following: https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker

Check https://get.docker.com/

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

```sh
sudo usermod -aG docker Pi
docker version
docker info
docker run hello-world
```
