const persona = {
    nombre: 'Leandro',
    apellido: 'Villalba',
    edad: 34,
    altura: 185,
    eresDesarrollador: true
}

const edad = persona['edad']

console.log(edad)

const listado = [
    {...persona
    },
    {
        nombre: 'Maxi',
        apellido: 'Gaitán',
        edad: 30,
        altura: 180,
        eresDesarrollador: true
    },
    {
        nombre: 'Florencia',
        apellido: 'Lico',
        edad: 33,
        altura: 170,
        eresDesarrollador: false
    }
]

const listaOrdenada = listado.sort((a,b) => b.edad - a.edad)

console.log(listaOrdenada)