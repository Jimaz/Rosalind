s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

dict = {} # Inicializar diccionario vacío

for p in s.split(' '): # Iteramos sobre cada palabra del string, asegurando quitar los espacios con split()
    key = 0 # Este será el contador del diccionario que actuará como clave
    if p not in dict: # Si la palabra no está en el diccionario se añade
        dict [p] = key

    if p in dict: # Si la palabra está en el diccionario, se suma 1
        dict [p] += 1

for k, v in dict.items(): # Accedemos a los elementos del diccionario y formateamos la salida
    print (k, v)
