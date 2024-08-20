README - Ejecución de pruebas E2E automatizadas con Selenium

REQUISITOS PREVIOS

1. Tener instalado python en el equipo donde se ejecutara la prueba.
Para obtener más información sobre como instalarlo, acceder al sitio oficial de python.
Sitio oficial: https://www.python.org/downloads/

2. En caso de no tener pip instalado en el equipo, ejecutar el siguiente comando: python get-pip.py

3. Instalar selenium usando el siguiente comando: pip install selenium

4. Instalar webdriver-manager usando el siguiente comando: pip install webdriver-manager

5. Instalar requests usando el siguiente comando: pip install requests


PASOS PARA EJECUTAR LA PRUEBA

1. Ubicar el directorio de trabajo
Una vez instalado todas las dependencias, ir al directorio que contiene el
proyecto de pruebas API: cd testAutomation/automation_e2e

3. Ejecutar las pruebas API
Finalmente, ejecuta las pruebas e2e con el siguiente comando: pytest test_purchase_flow.py