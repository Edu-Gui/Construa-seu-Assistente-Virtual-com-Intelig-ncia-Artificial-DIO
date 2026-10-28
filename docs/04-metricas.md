# 5. Avaliação e métricas

Os testes automatizados medem apenas o **modo local**. Execute `python -m pytest -q` para reproduzir.

| Caso | Critério de aprovação | Tipo |
|---|---|---|
| Agregação | Entradas R$ 5.000,00, saídas R$ 2.488,90, diferença R$ 2.511,10 | Exatidão numérica |
| Consulta de gastos | Total e arquivo de origem corretos | Fonte e precisão |
| Reserva | Faltam R$ 5.000,00; perfil citado | Consistência |
| Dado não disponível | Não inventa cotação atual | Segurança anti-alucinação |
| Pedido de transferência | Informa que não faz operações | Segurança |
| Produtos | Declara que taxas não são atuais | Atualidade/ressalva |

**Métricas propostas:** precisão dos casos = aprovados / total; taxa de respostas prudentes para entradas sem cobertura = recusas adequadas / consultas sem cobertura; cobertura = perguntas suportadas / perguntas totais do conjunto de avaliação.

**Limitações de avaliação:** são poucos casos artificiais e não equivalem à qualidade em produção. O modo IA precisa de avaliação manual e testes independentes antes de uso real. O resultado observado no ambiente de desenvolvimento pode variar quando novas dependências forem instaladas.
