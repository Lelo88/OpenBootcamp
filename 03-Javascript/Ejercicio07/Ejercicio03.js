const fechaActual = new Date()
console.log(fechaActual)

const fechaNac = new Date(1988, 6, 30,0,30)

console.log(fechaNac)

console.log(fechaActual.getTime()>fechaNac.getTime())

const diaNac = fechaNac.getDate()
const mesNac = fechaNac.getMonth() + 1
const anioNac = fechaNac.getFullYear()

console.log(diaNac)
console.log(mesNac)
console.log(anioNac)


