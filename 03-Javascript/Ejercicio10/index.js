import * as controller from './moduloEjercicio/controller.js'
import chalk from 'chalk';

const suma1 = controller.suma(1,2);;
const suma2 = controller.suma(4,5);
const multiplica = controller.multiplica(suma1, suma2); 

console.log(suma1)
console.log(suma2)
console.log(chalk.green(multiplica))

