# 6. Pitch — roteiro de apresentação (aprox. 3 minutos)

**Problema:** Muitas pessoas têm dificuldade para entender em quais categorias gastam mais e quanto falta para alcançar metas. Mesmo com dados disponíveis, extrair respostas rápidas exige organização.

**Solução:** Criei a BIA Planeja, um assistente virtual que lê dados fictícios de transações e metas e apresenta respostas claras em um chat. A interface foi construída em Streamlit e funciona sem custo de API no modo local.

**Demonstração:** Pergunto “Quanto gastei?”: o agente reúne saídas de outubro de 2025, mostra R$ 2.488,90 e detalha as categorias. Pergunto “Quanto falta para a reserva?”: ele informa R$ 5.000,00, cita a fonte e alerta que o prazo cadastrado está vencido.

**Segurança:** Em vez de inventar a cotação do dólar ou realizar transferências, informa os limites. Uma integração opcional com IA generativa pode reformular respostas fundamentadas nos dados locais, mediante chave e revisão.

**Valor:** O usuário compreende dados, acompanha metas e pode decidir qual informação complementar precisa buscar. O protótipo demonstra integração de dados, desenvolvimento Python, design de prompts e avaliação — uma base para versões futuras com validação mais robusta.

**Próximos passos:** ampliar o conjunto de perguntas e métricas, adicionar testes adversariais e desenhar controles adequados para dados pessoais antes de qualquer uso real.
