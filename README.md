# Calculadora de Idade em Tkinter

Este é um código simples de uma **Calculadora de Idade** criada com a biblioteca `Tkinter` do Python. O aplicativo permite que o usuário insira uma data de nascimento e uma data inicial, e ele calculará a diferença entre as duas datas, exibindo o resultado em anos, meses e dias.

## Funcionalidades

- Interface gráfica utilizando o Tkinter.
- Calcula a diferença de idade entre uma data de nascimento e uma data atual selecionada pelo usuário.
- Exibe o resultado em **anos**, **meses** e **dias**.
- Uso de `tkcalendar` para escolher as datas facilmente.

## Requisitos

Para rodar este projeto, você precisa ter o Python e as seguintes bibliotecas instaladas:

- `tkinter`
- `tkcalendar`
- `dateutil`

Instale as dependências com o seguinte comando:

```bash
pip install tkcalendar python-dateutil
```

## Estrutura do Código

1. **Definição das Cores e Interface**
   O código define algumas cores para estilizar a interface do usuário. A janela principal possui um fundo escuro e os componentes são organizados em dois frames: o topo e o fundo.

2. **Frames e Widgets**
   - **top_frame**: Contém o título do aplicativo.
   - **bottom_frame**: Contém os campos de entrada para as datas e o botão de cálculo.
   - **Calendários**: Usamos `DateEntry` da biblioteca `tkcalendar` para permitir ao usuário selecionar as datas.
   - **Labels**: Para exibir os resultados (anos, meses e dias).
   - **Botão**: O botão "Calcular Idade" chama a função para calcular a diferença entre as datas e atualiza os resultados.

3. **Função de Cálculo**:
   A função `calculate_age()` usa a biblioteca `dateutil.relativedelta` para calcular a diferença entre as duas datas e atualizar os labels de exibição com os anos, meses e dias calculados.

## Como Usar

1. Abra o aplicativo.
2. Selecione a **Data Atual** e a **Data de Nascimento** usando os calendários.
3. Clique no botão **Calcular Idade** para ver o resultado.

## Exemplo de Uso

Após selecionar uma data de nascimento e uma data inicial, o aplicativo calculará a idade e exibirá o resultado como segue:

- **Anos**: 27
- **Meses**: 4
- **Dias**: 15

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Você pode criar uma **issue** ou enviar um **pull request** com suas modificações.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
