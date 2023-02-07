# Tarea vulnerabilidades Unidad 4 :snake:

## Para esta evaluación se le pide crear 1 programa para aprovechar las  vulnerabilidades del sitio dvwa, su script debe poder realizar:

1. Scraping sobre un sitio web con formulario de login o ingreso de datos (ej. post) a través de un contenedor, si es a nivel de url debe indicar cual es y debe estar pública para validar lo indicado.
	```code
	python ./1_scraping.py
	```

2. Validar si por fuerza bruta a través de un archivo de texto que tenga un listado de usuario(separador)contraseñas posible ingresar al sito web vulnerable. 
	```code
	python ./2_bruteforce.py
	```

3. Validar si es posible realizar SQL Injection a través de alguno de los formularios que existen en el sitio web.
	```code
	python ./3_injection.py
	```