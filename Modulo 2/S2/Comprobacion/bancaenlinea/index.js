// Obtener elementos del formulario
const form = document.getElementById("login-form");
const usuario = document.getElementById("usuario");
const contrasena = document.getElementById("contrasena");

// Agregar evento de envío del formulario
form.addEventListener("submit", function(event) {
  // Validar que los campos no estén vacíos
  if (usuario.value === "" || contrasena.value === "") {
    alert("Por favor ingrese su nombre de usuario y contraseña");
    event.preventDefault();
    return;
  }

  // Validar que el nombre de usuario y la contraseña sean válidos
  if (!validarUsuario(usuario.value) || !validarContrasena(contrasena.value)) {
    alert("Nombre de usuario o contraseña no válidos");
    event.preventDefault();
    return;
  }

  // Si todo es válido, enviar el formulario
});

// Función para validar el nombre de usuario
function validarUsuario(usuario) {
  // Validar que el nombre de usuario tenga al menos 5 caracteres
  if (usuario.length < 5) {
    return false;
  }

  // Validar que el nombre de usuario contenga solo letras y números
  const regex = /^[a-zA-Z0-9]+$/;
  if (!regex.test(usuario)) {
    return false;
  }

  // Si pasa todas las validaciones, es un nombre de usuario válido
  return true;
}

// Función para validar la contraseña
function validarContrasena(contrasena) {
  // Validar que la contraseña tenga al menos 8 caracteres
  if (contrasena.length < 8) {
    return false;
  }

  // Validar que la contraseña contenga al menos una letra mayúscula, una minúscula y un número
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$/;
  if (!regex.test(contrasena)) {
    return false;
  }

  // Si pasa todas las validaciones, es una contraseña válida
  return true;
}