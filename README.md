# Nexus_Query

Nexus Query es una aplicación web cuyo objetivo es la traducción de Lenguaje Natural a Consultas SQL utilizando un modelo de lenguaje grande (LLM) a través de la API de Google Gemini.

Para utilizar Nexus Query asegurese de instalar los requerimientos del archivo "requirements.txt"

Pasos a seguir para utilizar Nexus Query:

1. Cree y active el entorno virtual.
2. Cree un archivo .env con su API KEY de Gemini o Genia.
3. Instale los requerimientos del archivo "requirements.txt".
4. En la teminal ingrese "streamlit run main.py".
5. Utilice los prompts de prueba para probar el modelo.

# Prompts de Prueba para agregar las tablas

"tengo una tabla de ventas con Id_venta, Id_cliente, Id_Producto y precio_venta"

"tengo la tabla de clientes Con Id_cliente, nombre, empresa, fecha_alta, total_vendido"

"Tengo tabla de productos con Id_producto, nombre, categoria, precio_venta, precio_compra"

# Consulta para codigo SQL

"Necesito saber cuales son los top 5 clientes en total vendido de la categoría limpieza unicamente teniendo en cuenta ventas superioes a 500.000 pesos"