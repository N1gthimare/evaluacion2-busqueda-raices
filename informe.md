# Informe: La raíz que se esconde

**Evaluación 2: búsqueda de raíces y análisis de convergencia**  
Universidad Católica del Maule  
Integrantes:Ariel Gallardo-Manuel Fuentes.

> Todos los números de este informe provienen de la ejecución del script principal y sus respectivos conjuntos de datos.
> La informacion se puede obtener ejecutando el script en terminal o los valores especificos en la carpeta (scr\data) y (scr\assets)

---

## 1. Parametros para las funciones y metodos

Para todas las funciones: **tolerancia = 1e-6**, **tope = 100 iteraciones**, criterio de parada `|f(xₙ)| < tol` o `|xₙ − xₙ₋₁| < tol`.

---

## 2. Resultados

Los valores de las tablas pueden ser numericos o no aplicables,ya que no todos los metodos sirven para todas las funciones,las iteraciones hasta cumplir la tolerancia establecida son:

| Función | Bisección | Falsa posición | Punto fijo | Secante | Newton | Newton mejorado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| x³ − x − 2 | 20| 12 | 8 | 6 | 5 | 5 |
| (x − 2)² | No aplica | No aplica| No aplica| No aplica| 10| 1 |
| ln(x) + x − 4 | 19 | 4 |Agoto iteracion | 3| 3 | 3 |
| e^(−x) − x | 20 |7 | 26| 4 | 3| No valida |
| cos(x) − x | 20 | 5 | 35| 4 | 4 | No aplica |
| √x − cos(x) | 20 | 4 | Agoto iteracion| 3| 3| No aplica|

---

## 3. Preguntas de convergencia

### 3.1 ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?
Los metodos que mas convergieron en la menor cantidad de iteraciones fueron los siguiente,algunos tuvieron la misma cantidad por la cual para este caso son igual de eficientes.


| Función | Metodos | Iteraciones | 
| :--- | :--- | :--- |
| x³ − x − 2 | Newton Raphson y Newton Raphson Modificado| 5 |
| (x − 2)² | Newton RaphsonModificado | 1|
| ln(x) + x − 4 | Secante,Newton Raphson y Newton Raphson Modificado | 3 |
| e^(−x) − x | Newton Raphson| 3 | 
| cos(x) − x | Newton Raphson y secante| 4 | 
| √x − cos(x) | Secante y Newton Raphson | 3 | 

- **Raiz simple:**Newton-Raphson y Newton-Raphson Modificado presentan una convergencia cuadrática para las raíces simples,esto permite reducir rápidamente el error en cada iteración.
- **Raiz doble:**En raiz doble Newton Raphson pierde velocidad,por ello se utiliza Newton Modificado,este es usado para funciones con mayor multiplicidad,esto permite una convergencia mucho mayor respecto a otras.
- **Logaritmica:**Es este caso especifico la derivada de x>0 y no se anulan por ello los Newton Raphson son utilizables por su velocidad y la secante no necesita su derivada exacta.
- **Trigonometrica** Newton-Raphson converge rápidamente porque su derivada, $f'(x)=-\sin(x)-1$, no es cero en la raíz, lo que favorece la convergencia cuadrática. Por su parte, Secante aproxima la pendiente mediante dos puntos y alcanza una convergencia superlineal. Además, ambos métodos parten de aproximaciones iniciales adecuadas para esta función.

- **Mixta:** Newton-Raphson aprovecha que la función es derivable cerca de la raíz y que su derivada no es cero, permitiendo reducir rápidamente el error. Secante también obtiene buenos resultados porque aproxima la pendiente usando dos valores anteriores, evitando calcular derivadas explícitamente. En ambos casos, las aproximaciones iniciales favorecieron la convergencia en pocas iteraciones.

### 3.2 ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?


- **Bisección:** Tiene convergencia lineal como se puede apreciar en (scr\assets\errores_Logaritmica.png). El error disminuye progresivamente a medida que el intervalo se reduce a la mitad en cada iteración.

- **Newton-Raphson:** Tiene convergencia cuadrática cuando se aproxima a una raíz simple. Esto se refleja en una disminución rápida del error en pocas iteraciones.

- **Newton-Raphson Modificado:** Para raíces múltiples, puede recuperar la convergencia cuadrática. En el gráfico, el error disminuye rápidamente cuando el método funciona correctamente.

- **Punto Fijo:** Generalmente tiene convergencia lineal cuando se cumple la condición de convergencia. En el gráfico, el error disminuye gradualmente; si el método diverge, puede aumentar o presentar valores inválidos.

- **Secante:** Tiene convergencia superlineal, de orden aproximado 1.618 para raíces simples. El error disminuye rápidamente, aunque generalmente no tan rápido como Newton-Raphson.

