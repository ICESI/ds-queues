### Message Queues

### Activities
1. Deploy rabbitmq cluster

En el nodo maestro: 

Actualizar /etc/hosts
```
192.168.33.10 rabbit1
192.168.33.11 rabbit2
```

Es necesario configurar correctamente el hostname del nodo antes de comenzar a configurar rabbitmq-server en modo cluster
```
hostnamectl set-hostname rabbit1
reboot
```

```
systemctl restart rabbitmq-server
```

Copiar la cookie de earlang en los esclavos y reiniciar rabbitmq-server

```
cat /var/lib/rabbitmq/.earlang_cookie
```

```
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@rabbit2
rabbitmqctl start_app
```

En el nodo esclavo 1: 

Actualizar /etc/hosts
```
192.168.33.10 rabbit1
192.168.33.12 rabbit3
```

Es necesario configurar correctamente el hostname del nodo antes de comenzar a configurar rabbitmq-server en modo cluster
```
hostnamectl set-hostname rabbit2
reboot
```

```
systemctl restart rabbitmq-server
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
```

En el nodo esclavo 2:

Actualizar /etc/hosts
```
192.168.33.11 rabbit2
192.168.33.12 rabbit3
```

Es necesario configurar correctamente el hostname del nodo antes de comenzar a configurar rabbitmq-server en modo cluster
```
hostnamectl set-hostname rabbit3
reboot
```

```
systemctl restart rabbitmq-server
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
```

2. Test Hello World against members of the cluster
3. Enable high availability in the cluster
4. Test that if a node fail the messages do not get lost
5. Put a load balancer in front on the rabbitmq cluster
6. Run test against the load balancer. Test that if a node fail other node response automatically

### References
* https://www.rabbitmq.com/clustering.html  
* http://blog.flux7.com/blogs/tutorials/how-to-creating-highly-available-message-queues-using-rabbitmq
* http://linuxpitstop.com/rabbitmq-cluster-on-centos-7/  
* http://devopspy.com/linux/rabbitmq-cluster-centos-7/  
* http://blog.flux7.com/aws-sqs-fifo-queues-and-rabbitmq-on-aws
