// Crear un nombre con un valor asignado
const x = { valor: 42 };

// Crear un alias y utilizando asignación
const y = x;

console.log(y.valor); // Tanto x como y apuntan al mismo valor

// Modificar el objeto a través de cualquiera de los nombres
y.valor = 100;
console.log(x.valor); // Imprimirá 100