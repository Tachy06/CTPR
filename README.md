# Página oficial del CTPR DE SC

Este es el repositorio oficial del CTPR. 

## Tecnologías utilizadas

En este proyecto usamos ciertas tecnologías que son:

- HTML
- CSS
- JavaScript
- Django

## Base de datos

Nosotros optamos por utilizar la base de datos tipo **SQL** más que todo por mantener la información mayormente estructurada.

## El porque crear esta página

Bueno el fin de crear esta página es para dar **anuncios del colegio**, **mostrar información acerca de la institución**, **mantener informados a los padres sobre sus hijos** y **digitalizar** muchas cosas que se hacian a mano.

## Creada con la mejor estructura de Django

Este proyecto se dividió por apps, así cada funcionalidad está por separado y su lógica de igual manera, esto evita muchos errores o posibles fallas que dejen expuesto el sistema como por **Inyecciones SQL**. El panel administrador es el incorporado por defecto que trae Django ya que este es muy seguro y así evitamos hacer uno y que tenga fallas.

## Consultas a la base de datos

Las consultas hechas a las bases de datos fueron hechas mediante las funciones incorporadas con django como el *Objects.filter*, *Objects.get*, etc. Ya que estos no dejan vulnerabilidades como si las dejan si se hacen consultas manuales. Así evitamos **Inyecciones SQL**