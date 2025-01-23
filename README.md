# CopilotExporter
Es un pequeño script para convertir el chat exportado de copilot a un archivo formateado markdown (.md)

# Como usarlo:
1. Ten [python](https://www.python.org/downloads/) instalado 
2. En visual studio code exporta una sesión de chat de copilot a json mediante `Ctrl+Shift+P | Chat: Export Session...` eligiendo  `View > Command Palette | Chat: Export Session...`
3. Deja el chat.json en el mismo lugar donde el script de python
4. Abre cmd o cualquier otra terminal que uses y ejecuta  `python exporterCopilot.py` o `py exporterCopilot.py`
5. En la misma carpeta creará un fichero .md formateado 