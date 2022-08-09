function devuelve(){
    return true;
}

async function promesa(){
    return setTimeout(()=> console.log("Hola, soy una promesa"), 5000);
}

function *pares(){
    let num =0;
    while(true){
        num+=2
    }
}