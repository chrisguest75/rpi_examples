# DOCKER

Installing Docker on a Raspberry PI.  

Following: https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker

Check https://get.docker.com/

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

```sh
# add user to group
sudo usermod -aG docker pi

# requires a reboot
shutdown -r now

# test installation
docker version
docker info
docker run hello-world
```

## Resources
