#!/bin/bash

# Esperar a que el servidor interno de Ollama responda
echo "⏳ Esperando a que Ollama inicie..."

# Reemplazamos curl por "ollama list". Si falla, espera 2 segundos y reintenta.
while ! ollama list > /dev/null 2>&1; do
  sleep 2
done

echo "🚀 Ollama listo. Registrando modelos..."

# Recorrer la carpeta de modelos mapeada
for file in /models/*.mf; do
    # Evitar errores si la carpeta está vacía
    [ -e "$file" ] || continue
    
    model_name=$(basename "$file" .mf)
    echo "🔨 Creando/Actualizando: $model_name"
    
    ollama create "$model_name" -f "$file"
done

echo "✅ Proceso finalizado."