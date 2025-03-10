# CotiCar - Calculadora de Costos de Vehículos en Argentina

## Descripción
CotiCar es una aplicación web desarrollada con **Streamlit** que permite calcular los costos mensuales de mantener un vehículo en Argentina, basándose en el precio en dólares del auto y la cotización del dólar blue. Además, incluye una comparación con el sueldo del usuario para determinar la viabilidad financiera de la compra.

## Características
- Conversión del precio del vehículo de USD a ARS.
- Cálculo de costos mensuales: **seguro, patente, combustible, mantenimiento**.
- Comparación del costo mensual del auto con el **sueldo del usuario**.
- Generación de un **análisis financiero** con IA utilizando **Groq API**.

## Tecnologías utilizadas
- **Python 3**
- **Streamlit** (para la interfaz de usuario)
- **Groq API** (para el análisis financiero con IA)

## Instalación y ejecución
### 1. Clonar el repositorio
```bash
 git clone https://github.com/tu-usuario/coticar.git
 cd coticar
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv  # Crear entorno virtual
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
streamlit run coticar.py
```

## Uso
1. Ingresar el **precio del vehículo en dólares**.
2. Ingresar la **cotización del dólar blue**.
3. Ingresar el **sueldo mensual en ARS**.
4. Visualizar el **cálculo de costos mensuales**.
5. Recibir un **análisis financiero** detallado con IA.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, sigue estos pasos:
1. Haz un **fork** del repositorio.
2. Crea una nueva rama: `git checkout -b feature-nueva-funcionalidad`.
3. Realiza tus cambios y haz un **commit**: `git commit -m 'Agrega nueva funcionalidad'`.
4. Sube los cambios: `git push origin feature-nueva-funcionalidad`.
5. Abre un **pull request**.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo [LICENSE](LICENSE).

---
**Autor:** Athos  

