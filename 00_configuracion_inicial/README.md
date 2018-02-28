### Instalación y configuración inicial de RabbitMQ
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Instalación y configuración inicial de RabbitMQ
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer y emplear los pasos para la instalación y configuración de RabbitMQ

### Introducción
RabbitMQ es una tecnología open source para la creación de colas de mensajes

### Desarrollo

```
su -c 'rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm'
yum install erlang -y
yum install socat -y
su -c 'rpm -Uvh https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.7.3/rabbitmq-server-3.7.3-1.el7.noarch.rpm'
service rabbitmq-server start
rabbitmqctl add_vhost /icesi
rabbitmqctl add_user icesi password
rabbitmqctl set_permissions -p /icesi icesi ".*" ".*" ".*"
rabbitmq-plugins enable rabbitmq_management
chown -R rabbitmq:rabbitmq /var/lib/rabbitmq/
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
firewall-cmd --zone=public --add-port=5672/tcp --permanent
firewall-cmd --zone=public --add-port=15672/tcp --permanent
firewall-cmd --reload
```

### Preguntas
* ¿Que otras tecnologías de mensajeria existen?

### Referencias
* https://www.rabbitmq.com/download.html
