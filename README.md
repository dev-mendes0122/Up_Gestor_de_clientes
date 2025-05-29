# Gestor de Clientes

## 📘 Documentação do Sistema

Este repositório contém a documentação completa do projeto desenvolvido pelos alunos do Centro Universitário Unimetrocamp como parte da disciplina **Desenvolvimento rápido de aplicações em Python**, sob orientação do professor **Mauro Rodrigues**. O projeto adota a metodologia **RAD** (Rapid Application Development).

---

## 🧑‍💼 Dados do Cliente

- **Título do Projeto:** Gestão de Clientes 
- **Cliente:** Marcus Vinicius de Lira Rocha
- **Contato:** (19) 98835-6289

---

## 👩‍💻 Equipe de Desenvolvimento

| Nome                            | Curso                                 | Disciplina                                   |
|---------------------------------|---------------------------------------|----------------------------------------------|
| Pedro Adolfo Custódio Maia      | Análise e Desenvolvimento de Sistemas | Desenvolvimento Rápido de Aplicações em Python      |
| Zahira de Oliveira Silva  | Ciência da Computação            | Desenvolvimento Rápido de Aplicações em Python    |
| Sabrina Moreno Paes  | Ciência da Computação            | Desenvolvimento Rápido de Aplicações em Python    |
| Fellipe Galvão de F. Mendes      | Análise e Desenvolvimento de Sistemas | Desenvolvimento Rápido de Aplicações em Python

**Professor Orientador:** Mauro

---

🧭 Introdução
A comunicação rápida e eficiente com os clientes é um dos pilares fundamentais para empresas prestadoras de serviço, como provedores de IPTV. Atualmente, muitos desses negócios dependem de diversas plataformas para gerenciar informações dos clientes, o que torna o atendimento descentralizado, manual e propenso a erros.

Pensando nisso, este projeto propõe o desenvolvimento de um sistema unificado que centraliza os dados de sites utilizados por um cliente em uma única aplicação. Com o uso de tecnologias como Python, SQLite3, Selenium e WebDriver para coleta de dados (web scraping), além de uma interface gráfica em PyQt, será possível automatizar o fluxo de informações.

🎯 Objetivo
Problema
O cliente utiliza plataformas diferentes para acessar informações dos seus usuários, como status de pagamento, agendamentos e suporte. Além disso, todo o atendimento via WhatsApp é feito de forma manual, o que gera atrasos, aumenta o risco de erro humano e compromete a experiência do cliente.

Solução Proposta
Desenvolver um sistema desktop que:

Reúna os dados dos sites distintos por meio de web scraping automatizado.

Armazene e organize essas informações localmente com SQLite3.

Utilize uma interface amigável com PyQt para visualização e controle das operações.

🧩 Escopo
Funcionalidades Principais:
Integração com plataformas web: Coleta automatizada de dados relevantes dos clientes.

Centralização de dados em banco local: Utilização do SQLite3 para armazenar as informações extraídas.

Interface gráfica (GUI): Gerenciamento das funcionalidades por meio de uma aplicação em PyQt.

Autenticação via JSON: Controle de acesso ao sistema e dados de configuração armazenados de forma segura.

Limitações:

Atendimento complexo e técnico continuará sendo realizado manualmente.

A primeira versão não terá foco em grande escalabilidade ou múltiplos usuários simultâneos.

Não Incluso na versão 1.0:
Processamento de pagamentos diretamente pelo sistema.

Funcionalidades de e-commerce.

Integração com outros mensageiros (Telegram, SMS, e-mail etc.).

📋 Backlog do Produto (Resumo)
Módulo de Coleta de Dados

Automatizar login e extração de dados dos 7 sites usando Selenium.

Banco de Dados Local

Criar estrutura SQLite para armazenar dados dos clientes.

Interface com PyQt

Exibir, filtrar e editar informações dos clientes.

Autenticação e Configurações

Leitura e escrita de arquivos JSON com credenciais e preferências.

Testes e Validação

Garantir que os dados estão corretos.

⚙️ Tecnologias Utilizadas
Python – Lógica de aplicação

Selenium + WebDriver – Web scraping nos 7 sites

SQLite3 – Banco de dados local

PyQt – Interface gráfica

JSON – Armazenamento de configurações e dados de login


🗓️ Cronograma (Sprints)
Sprint	Tarefas Principais	Duração Estimada
1	Coleta de dados dos sites (1 a 3)	1 semana
2	Coleta de dados dos sites (4 a 7)	1 semana
3	Banco de dados SQLite + integração inicial	1 semana
4	Desenvolvimento da interface com PyQt	2 semanas
6	Testes, ajustes finais e documentação	1 semana

> _Projeto acadêmico desenvolvido com fins educativos. Todos os dados são fictícios e utilizados para simulação de um ambiente real de desenvolvimento de software._

