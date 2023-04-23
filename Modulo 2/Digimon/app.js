// Obtener el contenedor de las cartas
var digimonList = document.getElementById("digimon-list");

// Hacer una petición GET a la API de Digimon
fetch("https://digimon-api.vercel.app/api/digimon")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    // Crear una tarjeta para cada Digimon y añadirla al contenedor
    data.forEach(function (digimon) {
      var card = document.createElement("div");
      card.className = "col-sm-12 col-md-4 col-lg-3";

      var innerHTML = `
        
        <div class="card">
          <img src="${digimon.img}" class="card-img-top" alt="${digimon.name}">
          <div class="card-body">
            <h5 class="card-title">${digimon.name}</h5>
            <p class="card-text">${digimon.level}</p>
          </div>
        </div>
        
      `;
      card.innerHTML = innerHTML;

      digimonList.appendChild(card);
    });
  })
  .catch(function (error) {
    console.error("Error:", error);
  });
