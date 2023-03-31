
# Problema 2

 Un servidor crea logs por cada acción que se realiza en él. El administrador desea
un programa que todos los días borre todos los logs excepto si el log contiene la
palabra "error"; si contiene esta palabra, se debe copiar el log al directorio "Errores" y se debe enviar un correo al administrador.

## PASO 1

El servidor crea logs de registro sobre cada accion que se realiza, se necesita un programa que todos lo dias borre los logs excepto los logs que contengan la palabra "error".
Si contiene la palabra "error" se debe hacer una copia a un directorio llamado errores y notificar via correo al administrador. 

## PASO 2
1. No se necesitaria una interfaz de ususario, excepto para apagar o encender el servicio por linea de comando.
2. Crear una funcion que revise los archivos de texto dentro de la carpeta de logs
3. Crear una funcion que identifique la palabra "error" en mayuscula o miniscula  en cada log.
4. Si identifica la palabra "error"  hacer copy & paste hacia el directorio "errores"
5. Generar una rutina que ejecute un proceso en segundo plano que envie de forma
automatica un correo al administrador con la cantidad de archivos de error reportados.

## PASO 3

 1. Se debe investigar como funciona la aplicacion que genera los logs para entender el peso del archivo y cuanto se tardaria en moverlo si es que contiene errores.
 2. identificar la funcion que permita en el menor tiempo posible los logs que contenga la palabra "error".
 3. Investigar la mejor forma de administrar el programa, si es mejor arrancar por linea de comandos o bien detener el programa en casos de fechas de mantenimiento del servidor.
 4. El programa debe de consumir la menor cantidad de recursos y no debe impactar el performance del servidor en produccion durante la revision de los logs.
