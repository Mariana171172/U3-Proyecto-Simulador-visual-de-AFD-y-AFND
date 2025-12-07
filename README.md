# Simulador Visual de AFD y AFND
## Universidad Politécnica De Victoria
**Ingeniería en Tecnologías de la Información**  
**Materia**: Lenguajes y Autómatas  
**Grupo**: ITI 7-1  
**Docente**: M.I. Lidia Ivaanery García Juárez  
**Ciudad Victoria, Tamaulipas, Agosto – Diciembre 2025

---

## 🧑‍💻 Integrante
- Mariana Abigail Olvera Zúñiga  
(Matrícula: 2230409)

---

## 📌 Descripción del Proyecto
Este proyecto desarrolla un **simulador visual** que permite a los usuarios crear y simular **Autómatas Finitos Deterministas (AFD)** y **Autómatas Finitos No Deterministas (AFND)**. El simulador facilita la comprensión de cómo estos autómatas procesan cadenas de símbolos y permite comparar el comportamiento de ambos modelos.

### Funcionalidades:
- **Creación de AFD y AFND**: El usuario ingresa alfabeto, estados, transiciones y observa cómo los autómatas procesan cadenas.
- **Simulación de cadenas**: Proceso paso a paso para verificar la aceptación o rechazo de una cadena.
- **Comparación AFD vs AFND**: Comparación paralela de la ejecución de una misma cadena entre AFD y AFND.

---

## 🧠 Justificación y Algoritmo
El simulador permite visualizar la simulación de autómatas para enseñar de manera interactiva los conceptos de los **lenguajes regulares**. Implementa dos tipos de autómatas (AFD y AFND), destacando sus diferencias en cómo procesan las cadenas.  
### Beneficio educativo:
- **Estudio práctico**: Permite estudiar el funcionamiento de los autómatas de manera práctica e interactiva.
- **Visualización clara**: Muestra gráficamente las rutas, transiciones y cierres-ε, facilitando la comprensión del proceso interno.
- **Facilita el aprendizaje**: Ayuda a entender la teoría de cómputo y lenguajes formales de forma más accesible y dinámica.

### Estructura interna del simulador:
- **AFD (Autómata Finito Determinista)**: Tiene una única transición definida por cada símbolo del alfabeto.
- **AFND (Autómata Finito No Determinista)**: Permite múltiples transiciones por símbolo y hace uso de **transiciones ε**, lo que permite moverse entre estados sin consumir símbolos.

### Algoritmos implementados:

#### **Simulación AFD**
- El AFD sigue un recorrido **lineal** por cada símbolo.
- Para cada par de **estado actual** y **símbolo leído**, se realiza una **transición única** a un solo estado.
- **Complejidad computacional**: **O(n)**, donde **n** es la longitud de la cadena procesada.

#### **Simulación AFND**
- El AFND maneja **conjuntos de estados activos** y permite **múltiples transiciones simultáneas**.
- Se implementa el cálculo **recursivo del cierre-ε**, permitiendo que el autómata realice transiciones sin consumir símbolos.
- **Complejidad computacional**: **O(n × m)**, donde **n** es la longitud de la cadena y **m** es el número de estados del autómata.


---

## 🧰 Estructuras de Datos Utilizadas
- **Listas y Diccionarios**: Para representar estados, transiciones y cadenas.
- **Gráficos de red**: Usados para representar gráficamente los autómatas.
- **Cierre-ε**: Se calcula para AFND y visualiza los estados alcanzados por transiciones ε.

---

## 📂 Estructura del Proyecto
