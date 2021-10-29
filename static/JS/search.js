var buscador = $("#table").DataTable();

$("#busqueda").keyup(function(){
    
    buscador.search($(this).val()).draw();
    
    if ($("#busqueda").val() == ""){
        $(".contenido").fadeOut();
    }else{
        $(".contenido").fadeIn();
    }
})