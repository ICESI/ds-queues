### Creación de un cluster con RabbitMQ
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Creación de un cluster con RabbitMQ
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Crear y emplear un cluster con RabbitMQ

### Introducción
La configuración de RabbitMQ en cluster permite aumentar la cantidad de usuarios que pueden ser atendidos por las aplicaciones que emplean colas de mensajes

### Desarrollo
1. Los siguientes pasos permiten desplegar un cluster de RabbitMQ. Se asume que en cada nodo ya se encuentra instalado el servicio de RabbitMQ

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

2. Cree un ambiente virtual de python de nombre **icesi-queues** e instale las dependencias a partir del archivo **requirements.txt** proporcionado
3. Ejecute el programa send.py una vez
4. Observe en la interfaz web de RabbitMQ como el mensaje es encolado
5. Ejecute el programa receive.py una sola vez
6. Observe en la interfaz web de RabbitMQ como el mensaje es eliminado

### Preguntas
¿Cual es la cantidad máxima de nodos que puede tener un cluster de RabbitMQ?

### Referencias
* https://www.rabbitmq.com/clustering.html  
* http://blog.flux7.com/blogs/tutorials/how-to-creating-highly-available-message-queues-using-rabbitmq
* http://linuxpitstop.com/rabbitmq-cluster-on-centos-7/  
* http://devopspy.com/linux/rabbitmq-cluster-centos-7/  
