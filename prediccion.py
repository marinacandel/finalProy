import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

longitud, altura = 150, 150 #predefino para todo el modelo
modelo = './modeloRedNeuronal/modelo.h5' #cargo el modelo guardado
pesos_modelo = './modeloRedNeuronal/pesos.h5' #cargo los pesos
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  arreglo = cnn.predict(x)
  resultado = arreglo[0]
  respuesta = np.argmax(resultado)
  respuesta_pred="Una danza no entrenada u otra Imagen"
  if respuesta == 0:
     respuesta_pred="Caporal Mujer"
  elif respuesta == 1:
    respuesta_pred="Caporal Varon"
  elif respuesta == 2:
    respuesta_pred="Diablada mujer"
  elif respuesta == 3:
    respuesta_pred="Diablada Varon"
  elif respuesta == 4:
    respuesta_pred="Morenada Mujer"
  elif respuesta == 5:
    respuesta_pred="Morenada Varon"
  elif respuesta == 6:
    respuesta_pred="Salay Mujer"
  elif respuesta == 7:
    respuesta_pred="Salay Varon"
  elif respuesta == 8:
    respuesta_pred="Tinkuy Mujer"
  elif respuesta == 9:
    respuesta_pred="Tinkuy Varon"
  return respuesta_pred
