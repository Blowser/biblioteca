$('#registroFormularioJS').submit(function(event) {
    let valid = true;

    const firstName = $('#first_name').val().trim();
    const lastName = $('#last_name').val().trim();
    const username = $('#username').val().trim();
    const email = $('#email').val().trim();
    const password1 = $('#password1').val().trim();
    const password2 = $('#password2').val().trim();

    // Limpiar mensajes de error previos
    $('.error-message').text('');

    // Validación de nombre
    if (!firstName || firstName.length < 2) {
        $('#errorFirstName').text('El nombre debe tener al menos 2 caracteres');
        valid = false;
    }

    // Validación de apellido
    if (!lastName || lastName.length < 2) {
        $('#errorLastName').text('El apellido debe tener al menos 2 caracteres');
        valid = false;
    }

    // Validación de nombre de usuario
    if (!username || username.length < 6) {
        $('#errorUsername').text('El nombre de usuario debe tener al menos 6 caracteres');
        valid = false;
    }

    // Validación de correo electrónico
    if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
        $('#errorEmail').text('Por favor, ingresa un correo válido');
        valid = false;
    }

    // Validación de contraseña
    if (!password1 || !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,18}$/.test(password1)) {
        $('#errorPassword1').text('La contraseña debe tener entre 6-18 caracteres, incluyendo una mayúscula, una minúscula, un dígito y un carácter especial');
        valid = false;
    }

    // Validación de confirmación de contraseña
    if (password1 !== password2) {
        $('#errorPassword2').text('Las contraseñas no coinciden');
        valid = false;
    }

    if (!valid) {
        event.preventDefault();  // Detener el envío si hay errores
    }
})

        // VALIDACIÓN FORM MODIFICAR PERFIL
        $('#modificarPerfilFormularioJS').submit(function(event) {
            event.preventDefault();  // Prevenir el envío por defecto del formulario
            let valid = true;
        
            const nombre = $('#nombre').val().trim();
            const apellido = $('#apellido').val().trim();
            const correo = $('#correo').val().trim();
            const mayusculaRegex = /[A-Z]/; // Expresión regular para al menos una mayúscula
        
            // Validación de nombre (debe contener al menos una mayúscula)
            if (!nombre || !mayusculaRegex.test(nombre)) {
                $('#errorNombre').text('El nombre debe tener al menos una mayúscula');
                valid = false;
            } else {
                $('#errorNombre').text('');
            }
        
            // Validación de apellido (debe contener al menos una mayúscula)
            if (!apellido || !mayusculaRegex.test(apellido)) {
                $('#errorApellido').text('El apellido debe tener al menos una mayúscula');
                valid = false;
            } else {
                $('#errorApellido').text('');
            }
        
            // Validación de correo electrónico
            if (!correo || !/^\S+@\S+\.\S+$/.test(correo)) {
                $('#errorCorreo').text('El correo electrónico es inválido');
                valid = false;
            } else {
                $('#errorCorreo').text('');
            }
        
            // Si todas las validaciones pasan, enviamos el formulario
            if (valid) {
                $('#modificarPerfilFormularioJS')[0].submit();  // Enviar el formulario si es válido
                $('#mensajeErrorModificarPerfil').text('');
            } else {
                $('#mensajeErrorModificarPerfil').text('Por favor, corrige los errores en el formulario');
            }
        });





