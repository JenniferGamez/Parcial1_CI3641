let c = 4;

function R(a) {
  if (a < 5) {
    return R(a + 2);
  } else {
    return a;
  }
}

c = 1;
const resultado = R(c);

console.log(resultado); // Esto imprimirá 5, que es el valor final
