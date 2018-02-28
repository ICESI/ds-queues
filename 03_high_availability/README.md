### Alta disponibilidad con RabbitMQ
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Alta disponibilidad con RabbitMQ
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Emplear la funcionalidad de alta disponiblidad de un cluster con RabbitMQ

### Introducción
La configuración de RabbitMQ en modo de alta diponibilidad permite poder replicar mensajes en el cluster para que estos no se pierdan ante la caída de un nodo

### Desarrollo
1. Habilite la opción de alta disponibilidad en el cluster de RabbitMQ
2. Cree un ambiente virtual de python de nombre **icesi-queues** e instale las dependencias a partir del archivo **requirements.txt** proporcionado
3. Ejecute el programa send.py una vez
4. Observe en la interfaz web de RabbitMQ como el mensaje es encolado
5. Apague uno de los nodos del cluster donde el mensaje fue encolado
6. Ejecute el programa receive.py una sola vez
7. Observe como el mensaje es obtenido a partir del cluster

### Preguntas
¿Como se logra mantener el principio de integridad al emplear la opción de alta disponibilidad con RabbitMQ?

### References
* https://www.rabbitmq.com/ha.html
