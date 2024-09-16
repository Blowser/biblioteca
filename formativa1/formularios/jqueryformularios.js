$(document).ready(function() {
        // VALIDACIÓN FORM CREAR CUENTA NUEVA
        $('#registroFormularioJS').submit(function(event) {
            let valid = true;
        
            const firstName = $('#first_name').val().trim();
            const lastName = $('#last_name').val().trim();
            const username = $('#username').val().trim();
            const email = $('#email').val().trim();
            const password1 = $('#password1').val().trim();
            const password2 = $('#password2').val().trim();
        
            // Validación de nombre
            if (!firstName || firstName.length < 2) {
                $('#errorFirstName').text('El nombre debe tener al menos 2 caracteres');
                valid = false;
            } else {
                $('#errorFirstName').text('');
            }
        
            // Validación de apellido
            if (!lastName || lastName.length < 2) {
                $('#errorLastName').text('El apellido debe tener al menos 2 caracteres');
                valid = false;
            } else {
                $('#errorLastName').text('');
            }
        
            // Validación de nombre de usuario
            if (!username || username.length < 6) {
                $('#errorUsername').text('El nombre de usuario debe tener al menos 6 caracteres');
                valid = false;
            } else {
                $('#errorUsername').text('');
            }
        
            // Validación de correo electrónico
            if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
                $('#errorEmail').text('Por favor, ingresa un correo válido');
                valid = false;
            } else {
                $('#errorEmail').text('');
            }
        
            // Validación de contraseña
            if (!password1 || !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,18}$/.test(password1)) {
                $('#errorPassword1').text('La contraseña debe tener entre 6-18 caracteres, incluyendo una mayúscula, una minúscula, un dígito y un carácter especial');
                valid = false;
            } else {
                $('#errorPassword1').text('');
            }
        
            // Validación de confirmación de contraseña
            if (password1 !== password2) {
                $('#errorPassword2').text('Las contraseñas no coinciden');
                valid = false;
            } else {
                $('#errorPassword2').text('');
            }
        
            if (!valid) {
                event.preventDefault();  // Solo detén el envío si hay errores
            }
        });
        

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
            window.location.href = "modificarperfil.html"; // REDIRECCIONAMOS A MODIFICAR PERFIL
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
