{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red131\green0\blue165;\red0\green0\blue0;\red15\green112\blue1;
\red144\green1\blue18;\red87\green65\blue25;\red0\green0\blue255;\red19\green85\blue52;}
{\*\expandedcolortbl;;\cspthree\c54429\c17729\c68160;\csgray\c0;\cspthree\c21607\c49422\c13150;
\cspthree\c58589\c14916\c12116;\cspthree\c40125\c32566\c16155;\cspthree\c22\c0\c95960;\cspthree\c18354\c39391\c27726;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf2 import\cf3  streamlit \cf2 as\cf3  st\
\cf2 import\cf3  tensorflow \cf2 as\cf3  tf\
\cf2 from\cf3  streamlit_drawable_canvas \cf2 import\cf3  st_canvas\
\cf2 import\cf3  cv2\
\cf2 import\cf3  numpy \cf2 as\cf3  np\
\cf4 # Configuraci\'f3n de la p\'e1gina\
\cf3 st.set_page_config(page_title=\cf5 "IA Digit Recognizer"\cf3 )\
st.title(\cf5 "Reconocedor de D\'edgitos en Tiempo Real"\cf3 )\
st.write(\cf5 "Dibuja un n\'famero del 0 al 9 en el recuadro\
negro."\cf3 )\
\cf4 # 1. Cargar el modelo guardado\
\cf6 @st.cache_resource\
\cf7 def\cf3  \cf6 load_my_model\cf3 ():\
\cf2 return\cf3  tf.keras.models.load_model(\cf5 'modelo_mnist.keras'\cf3 )\
model = load_my_model()\
\cf4 # 2. Crear el lienzo (Canvas) para dibujar\
\cf3 canvas_result = st_canvas(\
fill_color=\cf5 "white"\cf3 , stroke_width=\cf8 20\cf3 ,\
stroke_color=\cf5 "white"\cf3 ,\
background_color=\cf5 "black"\cf3 , height=\cf8 280\cf3 , width=\cf8 280\cf3 ,\
drawing_mode=\cf5 "freedraw"\cf3 , key=\cf5 "canvas"\cf3 ,\
)\
\cf4 # 3. Procesar el dibujo y predecir\
\cf2 if\cf3  canvas_result.image_data \cf7 is\cf3  \cf7 not\cf3  \cf7 None\cf3 :\
\cf4 # Convertir el dibujo a 28x28 p\'edxeles (formato MNIST)\
\cf3 img =\
cv2.resize(canvas_result.image_data.astype(\cf5 'uint8'\cf3 ), (\cf8 28\cf3 ,\
\cf8 28\cf3 ))\
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\
img = img / \cf8 255.0\cf3  \cf4 # Normalizar\
# Predicci\'f3n\
\cf3 pred = model.predict(img.reshape(\cf8 1\cf3 , \cf8 28\cf3 , \cf8 28\cf3 , \cf8 1\cf3 ))\
clase = np.argmax(pred)\
confianza = np.\cf6 max\cf3 (pred)\
\cf4 # 4. Mostrar resultados con Umbral de Seguridad\
\cf3 st.subheader(\cf7 f\cf5 "Resultado: \cf3 \{clase\}\cf5 "\cf3 )\
\cf2 if\cf3  confianza < \cf8 0.80\cf3 :\
st.warning(\cf7 f\cf5 "Confianza baja (\cf3 \{confianza\cf8 :.2%\cf3 \}\cf5 ).\
\'bfPodr\'edas dibujar m\'e1s claro?"\cf3 )\
\cf2 else\cf3 :\
st.success(\cf7 f\cf5 "Confianza alta: \cf3 \{confianza\cf8 :.2%\cf3 \}\cf5 "\cf3 )\
st.bar_chart(pred[\cf8 0\cf3 ]) \cf4 # Visualizaci\'f3n de probabilidades}