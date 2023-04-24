export default function getDigimonData() {
  return fetch("https://digimon-api.vercel.app/api/digimon")
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error("Error en la conexión a la API de Digimon");
    })
    .catch((error) => {
      console.error(error);
    });
}
