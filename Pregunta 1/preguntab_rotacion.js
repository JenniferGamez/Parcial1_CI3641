function rotar(w, k){
    if (k===0 && w.length > 0){
        return w;
    } else if (k > 0 && w.length > 0){
        const a = w.slice(0, 1);
        const x = w.slice(1, w.length);
        return rotar(x + a, k - 1);
    } else {
        return "Entrada no válida";
    }
}  

// Uso
const w = 'hola';

for (var k = 0 ; k< 6; k++){
    const resultado = rotar(w, k);
    console.log("Con k = "+ k + " el resultado es " + resultado);
}
