let factorial = 1;
for (let i = 10; i > 0; i--) {
    factorial *= i;
    if (i==1){
        break;
    }
}
console.log(factorial) // Factorial de 10 = 3628800