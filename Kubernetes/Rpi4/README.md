## Kubernetes (K3S) on Raspberry Pi 4

![my first setup](IMG_20210601_091709.jpg )

## Materials
1) 2x Raspberry Pi 4
2) 2x Official PSU
3) iUniker Raspberry Pi 4 Cluster Case
4) Sandisk USB 3.1 Ultra Fit 64GB

## Introduction
* After watching the [Kubecon talk](https://kccnceu2021.sched.com/event/iE2B/automating-your-home-with-k3s-and-home-assistant-eddie-zaneski-amazon-web-services-jeff-billimek-the-home-depot),
I decided to buy two Raspberry Pi 4 for one master node and one child node. 
* [Alex Ellist](https://github.com/alexellis) really make a lot of great open source software and blogs for how to set up Kubernetes on Raspberry Pi 4 so I mostly followed his blog to set it up.

## Process
1) Firstly, Raspberry Pi has default `raspberrypi` as their hostname, so changing the hostname will make it easier to recognize master node and children node. We can do that by using
```
hostnamectl set-hostname NAME
```
2) I then made sure the router's DHCP server uses the same IP address everytime it boots up
3) I installed [arkade](https://github.com/alexellis/arkade) and [k3sup](https://github.com/alexellis/k3sup) on my main machine that will greatly simplify the setup.
4) I used [arkade](https://github.com/alexellis/arkade) to install `kubectl` by doing 
```
arkade install kubectl
```
5) From [here](https://github.com/k3s-io/k3s/issues/3389), I know IPv6 is not supported for Flannel so I had to disable IPv6 by adding these commands to `/etc/sysctl.conf`
``` 
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1
net.ipv6.conf.eth0.disable_ipv6 = 1
```
6) To setup the master node, we need to know the ip address of the master node. After getting the ip address, from your computer we can do 
```
k3sup install --ip MASTER_IP  --user pi --k3s-channel stable
```
**Make sure you have your ssh key copied to raspberry pi by doing `ssh-copy-id`** </br>
7) To add the worker node, do
```
kubectl taint node kmaster  node-role.kubernetes.io/master:-
```
8) To enable `kubectl` to work for external IP we need configure `kmaster.service`. Modify `ExecStart` so it looks like
```
ExecStart=/usr/local/bin/k3s \
    server \
	'--tls-san' \
	'73.132.70.117' \
```
9) Restart the service
```
sudo systemctl restart k3s
```
