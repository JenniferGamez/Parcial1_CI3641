// FUNCIONES

// Funcion que construye una matriz transpuesta dada una matriz cambiando las filas por columnas.
function matrizTranspuesta(matriz) {
    const filas = matriz.length;
    const columnas = matriz[0].length;
  
    // Crear una nueva matriz para almacenar la matriz transpuesta.
    const matrizT = [];
    for (let i = 0; i < columnas; i++) {
        matrizT[i] = [];
    }
  
    // Llenar la matriz transpuesta intercambiando filas y columnas.
    for (let i = 0; i < filas; i++) {
      for (let j = 0; j < columnas; j++) {
        matrizT[j][i] = matriz[i][j];
      }
    }
  
    return matrizT;
}

// Función para mostrar la matriz en la consola
function mostrarMatriz(matriz) {
    for (let i = 0; i < matriz.length; i++) {
      console.log(matriz[i].join(" ")); // Imprimir fila como cadena
    }
}

// funcion que multiplica dos matrices A y B
/*      La multiplicación de matrices se da solo cuando m x n * n x l, 
        siendo el número de columnas en la primera matriz debe ser igual 
        al número de renglones en la segunda matriz.
*/
function multiplicarMatrices(A, B){
    const A_m = A.length;
    const A_n = A[0].length;
    const B_m = B.length;
    const B_n = B[0].length;
    
    // Verificar si las matrices son multiplicables
    if (A_n !== B_m) {
        return "No se pueden multiplicar, dimensiones incorrectas.";
    }

    // Inicializar una matriz nueva para el resultado A x B
    const resultado = new Array(A_m);

    for (let i = 0; i < A_m; i++) {
        resultado[i] = new Array(B_n);
        for (let j = 0; j < B_n; j++) {
          resultado[i][j] = 0;
          for (let k = 0; k < A_n; k++) {
            resultado[i][j] += A[i][k] * B[k][j];
          }
        }
      }
    
    return resultado;
}


// MAIN 

// Ejemplo de uso:

const A = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]];

const A_transpuesta = matrizTranspuesta(A);

const resultado = multiplicarMatrices(A, A_transpuesta);

// SALIDA

console.log("Matriz A:");
mostrarMatriz(A)

console.log("Matriz At:");
mostrarMatriz(A_transpuesta);

console.log("Resultado A x A_transpuesta:");
console.log(resultado);
mostrarMatriz(resultado);