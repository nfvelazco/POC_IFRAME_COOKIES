
const NAME_COOKIE = 'cookiedemo'
var json_valor_por_defecto = {flag_novedad: true,id_producto: -1};

$(document).ready(()=>{
    $('.buttons').click((e)=>{
        var producto_id = $(e.target).attr('product');
        // Objeto que quieres almacenar
        json_valor_por_defecto.id_producto = producto_id;
        // Convertir el objeto a una cadena JSON
        var valorCookie = JSON.stringify(json_valor_por_defecto);
        Cookies.set(NAME_COOKIE, valorCookie); // Crea una cookie
    })
})