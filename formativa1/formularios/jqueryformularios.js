$(document).ready(function() {
        // VALIDACIÓN FORM CREAR CUENTA NUEVA
    $('#registroFormularioJS').submit(function(event) {
        event.preventDefault(); // Detiene el envío del formulario por defecto
        let valid = true;

        const nombreCompleto = $('#nombreCompleto').val().trim();
        const nombreUsuario = $('#nombreUsuario').val().trim();
        const correo = $('#correo').val().trim();
        const contrasena = $('#contrasena').val().trim();
        const confirmarContrasena = $('#confirmarContrasena').val().trim();
        const fechaNacimiento = $('#fechaNacimiento').val().trim();
        const fechaactual = new Date();
        const edad = fechaactual.getFullYear() - new Date(fechaNacimiento).getFullYear();
        const mes = fechaactual.getMonth() - new Date(fechaNacimiento).getMonth();

        if (!nombreCompleto) {
            $('#errorNombreCompleto').text('Tu nombre es obligatorio');
            valid = false;
        } else {
            $('#errorNombreCompleto').text('');
        }

        if (!nombreUsuario) {
            $('#errorNombreUsuario').text('El nombre de usuario es obligatorio');
            valid = false;
        } else {
            $('#errorNombreUsuario').text('');
        }

        if (!correo || !/^\S+@\S+\.\S+$/.test(correo)) {
            $('#errorCorreo').text('El correo electrónico es inválido');
            valid = false;
        } else {
            $('#errorCorreo').text('');
        }

        if (!contrasena || !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,18}$/.test(contrasena)) {
            $('#errorContrasena').text('La contraseña debe tener entre 6-18 caracteres, y al menos 1: mayúscula, minúscula, dígito y carácter especial');
            valid = false;
        } else {
            $('#errorContrasena').text('');
        }

        if (confirmarContrasena !== contrasena) {
            $('#errorConfirmarContrasena').text('Las contraseñas no coinciden');
            valid = false;
        } else {
            $('#errorConfirmarContrasena').text('');
        }

        if (edad < 13 || (edad === 13 && mes < 0)) {
            $('#errorFechaNacimiento').text('Debes tener al menos 13 años de edad para registrarte');
            valid = false;
        } else {
            $('#errorFechaNacimiento').text('');
        }

        if (valid) {
            $('#mensajeErrorRegistro').text('');
            alert('Formulario enviado con éxito');
            window.location.href = "modificarperfil.html"; // REDIRECCIONAMOS A MODIFICAR PERFIL
        
        } else {
            $('#mensajeErrorRegistro').text('Por favor, corrige los errores en el formulario');
        }
    });

    // Función para limpiar el formulario y los mensajes de error
    window.limpiarFormulario = function() {
        $('#registroFormularioJS')[0].reset();
        $('.text-danger').text('');
        $('#mensajeError').text('');
    }


    // VALIDACIÓN FORM RECUPERAR CONTRASEÑA
    $('#recuperarContrasenaFormularioJS').submit(function(event) {
        event.preventDefault();
        let valid = true;
        const correo = $('#correo').val().trim();

        if (!correo|| !/^\S+@\S+\.\S+$/.test(correo)) {
            $('#errorCorreoRecuperacion').text('Por favor, ingresa un correo válido');
            valid = false;
        } else {
            $('#errorCorreoRecuperacion').text('');}

        if (valid) {
            $('#mensajeErrorRecuperacion').text('');
            alert('Enlace de recuperación enviado con éxito');
            window.location.href = "iniciarsesion.html"; // REDIRECCIONAMOS A INICIAR SESIÓN
        }else {
         $('#mensajeErrorRecuperacion').text('Por favor, corrige el formulario');}



    })






});
