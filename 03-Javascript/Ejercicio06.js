const listaCompras = ['Arroz', 'Fideos', 'Huevos', 'Azucar', 'Cafe']

//agrego producto
listaCompras.push('Aceite de girasol')

//saco producto
listaCompras.pop('Aceite de girasol')

//listado de peliculas como objetos
const listaPeliculas = [
    pelicula1 = {
        titulo: 'Arma Mortal',
        director: 'Mel Gibson',
        fecha: new Date(1988, 6, 12)
    },
    pelicula2 = {
        titulo: 'Avengers',
        director: 'Sam Raimi',
        fecha: new Date(2012, 5, 14)
    },
    pelicula3 = {
        titulo: 'Iron Man',
        director: 'James Gunn',
        fecha: new Date(2007, 8, 8)
    }
]

//filtrar peliculas por fecha de estreno
const pelisNuevas = listaPeliculas.filter(pelicula => pelicula.fecha > new Date (2010,0,1))

const direPelis = listaPeliculas.map(director => {
    return director.director;
})

const nombrePelis = listaPeliculas.map(nombres =>{
    return nombres.titulo
})

const directores = direPelis.concat(nombrePelis)

const directores2 = [...direPelis,...nombrePelis]