- **Falsa Posición:** Su convergencia depende de la función y del intervalo inicial. Puede presentar un comportamiento lineal, pero también estancarse si uno de los extremos permanece fijo durante muchas iteraciones.

En los gráficos de error frente a iteraciones, los métodos convergentes muestran una tendencia descendente. Sin embargo, la rapidez y la forma de esa disminución dependen de la función, las aproximaciones iniciales y la tolerancia utilizada.

### 3.3 ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?
Metodos abiertos:Estos metodos no requieren un intervalo para poder evaluarlos,ya que solo necesitan un valor inicial para empezar a funcionar,pero si usan otros metodos como derivadas y dobles derivadas como los metodos de Newton Raphson y Newton Raphson Modificado.

Metodos cerrados:**Biseccion** y **Falsa posicion** estos metodos usan el cambio de signo,en caso de no ser posibles no se pueden evaluar como en el caso de polinomica de raiz doble,en la cual no se entrega un parametro b para realizar la comprobacion "f(a)*f(b)<0".


### 3.4 En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?
| Método | ¿Aplica / Funciona? | Por qué |
| :--- | :--- | :--- |
| **Bisección** | **No aplica** | La función $f(x) = (x-2)^2 \ge 0$ en todo $\mathbb{R}$, por lo que nunca cruza el eje $x$ y no existe un intervalo con cambio de signo para que cumpla el Teorema de bolzano
| **Falsa Posición** | **No aplica** | Al igual que la bisección, requiere obligatoriamente un cambio de signo en los extremos del intervalo, condición que tampoco cumple. |
| **Punto Fijo** | **Falla** | La funcion despejada no es valida para una convergencia dentro de los limites de las iteraciones |
| **Secante** | **No aplica** | La funcion de raiz doble no tiene 2 valores por lo cual el metodo de la secante no puede iniciar sin los 2 valores iniciales. |
| **Newton-Raphson** | **Converge** | Encuentra la raíz, pero **pierde su convergencia cuadrática clásica**, reduciendo su velocidad a lineal debido a que la derivada en la raíz doble es cero. |
| **Newton-Raphson Modificado** | **Funciona perfecto (1 iteración)** | Está diseñado algebraicamente para raíces múltiples. Al incorporar la primera y segunda derivada en su fórmula, corrige el problema que se tiene con un denominador y obtiene el valor con una velocidad incomparable a las demas. |


Estos casos se pueden observar en nuestro grafico (`src/assets/errores_Polinomica_(Raiz doble).png`) el cual solo se muestran los dos metodos funcionales en nuestro caso.
### 3.5 ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?

**Métodos cerrados:**

- **Bisección:** Utilizar un intervalo cuyos extremos tengan signos opuestos permite garantizar la convergencia, siempre que la función sea continua en dicho intervalo. La amplitud inicial influye en la cantidad de iteraciones, ya que un intervalo más amplio requiere más divisiones para alcanzar la tolerancia deseada. La cantidad aproximada de iteraciones se calcula mediante:

    n ≥ log₂((b − a) / tolerancia)
  Por lo tanto, aumentar el ancho del intervalo incrementa las iteraciones necesarias, pero no compromete la convergencia si se cumplen las condiciones del método.

- **Falsa posición:** También requiere un intervalo cuyos extremos tengan signos opuestos y una función continua. Sin embargo, su convergencia puede ser más lenta que la de bisección, ya que uno de los extremos puede permanecer prácticamente fijo durante varias iteraciones. Esto provoca estancamiento y puede hacer que no se alcance la tolerancia dentro del máximo de iteraciones establecido.

**Métodos abiertos:**

