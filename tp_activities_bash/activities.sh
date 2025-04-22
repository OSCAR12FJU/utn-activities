#EJERCICIOS GRUPO 1

#!/bin/bash
echo "La variable LOGNAME tiene el valor $LOGNAME"
echo "La variable HOME tiene el valor $HOME"
echo "La variable SHELL tiene el valor $SHELL"
echo "La variable PWD tiene el valor $PWD"
echo "La variable USER tiene el valor $USER"
echo "La variable SSH_TTY tiene el valor $SSH_TTY"


#-----------------------------------------------
#!/bin/bash

read -p "Ingrese el nombre de usuario: " usuario
read -p "Ingrese el mensaje: " mensaje

echo "$mensaje" | write $usuario

#-------------------------------------------
#!/bin/bash

echo "Nombre del script: $0"
echo "Cantidad de parámetros: $#"

for i in {1..9}; do
    eval "valor=\$$i"
    echo "El parámetro \$$i es $valor"
done

echo "Todos los parámetros: $*"

#------------------------------------
#!/bin/bash

read -p "Ingrese la primera cadena: " cadena1
read -p "Ingrese la segunda cadena: " cadena2

if [ -z "$cadena1" ]; then
    echo "La cadena1 está vacía"
else
    echo "La cadena1 no está vacía"
fi

if [ -z "$cadena2" ]; then
    echo "La cadena2 está vacía"
else
    echo "La cadena2 no está vacía"
fi

if [ "$cadena1" == "$cadena2" ]; then
    echo "Las cadenas son iguales"
else
    echo "Las cadenas son diferentes"
fi
 #----------------------------------------

 #!/bin/bash

if [ $# -eq 0 ]; then
    echo "No ha introducido ninguno. ¿Quiere ahora? (s/n)"
    read opcion
    [ "$opcion" == "s" ] && read -p "Número 1: " num1 && read -p "Número 2: " num2
elif [ $# -eq 1 ]; then
    echo "Ha introducido uno. ¿Quiere ahora? (s/n)"
    read opcion
    [ "$opcion" == "s" ] && num1=$1 && read -p "Número 2: " num2
elif [ $# -gt 2 ]; then
    echo "Demasiados parámetros, tomo los dos primeros."
    num1=$1
    num2=$2
else
    echo "CORRECTO"
    num1=$1
    num2=$2
fi

if [ -n "$num1" ] && [ -n "$num2" ]; then
    echo "Suma: $((num1 + num2))"
    echo "Resta: $((num1 - num2))"
    echo "Multiplicación: $((num1 * num2))"
    if [ "$num2" -ne 0 ]; then
        echo "División: $((num1 / num2))"
    else
        echo "Error: División por cero"
    fi
fi

#----------------------------------------
#EJERCICIOS GRUPO 2

#!/bin/bash

read -p "Ingrese un número: " num

if [ $num -gt 0 ]; then
    echo "El número es positivo"
elif [ $num -lt 0 ]; then
    echo "El número es negativo"
else
    echo "El número es cero"
fi

#----------------------------------------

#!/bin/bash

read -p "Ingrese un número: " num

if [ $((num % 2)) -eq 0 ]; then
    echo "El número es par"
else
    echo "El número es impar"
fi

#----------------------------------------

#!/bin/bash

read -p "Ingrese un número: " num

if [ $((num % 2)) -eq 0 ] && [ $((num % 3)) -eq 0 ]; then
    echo "Es múltiplo de 2 y 3"
elif [ $((num % 2)) -eq 0 ]; then
    echo "Es múltiplo de 2"
elif [ $((num % 3)) -eq 0 ]; then
    echo "Es múltiplo de 3"
else
    echo "No es múltiplo de 2 ni de 3"
fi

#---------------------------------------

#!/bin/bash

read -p "Ingrese un número: " num
fact=1
i=1

while [ $i -le $num ]; do
    fact=$((fact * i))
    i=$((i + 1))
done

echo "El factorial de $num es: $fact"

#--------------------------------------

#!/bin/bash

echo "Seleccione una opción:"
echo "a) Mostrar fecha y hora"
echo "b) Mostrar quién está conectado"
echo "c) Mostrar directorio actual"
echo "d) Salir"

read -p "Opción: " opcion

case $opcion in
    a) date ;;
    b) who ;;
    c) pwd ;;
    d) echo "Saliendo...";;
    *) echo "Opción no válida" ;;
esac

#-------------------------------------------
#EJERCICIOS GRUPO 3
#!/bin/bash

read -p "Ingrese el nombre del archivo: " archivo

if [ -f "$archivo" ]; then
    while IFS= read -r linea; do
        echo "$linea"
    done < "$archivo"
else
    echo "El archivo no existe"
fi

#---------------------------------------

#!/bin/bash

read -p "Ingrese el nombre del archivo: " archivo

if [ -f "$archivo" ]; then
    lineas=$(wc -l < "$archivo")
    echo "El archivo tiene $lineas líneas"
else
    echo "El archivo no existe"
fi

#-----------------------------------

#!/bin/bash

read -p "Nombre del archivo a copiar: " origen
read -p "Nombre del archivo destino: " destino

if [ -f "$origen" ]; then
    cp "$origen" "$destino"
    echo "Archivo copiado con éxito"
else
    echo "El archivo origen no existe"
fi

#---------------------------------------------

#!/bin/bash

read -p "Archivo a buscar: " archivo
read -p "Palabra clave: " palabra

if [ -f "$archivo" ]; then
    grep "$palabra" "$archivo"
else
    echo "Archivo no encontrado"
fi
