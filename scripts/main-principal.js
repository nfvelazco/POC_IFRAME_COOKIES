const NAME_COOKIE = 'cookiedemo'

// Objeto que quieres almacenar
var json_valor_por_defecto = {flag_novedad: false,id_producto: -1};

// Convertir el objeto a una cadena JSON
var valorCookie = JSON.stringify(json_valor_por_defecto);
Cookies.set(NAME_COOKIE, valorCookie); // Crea una cookie de sesión


// TODO: ver si tiene sentido persistir el ultimo valor recuperado
const setCookieFinishRender = ()=>{
    console.log(`Reestableciendo el valor por defecto de la coockie de session`)
    Cookies.set(NAME_COOKIE, valorCookie);
}

const render_producto = (valor) =>{
    $("#txtProducto").html(`Producto id: ${valor.id_producto}`)
}

$(document).ready(()=>{

    var checkCookie = setInterval(function() {
        var miCookie = Cookies.get(NAME_COOKIE); // Obtiene el valor de la cookie
        var valor = miCookie ? JSON.parse(miCookie) : undefined
        if((valor != undefined)&&(valor.flag_novedad)){
            // Ejecuta tu función aquí
            render_producto(valor);
            console.log(`El valor fue actualizado a: ${valor.id_producto}`)
            setCookieFinishRender();  
        } else {
            // Si la cookie no es 'false', detiene la iteración
            //clearInterval(checkCookie);
        }
    }, 500); // Intervalo de tiempo en milisegundos

})