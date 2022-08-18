# SSH

SSHing onto a Raspberry PI.  

NOTE: You'll need to have enabled SSH if using Raspbian.  

```sh
# finding rpi on the network
nmap -sV -p 22 192.168.1.0/24
```

The default user and password on Raspbian is `user:pi` and `pw:raspberry`  

```sh
# agent forwarding for github access  
ssh -A pi@192.168.x.x
```

## Resources

* SSH example in my sysadmin_examples repo [here](https://github.com/chrisguest75/sysadmin_examples/tree/master/08_ssh)