- **Punto fijo:** La convergencia depende principalmente de la transformación \(x=g(x)\) elegida y del valor inicial. Una condición suficiente para la convergencia local es que \(|g'(r)|<1\) cerca de la raíz \(r\). En la función mixta, el método agotó las iteraciones (`src/assets/resumen_iteraciones.png`), lo que indica que no alcanzó la tolerancia establecida. Esto puede relacionarse con una transformación poco favorable, aunque no basta con ese resultado para afirmar que la derivada en la raíz sea mayor o igual a 1.


- **Secante:** No requiere calcular derivadas y utiliza dos estimaciones iniciales para aproximar la pendiente de la función. La elección de estos puntos influye en su convergencia: si se encuentran en zonas poco favorables o generan una pendiente muy pequeña, el método puede oscilar, avanzar lentamente o fallar. Por ejemplo, en la función con raíz doble, el método no logró converger con los valores iniciales utilizados.

- **Newton-Raphson:** Depende considerablemente de la estimación inicial, que en este proyecto corresponde al extremo \(a\) del intervalo. Si la derivada es cercana a cero en alguna iteración, el cálculo puede producir pasos muy grandes, alejarse de la raíz o salir del dominio de la función. Por ello, una estimación inicial adecuada favorece la convergencia y puede reducir la cantidad de iteraciones lo cual ocurrio en la funcion mixta la cual se puede observar en las comparaciones (`src/assets/resumen_iteraciones.png`).

- **Newton-Raphson modificado:** Está diseñado para mejorar el comportamiento de Newton-Raphson cuando existen raíces múltiples. Su convergencia depende de la estimación inicial, de las derivadas utilizadas y de que estas puedan evaluarse correctamente. Cuando las condiciones son favorables, puede converger rápidamente incluso ante una raíz doble (`src/assets/errores_Polinomica_(Raiz doble).png`); sin embargo, una estimación inicial inadecuada o derivadas nulas o no válidas pueden provocar que el método falle como ocurrio en la funcion mixta.


### 3.6 ¿Qué método recomiendan según el tipo de función?
| Función | Método recomendado | Fundamento |
|---|---|---|
| $x^3-x-2$ | Newton-Raphson | Converge rápidamente porque la función es de  raíz simple y su derivada permite mejorar la aproximación en cada paso de la iteración. |
| $(x-2)^2$ | Newton-Raphson Modificado | Es el mas adecuado para las raíces dobles,debido a que  mejora la velocidad de convergencia y obtiene una aproximación precisa en pocas iteraciones en comparacion a otros. |
| $\ln(x)+x-4$ | Newton-Raphson | Saca mas valor a la derivada de la función para encontrar la raíz de manera mas rapida y con buena precisión. |
| $e^{-x}-x$ | Newton-Raphson | Encuentra la raíz en pocas iteraciones gracias a su rápida convergencia para raíces simples. |
| $\cos(x)-x$ | Newton-Raphson | Utiliza la derivada para mejorar la aproximación obteniendo un valor mas preciso y converge rápidamente hacia la raíz. |
| $\sqrt{x}-\cos(x)$ | Secante | Permite encontrar la raíz en pocas iteraciones sin necesidad de calcular la derivada de la función y no debe limitarse por el intervalo de signo en comparacion a falsa posicion. |

---

## 4. Conclusión
**¿Qué método elegirían para cada tipo de función y por qué (velocidad vs. robustez)?**

En nuestro caso, preferimos el método de **bisección cuando se prioriza la robustez**, ya que presentó un comportamiento predecible y permitió obtener resultados consistentes en las funciones que cumplían sus condiciones de aplicación. Aunque generalmente requiere más iteraciones que los métodos abiertos, su principal ventaja es que permite controlar el intervalo en el que se encuentra la raíz.

Sin embargo, no es el método más adecuado para todos los casos. Por ejemplo, ante una raíz doble, bisección no puede aplicarse mediante el criterio habitual de cambio de signo. En esa situación, elegiríamos Newton-Raphson modificado, ya que está diseñado para trabajar con raíces múltiples y, en nuestras pruebas, obtuvo la solución en una sola iteración. En general, la elección depende de las características de la función: preferimos bisección cuando buscamos robustez y métodos como Newton-Raphson cuando buscamos rapidez y se cumplen sus condiciones de convergencia.

**¿Qué ocurrió en la raíz doble y qué dice eso sobre «tener raíz» frente a «cambiar de signo»?**

En la función con raíz doble, \((x-2)^2\), la gráfica toca el eje \(x\) en \(x=2\), pero no lo cruza. Esto ocurre porque la función es no negativa a ambos lados de la raíz, por lo que no existe un cambio de signo en el intervalo considerado.

Esto demuestra que una función puede tener una raíz sin que sus valores cambien de signo. El cambio de signo es una condición que permite aplicar los métodos de bisección y falsa posición bajo sus condiciones habituales, pero no es un requisito para que exista una raíz. Por esta razón, estos métodos no pudieron encontrar la raíz doble con el intervalo utilizado, mientras que Newton-Raphson modificado sí logró aproximarla a una gran velocidad de solo una iteracion con el metodo.

**¿Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?**

En nuestro proyecto no registramos sistemáticamente los resultados al modificar los intervalos y las estimaciones iniciales, por lo que no podemos establecer una comparación general sobre cuánto cambiaron las iteraciones. Sin embargo, observamos que Newton-Raphson puede mejorar su comportamiento cuando se utiliza una estimación inicial más favorable, ya que esta influye directamente en los pasos que realiza el método.

En los métodos cerrados, como bisección, el ancho del intervalo inicial influye en la cantidad de iteraciones necesarias para alcanzar la tolerancia. No obstante, modificar el intervalo no resuelve el problema de la raíz doble si los extremos continúan sin presentar un cambio de signo. En los métodos abiertos, una estimación inicial adecuada puede favorecer la convergencia y reducir las iteraciones, mientras que una elección desfavorable puede provocar lentitud o divergencia pero aun asi llegar al resultado dentro del valor de 100 iteraciones.