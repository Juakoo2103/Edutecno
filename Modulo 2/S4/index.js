$(document).ready(function() {
    $("form").submit(function(event) {
      event.preventDefault(); // Evita el comportamiento predeterminado del formulario
  
      // Obtener los valores de los elementos de formulario
      var nombre = $("#nombre").val();
      var email = $("#email").val();
      var asistentes = $("#asistentes").val();
  
      // Concatenar los valores en una cadena de texto
      var mensaje ="Estimado/a"+ nombre + "agradecemos por reservar con nosotros. Hemos"+ "\n" +
                    "registrado" + asistentes + "se ha enviado el codigo de confirmacion al"+ "\n" +
                    "correo" + email + "\n" +
                    "Gracias por preferirnos"
  
      // Mostrar la cadena de texto en un alert
      alert(mensaje);
    });
    // Validacion de form
    $("#form").validate({
        rules: {
          name: {
            required: true
          },
          email: {
            required: true,
            email: true
          }
        
        },
        messages: {
          name: {
            required: "Por favor ingrese su nombre."
          },
          email: {
            required: "Por favor ingrese su correo electrónico.",
            email: "Por favor ingrese un correo electrónico válido."
          }
        }
      });
      
  });