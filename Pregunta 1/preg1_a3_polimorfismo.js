class Animal {
    hablar() {
      throw new Error('No se ha implementado el método.');
    }
  }
  
class Perro extends Animal {
    hablar() {
        console.log('El perro ladra');
    }
}

const miAnimal = new Animal();
const miPerro = new Perro();

miPerro.hablar(); // Imprime 'El perro ladra'
  