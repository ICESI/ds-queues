### Introducción al uso de RabbitMQ
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción al uso de RabbitMQ
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Crear aplicativos que hagan uso de comunicación indirecta

### Introducción
Una de las tareas frecuentes en la programación de microservicios es el empleo de comunicación indirecta (desacoplada en espacio y tiempo) como un medio de lograr mejor tolerancia a fallos en los aplicaciones. En esta guía se presenta un ejemplo básico de comunicación por colas de mensajes empleando RabbitMQ.

### Desarrollo
1. Despliegue un servidor de RabbitMQ
2. Cree un ambiente virtual de python de nombre **icesi-queues** e instale las dependencias a partir del archivo **requirements.txt** proporcionado
3. Ejecute el programa send.py tres veces
4. Observe en la interfaz web de RabbitMQ como los mensajes son encolados
5. Ejecute el programa receive.py una sola vez
6. Observe en la interfaz web de RabbitMQ como todos los mensajes son eliminados

### Preguntas
* ¿Que tecnologías de mensajería estan disponibles en la nube?

### Referencias
* https://www.rabbitmq.com/tutorials/tutorial-one-python.html  
* http://blog.flux7.com/aws-sqs-fifo-queues-and-rabbitmq-on-aws
