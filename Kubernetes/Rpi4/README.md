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
5) To setup the master node, we need to know the ip address of the master node. After getting the ip address, from your computer we can do 
```
k3sup install --ip MASTER_IP  --user pi
```
**Make sure you have your ssh key copied to raspberry pi by doing `ssh-copy-id`** </br>
**I also tried using the stable version from the flag `k3s-channel stable` but no luck.....** </br>
6) To add the worker node, do
```
k3sup install --ip MASTER_IP  --user pi
```
7) When installing the master node, `k3sup` will output the instructions on how to configure the `kubectl`. I found it annoying having to not be able to just "switch the clusters" so I opened the `kubeconfig`
file and copied that file to `.kube/config`. Adding the `user`, `cluster`, and `context` value (I changed from `default` to `k3s-rpi`) to the `.kube/config` file does the work
8) Last but not least, I changed the `context` from `kubectl` by doing 
```
kubectl config use-context k3s-rpi
```
9) That's it, I have my Raspberry Pi Kubernetes Clusters running now
```
lau@debian:~ $ kubectl get nodes
NAME                STATUS     ROLES                  AGE     VERSION
raspberrypimaster   Ready      control-plane,master   12h     v1.19.11+k3s1
raspberrypichild0   Ready      <none>                 12h     v1.19.11+k3s1

```
```
lau@debian:~ $ kubectl top node
NAME                CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%     
raspberrypichild0   120m         3%     558Mi           14%         
raspberrypimaster   526m         13%    967Mi           25% 
```
