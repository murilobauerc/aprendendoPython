arquivo = open('pythonWeb.html', 'w' , encoding = 'utf-8') # encoding p/ mostrar caracteres especiais
arquivo.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title> Redes de Computadores </title>
</head>
<body>
<div id="caixas" class="thread">
          <img width="50px" src="https://image.flaticon.com/icons/svg/182/182321.svg" alt="picture"/>
          <h2> Apenas a história de como realizar uma marcação de texto através do Python! Mágico! </h2>
</div>
</body>
</html>''')
arquivo.close()
