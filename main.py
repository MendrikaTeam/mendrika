# importeko ny module communication electron sy python
import eel 

# misafidy port de communication amn le langage
# verifiena tsara mitov amn le anaty main.js
PORT = 19003

# preciseko dossier misy an le fichier static jiaby
eel.init('static/')
eel.start(mode='electron', port=PORT)