document.addEventListener("DOMContentLoaded", function(){

let botonesEliminar = document.querySelectorAll(".eliminar");

botonesEliminar.forEach(function(boton){

    boton.addEventListener("click", function(e){

        let confirmar = confirm("¿Seguro que quieres eliminar este producto?");

        if(!confirmar){
            e.preventDefault();
        }

    });

});

});