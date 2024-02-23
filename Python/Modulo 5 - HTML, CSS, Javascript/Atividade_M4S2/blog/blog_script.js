document.querySelectorAll('a.stretched-link').forEach(function(btn) {
    btn.addEventListener('click', function(event) {
      event.preventDefault();
      alert("Este produto está em falta. :(");
    });
  });