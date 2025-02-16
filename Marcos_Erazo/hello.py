#Codigo Python
import hashlib

# Mensaje a cifrar
mensaje = "Hola Mundo"

# Crear un objeto sha256
sha256 = hashlib.sha256()

# Actualizar el objeto con el mensaje codificado en bytes
sha256.update(mensaje.encode('utf-8'))

# Obtener el hash en formato hexadecimal
hash_hex = sha256.hexdigest()

print(f"El hash SHA-256 del mensaje 'Hola Mundo' es: {hash_hex}")

#texto de prueba Git pull re
