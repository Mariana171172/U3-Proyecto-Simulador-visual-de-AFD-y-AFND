# Simulador Visual de AFD y AFND
## Universidad Politécnica De Victoria
**Ingeniería en Tecnologías de la Información**  
**Materia**: Lenguajes y Autómatas  
**Grupo**: ITI 7-1  
**Docente**: M.I. Lidia Ivaanery García Juárez  
**Ciudad Victoria, Tamaulipas, Agosto – Diciembre 2025

---

## Integrante
- Mariana Abigail Olvera Zúñiga  
(Matrícula: 2230409)

---

## Descripción del Proyecto
Este proyecto consiste en un **Simulador Visual de Autómatas Finitos Deterministas (AFD)** y **No Deterministas (AFND)**, desarrollado en **Python**, con interfaz gráfica creada en **Tkinter** y visualizaciones construidas mediante **NetworkX** + **Matplotlib**.

El sistema permite:
- 🧠 **Crear AFD y AFND** proporcionando alfabeto, estados, estado inicial, estados finales y transiciones.
- ▶️ **Simular cadenas** en AFD y AFND paso a paso.
- 🎨 **Visualizar automáticamente los autómatas** en forma de grafo dirigido.
- 🔍 **Comparar resultados** entre AFD y AFND usando la misma cadena.
- 🔎 **Mostrar cierres-ε**, múltiples transiciones y estados alcanzados.

Todo bajo una interfaz moderna con diseño personalizado.

---

## Justificación y Algoritmo
El proyecto busca facilitar la comprensión visual e interactiva de los autómatas finitos, sus transiciones y su comportamiento ante cadenas de entrada.
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

## Estructuras de Datos Utilizadas
- **Listas y Diccionarios**: Para representar estados, transiciones y cadenas.
- **Gráficos de red**: Usados para representar gráficamente los autómatas.
- **Cierre-ε**: Se calcula para AFND y visualiza los estados alcanzados por transiciones ε.

---

## Estructura del Proyecto
```plaintext
simulador_automatas/
│
├── main.py                             # Punto de inicio del simulador
│
├── gui/
│   ├── app.py                          # Ventana principal, estilos y tabs
│   ├── afd_tab.py                      # Pestaña del AFD
│   ├── afnd_tab.py                     # Pestaña del AFND
│   └── compare_tab.py                  # Comparación AFD vs AFND
│
├── automata/
│   ├── dfa.py                          # Implementación del AFD
│   └── nfa.py                          # Implementación del AFND
│
└── utils/
    ├── visualizer.py                   # Generación de gráficas (NetworkX)
    └── helpers.py                      # Funciones auxiliares como parse_set
```
