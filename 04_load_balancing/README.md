### Balanceo de carga con un cluster con RabbitMQ
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Balanceo de carga con un cluster con RabbitMQ
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer la importancia de las tecnologías de balanceo de carga
* Emplear tecnologías de balanceo de carga con RabbitMQ

### Introducción
Una configuración de RabbitMQ con un balanceador de carga permite tener un punto de entrada único hacia la cola de mensajeria. Ante la caída de uno de los nodos el balanceador redireccionará automáticamente la petición recibida hacia un nodo saludable del cluster

### Desarrollo
1. Despliegue un servidor con un servicio de balanceo de carga
2. Realice las configuraciones necesarias para direccionar las peticiones a los nodos del cluster de RabbitMQ
3. Cree un ambiente virtual de python de nombre **icesi-queues** e instale las dependencias a partir del archivo **requirements.txt** proporcionado
4. Ejecute el programa send.py una vez
5. Observe en la interfaz web de RabbitMQ como el mensaje es encolado
6. Apague uno de los nodos del cluster donde el mensaje fue encolado
7. Ejecute el programa receive.py una sola vez
8. Observe como el mensaje es obtenido a partir del cluster

### Preguntas
* Investigue otras tecnologías de balanceo de carga diferentes a la empleada

###  Referencias
* https://ypereirareis.github.io/blog/2017/04/03/rabbitmq-high-available-cluster-haproxy-docker/
* https://insidethecpu.com/2014/11/17/load-balancing-a-rabbitmq-cluster/
* https://www.rabbitmq.com/federated-queues.html
