$(document).ready(function() {
    $("#trabajoForm").on("submit", function(event) {
        event.preventDefault();

        let isValid = true;
        const user = $("#User").val();
        const clave = $("#Clave").val();

        if (user.length < 3 || user.length > 15) {
            alert("El Username debe tener entre 3 y 15 caracteres.");
            isValid = false;
        }


        if (clave.length < 3 || clave.length > 8) {
            alert("La contraseña debe tener entre 3 y 8 caracteres.");
            isValid = false;
        }

        if (isValid) {
            alert("Formulario enviado correctamente.");
            this.submit();
        }
    }); 
});