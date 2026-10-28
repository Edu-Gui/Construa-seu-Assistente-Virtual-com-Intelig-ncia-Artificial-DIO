# 2. Base de conhecimento

Dados sintéticos preservados do repositório-base:

| Arquivo | Campos/uso | Tratamento |
|---|---|---|
| `data/transacoes.csv` | data, descrição, categoria, valor, tipo | CSV com entradas/saídas agregadas por Python; números convertidos para float |
| `data/perfil_investidor.json` | perfil, objetivo, reserva e metas | Consulta ao objetivo de reserva; diferença entre meta e valor cadastrado |
| `data/produtos_financeiros.json` | nomes, riscos e aportes ilustrativos | Exibição descritiva; sem considerar taxas atuais |
| `data/historico_atendimento.csv` | canais, temas e resoluções | Contagem de registros/resoluções |

Os dados são carregados a partir de caminhos relativos ao diretório do projeto (`pathlib`). Não há busca na internet nem dados em tempo real.

**Regras de confiabilidade:** citar o arquivo pertinente, identificar o período das transações e não tratar projeções ou exemplos de rentabilidade como informação atual. Caso a base não contenha a resposta, declarar insuficiência.
