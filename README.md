# Supermarket API
Este projeto representa o trabalho final para o curso de Programação Web I. Consiste em uma API desenvolvida com o framework Flask, destinada à gestão de estoque em um ambiente de supermercado.

## 🛒 Visão Geral
A API do Sistema de Estoque de Supermercado foi projetada para fornecer operações completas de CRUD (Criar, Ler, Atualizar, Excluir) relacionadas à administração de estoques em supermercados. Ao aderir aos princípios RESTful, nossa API oferece uma interface limpa, precisa e altamente interativa para lidar com todos os aspectos dos recursos de estoque. Você pode ler o escopo inicial do projeto [aqui](https://drive.google.com/file/d/1HjxuHSuxDgFZJ3w0GWennRiMm1EUZ2ED/view).

## 🔀 Rotas
<details>
<summary><strong>Products</strong></summary>
<br><p>Essa rota tem como objetivo a administração da entidade produtos</p>
<table>
    <thead>
        <tr>
            <th>Requisição</th>
            <th>Rota</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/products</td>
            <td>Buscar todos os produtos</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/products</td>
            <td>Cadastrar um novo produto</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td>/products/&#123;id&#125;</td>
            <td>Editar um produto já existente</td>
        </tr>
         <tr>
            <td>DELETE</td>
            <td>/products/&#123;id&#125;</td>
            <td>Deletar um produto já existente</td>
        </tr>
    </tbody>
</table>     
</details>

<details>
<summary><strong>Category</strong></summary>
<br><p>Essa rota tem como objetivo a administração da entidade categorias</p>
<table>
    <thead>
        <tr>
            <th>Requisição</th>
            <th>Rota</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/categories</td>
            <td>Buscar todas as categorias</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/categories</td>
            <td>Cadastrar uma nova categoria</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td>/categories/&#123;id&#125;</td>
            <td>Editar uma categoria já existente</td>
        </tr>
         <tr>
            <td>DELETE</td>
            <td>/categories/&#123;id&#125;</td>
            <td>Deletar uma categoria já existente</td>
        </tr>
    </tbody>
</table>
</details>

<details>
<summary><strong>Manufacturers</strong></summary>
<br><p>Essa rota tem como objetivo a administração da entidade fabricantes</p>
<table>
    <thead>
        <tr>
            <th>Requisição</th>
            <th>Rota</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/categories</td>
            <td>Buscar todos os fabricantes</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/categories</td>
            <td>Cadastrar um novo fabricante</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td>/categories/&#123;id&#125;</td>
            <td>Editar um fabricante já existente</td>
        </tr>
         <tr>
            <td>DELETE</td>
            <td>/categories/&#123;id&#125;</td>
            <td>Deletar um fabricante já existente</td>
        </tr>
    </tbody>
</table>     
</details>

## 💻 Instalação

Para rodar esse projeto localmente, siga os seguintes passos:
1. Clone esse repositório:
```bash
git clone <repository-url>
```

2. Navegue até o diretório desse projeto:
```bash
cd <project-directory>
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```

## 📄 Documentação
![image](https://github.com/felipecomarques/PWEB1-TrabalhoFinal/assets/57302703/efa49dde-671d-4979-ac99-b1ef3ff8983c)

A documentação completa da API pode ser acessada através do Swagger. Para explorar a documentação, basta abrir a [rota /api-docs](http://127.0.0.1:5000/api/docs/) em seu navegador web. Na documentação, você pode visualizar os esquemas de solicitação e resposta e até mesmo executar operações diretamente. Isso oferece uma maneira conveniente de entender e interagir com a API sem a necessidade de ferramentas ou clientes adicionais.

## 🌙 Insomnia
![image](https://github.com/felipecomarques/PWEB1-TrabalhoFinal/assets/57302703/090af8ee-96f0-44c0-9d3e-623138abab69)

Para simplificar ainda mais a integração e teste da nossa API, incluímos um [arquivo .json](https://github.com/felipecomarques/PWEB1-TrabalhoFinal/blob/main/Insomnia.json) do aplicativo Insomnia na pasta base deste projeto. Este arquivo contém uma coleção de rotas prontas para uso, permitindo que você teste rapidamente as funcionalidades da API sem a necessidade de configurar manualmente cada solicitação.

## 👨‍💻 Desenvolvedores

Este projeto é um esforço colaborativo dos seguintes desenvolvedores:

<!--
- [Felipe Marques](https://github.com/felipecomarques)
- [Rubens Lima](https://github.com/RubensLFerreira)
- [Jhon Wesley](https://github.com/Jhon-Wesley7)
- [Anderson Menezes](https://github.com/And3rs0nMenezes)
-->

<table align="center">
  <tr align="center">
    <td>
      <a href="https://github.com/felipecomarques">
        <img src="https://avatars.githubusercontent.com/felipecomarques" width=100 />
        <p>Felipe <br/>Marques</p>
      </a>
    </td>
    <td>
      <a href="https://github.com/RubensLFerreira">
        <img src="https://avatars.githubusercontent.com/RubensLFerreira" width=100 />
        <p>Rubens <br/>Lima</p>
      </a>
    </td>
    <td>
      <a href="https://github.com/Jhon-Wesley7">
        <img src="https://avatars.githubusercontent.com/Jhon-Wesley7" width=100 />
        <p>Jhon <br/>Wesley</p>
      </a>
    </td>
    <td>
      <a href="https://github.com/And3rs0nMenezes">
        <img src="https://avatars.githubusercontent.com/And3rs0nMenezes" width=100 />
        <p>Anderson <br/>Menezes</p>
      </a>
    </td>
  </tr>
</table>
