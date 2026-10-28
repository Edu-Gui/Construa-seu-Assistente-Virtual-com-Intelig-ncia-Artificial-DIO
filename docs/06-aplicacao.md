# 4. Aplicação funcional

**Interface:** Streamlit (`src/app.py`), com mensagens em formato chat, métricas do período e opção para limpar histórico da interface.

**Núcleo:** `src/agent.py`. `load_data()` lê os arquivos da base, `summary()` calcula entradas/saídas por categoria, `local_answer()` mapeia perguntas e responde com valores extraídos e fonte, e `answer()` permite usar IA externa apenas quando explicitamente habilitada.

**Demonstração:** execute `streamlit run src/app.py`, pergunte “Quanto gastei?” e confira o resultado e a fonte. Pergunte “Quanto está o dólar agora?” para verificar a resposta de insuficiência.

**Importante:** modo local é um assistente funcional baseado em regras (sem IA generativa). Para demonstrar IA generativa, habilite API e faça testes adicionais com uma chave válida, fora do controle deste repositório.
