document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('registroFormularioJS').addEventListener('submit', function(event) { 
        event.preventDefault(); // Detiene el envío del form y limpieza
        let valid = true; // Verificar que los campos del form sean correctos
        let mensajeError = '';
        
        const nombreCompleto = document.getElementById('nombreCompleto').value.trim();
        const nombreUsuario = document.getElementById('nombreUsuario').value.trim();
        const correo = document.getElementById('correo').value.trim();
        const contrasena = document.getElementById('contrasena').value.trim();
        const confirmarContrasena = document.getElementById('confirmarContrasena').value.trim();
        const fechaNacimiento = document.getElementById('fechaNacimiento').value.trim();
        const fechaactual = new Date();
        const edad = fechaactual.getFullYear() - new Date(fechaNacimiento).getFullYear();
        const mes = fechaactual.getMonth() - new Date(fechaNacimiento).getMonth();

        if (!nombreCompleto) {
            mensajeError = 'Tu nombre es obligatorio';
            document.getElementById('errorNombreCompleto').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorNombreCompleto').textContent = '';
        }

        if (!nombreUsuario) {
            mensajeError = 'El nombre de usuario es obligatorio';
            document.getElementById('errorNombreUsuario').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorNombreUsuario').textContent = '';
        }

        if (!correo || !/^\S+@\S+\.\S+$/.test(correo)) {
            mensajeError = 'El correo electrónico es inválido';
            document.getElementById('errorCorreo').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorCorreo').textContent = '';
        }
        
        if (!contrasena || !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{6,18}[^'\s]/.test(contrasena)) {
            mensajeError = 'La contraseña debe tener entre 6-18 caracteres, y al menos 1: mayúscula, minúscula, dígito y carácter especial';
            document.getElementById('errorContrasena').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorContrasena').textContent = '';
        }

        if (confirmarContrasena !== contrasena) {
            mensajeError = 'Las contraseñas no coinciden';
            document.getElementById('errorConfirmarContrasena').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorConfirmarContrasena').textContent = '';
        }

        if (edad < 13 || (edad === 13 && mes < 0)) {
            mensajeError = 'Debes tener al menos 13 años de edad para registrarte';
            document.getElementById('errorFechaNacimiento').textContent = mensajeError;
            valid = false;
        } else {
            document.getElementById('errorFechaNacimiento').textContent = '';
        }

        if (valid) {
            document.getElementById('mensajeError').textContent = '';
            alert('Formulario enviado con éxito');
        } else {
            document.getElementById('mensajeError').textContent = 'Por favor, corrige el formulario';
        }
    });
});

function limpiarFormulario(){
    document.getElementById('registroFormularioJS').reset();
    document.querySelectorAll('.text-danger').forEach(function(element){
        element.textContent = '';
    });
    document.getElementById('mensajeError').textContent = '';
}

