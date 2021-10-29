function validar_formulario(){
    var pass1 = document.getElementById('pass1');
    var pass2 = document.getElementById('pass2');

    if (pass1.value!= pass2.value) {
 
        // Si las constraseñas no coinciden mostramos un mensaje
        document.getElementById("error").classList.add("mostrar");
     
        return true;
    }
     
    else {
     
        // Si las contraseñas coinciden ocultamos el mensaje de error
        document.getElementById("error").classList.remove("mostrar");
     
        // Mostramos un mensaje mencionando que las Contraseñas coinciden
        document.getElementById("ok").classList.remove("ocultar");
		
		document.getElementById("resgistrarse").addEventListener("click");
		
    }

}   

function mostar1(){
    var pwd = document.getElementById("pass1");
    pwd.type="text"
}
function ocultar1(){
    var pwd = document.getElementById("pass1");
    pwd.type="password"
}
function mostar2(){
    var pwd = document.getElementById("pass2");
    pwd.type="text"
}
function ocultar2(){
    var pwd = document.getElementById("pass2");
    pwd.type="password"
}