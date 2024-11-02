# DEBUGGIN

pdb es una libreria built-in para debugear desde consola, para ejecutarla escribmos:

```shell
python -m pdb area_cuadrado.py
```

escribiendo "l" se ven las siguientes lineas
escribiendo "q" se sale del debuggin

Para definir un breakpoint escribimos: (se puede usar "b" en lugar de "break")

```shell
break 8
```

Después escribimos "continue" o "c" y continuará hasta el breakpoint, si usamos "next" vamos a la siguente linea de código.

Para ver una variable escribmos

```shell
display nombre_variable
```

Con "restart" se reinicia el debuggin sin quitar los breakpoints.
