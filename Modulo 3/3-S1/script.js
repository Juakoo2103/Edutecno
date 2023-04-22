const toggleSwitch = document.querySelector('#dark-mode-toggle');

toggleSwitch.addEventListener('click', switchTheme, false);

function switchTheme() {
  document.body.classList.toggle('dark-mode');
  toggleSwitch.querySelector('.fa-sun').classList.toggle('d-none');
  toggleSwitch.querySelector('.fa-moon').classList.toggle('d-none');
}