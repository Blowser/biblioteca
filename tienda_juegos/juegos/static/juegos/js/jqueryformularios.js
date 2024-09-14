$('#registroFormularioJS').submit(function(event) {
    let valid = true;

    const nombreCompleto = $('#nombreCompleto').val().trim();
    const nombreUsuario = $('#nombreUsuario').val().trim();
    const correo = $('#correo').val().trim();
    const contrasena = $('#contrasena').val().trim();
    const confirmarContrasena = $('#confirmarContrasena').val().trim();
    const fechaNacimiento = $('#fechaNacimiento').val().trim();
    const edad = new Date().getFullYear() - new Date(fechaNacimiento).getFullYear();

    // Validaciones aquí...

    if (!valid) {
        $('#mensajeErrorRegistro').text('Corrige los errores en el formulario');
        event.preventDefault();  // Solo detén el envío si hay errores
    } else {
        $('#mensajeErrorRegistro').text('');
    }

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
            //window.location.href = "iniciarsesion.html"; // REDIRECCIONAMOS A INICIAR SESIÓN
            window.location.href = iniciarSesionUrl;  // Redirigir a la URL generada por Django
        }else {
         $('#mensajeErrorRecuperacion').text('Por favor, corrige el formulario');}
    })

    // VALIDACIÓN FORM INICIO SESION
    $('#iniciarSesionFormularioJS').submit(function(event) {
        event.preventDefault();
        let valid = true;

        const usuario = $('#usuario').val().trim();
        const contrasena = $('#contrasena').val().trim();

        if (!usuario || usuario.length < 6) {
            $('#errorUsuarioSesion').text('El nombre de usuario debe tener al menos 6 caracteres');
            valid = false;
        } else {
            $('#errorUsuarioSesion').text('');
        }

        if (!contrasena || !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,18}$/.test(contrasena)) {
            $('#errorContrasenaSesion').text('La contraseña debe tener entre 6-18 caracteres, y al menos 1: mayúscula, minúscula, dígito y carácter especial');
            valid = false;
        } else {
            $('#errorContrasenaSesion').text('');
        }

        if (valid) {
            $('#mensajeErrorSesion').text('');
            alert('Inicio de sesión exitoso');
            //window.location.href = "modificarperfil.html"; // REDIRECCIONAMOS A MODIFICAR PERFIL
            window.location.href = modificarPerfilUrl;  // Redireccionamos a la URL de esta forma en Django
        } else {
            $('#mensajeErrorSesion').text('Por favor, corrige los errores en el formulario');
        }
    });
        // VALIDACIÓN FORM MODIFICAR PERFIL
     $('#modificarPerfilFormularioJS').submit(function(event) {
         event.preventDefault();
        let valid = true;
    
         const nombre = $('#nombre').val().trim();
         const apellido = $('#apellido').val().trim();
         const correo = $('#correo').val().trim();
         const telefono = $('#telefono').val().trim();
         const direccion = $('#direccion').val().trim();
         const mayusculaRegex = /[A-Z]/; //MINIMO UNA MAYUSCULA PARA LOS NOMBRES
    
         if (!nombre || !mayusculaRegex.test(nombre)) {
             $('#errorNombre').text('El nombre debe tener almenos una mayúscula');
             valid = false;
         } else {
             $('#errorNombre').text('');
         }
    
         if (!apellido || !mayusculaRegex.test(nombre)) {
            $('#errorApellido').text('El apellido es debe tener almenos una mayúscula');
             valid = false;
         } else {
            $('#errorApellido').text('');
         }
    
         if (!correo || !/^\S+@\S+\.\S+$/.test(correo)) {
             $('#errorCorreo').text('El correo electrónico es inválido');
             valid = false;
         } else {
             $('#errorCorreo').text('');
            }
    
         if (!telefono || !/^\d{9,15}$/.test(telefono)) {
             $('#errorTelefono').text('El número de teléfono debe tener entre 9 y 15 dígitos');
             valid = false;
         } else {
             $('#errorTelefono').text('');
            }
    
         if (!direccion) {
             $('#errorDireccion').text('La dirección es obligatoria');
             valid = false;
         } else {
             $('#errorDireccion').text('');
            }
    
         if (valid) {
             alert('Información guardada con éxito');
             $('#mensajeErrorModificarPerfil').text('');
         } else {
             $('#mensajeErrorModificarPerfil').text('Por favor, corrige los errores en el formulario');
         }
        
    });
    




});
