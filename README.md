# Proyecto C1 - Robot Crawler - Taller de Proyecto II


En este repositorio se muestra el trabajo realizado en el transcurso de la materia Taller de Proyecto II en el año 2021. El mismo consiste en un robot Crawler que aprende a desplazarse utilizando un brazo robótico con dos grados de libertad mediante el algoritmo de aprendizaje automático Q-Learning.

<p align="center">
  <img src="resources/Crawler.png" width=50%/>
</p>

## Comenzando 🚀

Si bien el programa puede ser ejecutado desde una computadora de uso personal, el código se encuentra preparado para la administración de un robot Crawler controlado por una Raspberry Pi.

Mira **Despliegue** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

A continuación se listan componentes con los que se deberá contar para la construcción del robot Crawler:

<table>
  <tr>
    <th>Item</th>
    <th>Nombre</th>
    <th>Descripción</th>
    <th>Cantidad</th>
  </tr>
  <tr>
    <td>1</td> <td>Raspberry Pi 3 B+</td> <td>Lógica del programa y servidor.</td> <td>1</td>
  </tr>
  <tr>
    <td>2</td> <td>Encoders HC-020K</td> <td>Mide la rotación de las ruedas (movimiento del robot).</td> <td>2</td>
  </tr>
  <tr>
    <td>3</td> <td>Servomotores SG90</td> <td>Articulaciones del brazo robótico.</td> <td>2</td>
  </tr>
  <tr>
    <td>4</td> <td>Impresión 3D del brazo</td> <td>Esqueleto del brazo robótico.</td> <td>1</td>
  </tr>
  <tr>
    <td>5</td> <td>Ruedas de goma</td> <td>Ayudan al desplazamiento.</td> <td>2</td>
  </tr>
  <tr>
    <td>6</td> <td>Rueda ranurada</td> <td>Permite estabilizar al robot.</td> <td>1</td>
  </tr>
  <tr>
    <td>7</td> <td>Fuente switching 5V 3A</td> <td>Alimentación del sistema.</td> <td>1</td>
  </tr>
  <tr>
    <td>8</td> <td>Placa de alimentación QYF-DY02</td> <td>Provee múltiples niveles de tensión para la alimentación de los diferentes dispositivos.</td> <td>1</td>
  </tr>
  <tr>
    <td>9</td> <td>Pendrive 32GB</td> <td>Almacenamiento del SO, los archivos de programa, la base de datos y el servidor.</td> <td>1</td>
  </tr>
  <tr>
    <td>10</td> <td>Kit de cables dupont</td> <td>Kit de cables dupont macho-hembra, macho-macho y hembra-hembra.</td> <td>1</td>
  </tr>

</table>

Una vez obtenidos los elementos necesarios, se debe construir el Robot siguiendo el diagrama de ensamblado mostrado a continuación:

<p align="center">
  <img src="resources/DiagramaEnsamblado.png" width=60%/>
</p>


### Instalación 🔧

Para poder cargar el proyecto en una Raspberry Pi (o ejecutar el programa en una computadora personal como si de una simulación se tratase), en primer lugar se deberá clonar el repositorio en el dispositivo. 
Por ejemplo, si se clona utilizando SSH:

```
git@github.com:flemingmartin/crawler-bot.git
```

Se deberá contar con Python 3 y las siguientes librerías (instalables mediante _pip3 install_)
```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.


