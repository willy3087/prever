document.getElementById('iniciar').addEventListener('click', function() {
  const nomeTarefa = document.getElementById('nome_tarefa').value;
  const nomeDesigner = document.getElementById('nome_designer').value;
  const complexidade = document.getElementById('complexidade').value;
  const tempo_estimado = document.getElementById('tempo_estimado').value;

  fetch('/prever', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          nome_tarefa: nomeTarefa,
          nome_designer: nomeDesigner,
          complexidade: complexidade,
          tempo_estimado: tempo_estimado
      })
  })
  .then(response => {
    if (response.headers.get("content-type").includes("application/json")) {
        return response.json();
    } else {
        throw new Error('Não é JSON');
    }
  })
  .then(data => {
      console.log(data);
      document.getElementById('resultado').innerText = data.entropia_predita;
  })
  .catch(error => console.error('Erro:', error));
});

document.getElementById('limpar').addEventListener('click', function() {
  document.getElementById('nome_tarefa').value = '';
  document.getElementById('nome_designer').value = '';
  document.getElementById('complexidade').value = '';
  document.getElementById('tempo_estimado').value = '';
  document.getElementById('resultado').innerText = '';
});
