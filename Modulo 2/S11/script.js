function getJoke() {
    fetch('https://geek-jokes.sameerkumar.website/api?format=json')
      .then(response => response.json())
      .then(data => {
        const jokeElement = document.getElementById('joke');
        jokeElement.innerText = 'Translating...';
        fetch(`https://api-free.deepl.com/v2/translate?auth_key=<YOUR_AUTH_KEY>&text=${data.joke}&target_lang=ES`)
          .then(response => response.json())
          .then(translatedData => {
            jokeElement.innerText = translatedData.translations[0].text;
          })
          .catch(error => {
            console.error('Error:', error);
            jokeElement.innerText = 'Error translating joke :(';
          });
      })
      .catch(error => {
        console.error('Error:', error);
        jokeElement.innerText = 'Error getting joke :(';
      });
  }
  