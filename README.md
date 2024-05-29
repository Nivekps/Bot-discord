## Bot Básico para Discor

**Descrição:**

Este repositório contém o código para um bot básico do Discord que oferece diversas funcionalidades, incluindo:

* **Saudação personalizada:** Responde à mensagem "%oi" com uma saudação personalizada para o usuário.
* **Mensagens inspiradoras:** Envia mensagens inspiradoras para o usuário quando solicitado.
* **Moderação de linguagem:** Detecta e avisa sobre mensagens ofensivas no canal, promovendo um ambiente positivo.
* **Consulta de dados da Covid-19:** Acessa a Covid19 API para fornecer informações sobre casos e mortes por estado ou país.

**Funcionalidades:**

* **Comando "%oi":**
    * O bot identifica o nome do usuário que enviou a mensagem.
    * Responde com uma saudação personalizada, como "Oi, [nome do usuário]! Como você está hoje?".
* **Comando para mensagens inspiradoras:**
    * O usuário pode solicitar mensagens inspiradoras digitando um comando específico (a definir).
    * O bot busca e envia uma mensagem inspiradora de uma fonte confiável.
* **Moderação de linguagem:**
    * O bot utiliza um algoritmo de detecção de linguagem ofensiva para identificar mensagens inadequadas.
    * Ao detectar uma mensagem ofensiva, o bot envia uma mensagem de aviso para o usuário, lembrando-o das regras do canal.
* **Consulta de dados da Covid-19:**
    * Os usuários podem consultar dados da Covid-19 por estado ou país usando comandos específicos (por exemplo, "!covid_estado SP" ou "!covid_pais Brasil").
    * O bot acessa a Covid19 API e retorna informações atualizadas sobre casos e mortes.

**Pré-requisitos:**

* Conta do Discord
* Servidor Discord configurado
* Conhecimento básico de Python e programação de bots
* Chave de API da Covid19 (opcional, para consulta de dados)


1. Configure o bot com seu token do Discord:

* Crie um arquivo `config.py` e insira seu token do Discord:

```python
token = "SEU_TOKEN_DISCORD"
```

4. Execute o bot:

```bash
python bot.py
```

**Uso:**

* **Comando "%oi":**
    * Envie a mensagem "%oi" no canal do Discord onde o bot está configurado.
    * O bot responderá com uma saudação personalizada para você.
* **Comando para mensagens inspiradoras:**
    * Utilize o comando específico definido para solicitar uma mensagem inspiradora (por exemplo, "!inspiracao" ou "!motivar").
    * O bot buscará e enviará uma mensagem inspiradora para você.
* **Moderação de linguagem:**
    * Envie mensagens no canal do Discord.
    * O bot monitorará as mensagens e avisará caso detecte conteúdo ofensivo.
* **Consulta de dados da Covid-19:**
    * Utilize os comandos específicos para consultar dados por estado ou país (por exemplo, "!covid_estado SP" ou "!covid_pais Brasil").
    * O bot exibirá informações atualizadas sobre casos e mortes da Covid-19.

**Contribuição:**

Sinta-se à vontade para contribuir com este projeto! Você pode sugerir melhorias, corrigir bugs ou adicionar novas funcionalidades.

**Licença:**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.


**Observações:**

* Este README.md fornece uma visão geral das funcionalidades do bot. Para mais detalhes sobre a implementação, consulte o código Python.
* Este projeto é um ponto de partida e pode ser facilmente adaptado para atender às suas necessidades específicas.
* Utilize boas práticas de desenvolvimento de software e siga as diretrizes do Discord para garantir a confiabilidade e a segurança do bot.
* A implementação da moderação de linguagem e da consulta de dados da Covid-19 pode variar de acordo com as suas necessidades e ferramentas disponíveis.
