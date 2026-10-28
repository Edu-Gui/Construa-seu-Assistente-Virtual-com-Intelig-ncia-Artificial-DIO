# 💬 BIA Planeja — Assistente Virtual de Organização Financeira

Projeto educacional do laboratório **Construa Seu Assistente Virtual Com Inteligência Artificial (DIO)**, adaptado do repositório-base. O protótipo utiliza apenas informações **fictícias** e tem foco em explicar gastos, organizar metas e evitar respostas inventadas.

## Demonstração e finalidade

O assistente atende pessoas que desejam entender um histórico de receitas e despesas, consultar o progresso da reserva de emergência e conhecer categorias de produtos presentes na base didática. Não acessa bancos, não realiza operações e não substitui aconselhamento financeiro profissional.

**O que ele faz:** calcula valores diretamente dos CSVs, responde com a origem da informação, admite lacunas e pode usar uma API de modelo de linguagem **opcionalmente** para formular respostas. Sem chave de API, funciona em modo local (respostas por regras, não IA generativa).

## Executar no computador

Requer **Python 3.10 ou superior**. Na raiz do projeto:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

Abra o endereço local exibido pelo Streamlit, normalmente `http://localhost:8501`.

### Habilitar respostas com IA (opcional)

Na barra lateral, marque **Usar IA via API** e informe sua chave, ou configure a variável de ambiente `OPENAI_API_KEY`. Por exemplo, no PowerShell:

```powershell
$env:OPENAI_API_KEY="sua-chave"
streamlit run src/app.py
```

Requer acesso habilitado ao modelo configurado e pode gerar custos de API. **Não coloque chaves reais em arquivos versionados no GitHub.** Ao habilitar, perguntas e contexto de exemplo podem ser transmitidos ao provedor. O modo IA não foi validado automaticamente neste pacote e pode exigir ajustes conforme a versão/API disponível.

## Experimente estas perguntas

- Quanto gastei no período?
- Qual foi a diferença entre entradas e saídas?
- Quanto falta para minha reserva de emergência?
- Que produtos aparecem na base?
- Quanto está o dólar agora? (teste de informação ausente)

## Organização dos arquivos

```text
README.md
requirements.txt
data/         # 4 arquivos fictícios originais do repositório
src/          # app.py (interface) e agent.py (dados e respostas)
docs/         # etapas 1, 2, 3, 5 e 6 + documentação da aplicação
tests/        # testes automatizados do modo local
assets/       # materiais de apoio do desafio original
```

## Os 6 passos

1. **Documentação:** [docs/01-documentacao-agente.md](docs/01-documentacao-agente.md)
2. **Base de conhecimento:** [docs/02-base-conhecimento.md](docs/02-base-conhecimento.md)
3. **Prompts:** [docs/03-prompts.md](docs/03-prompts.md)
4. **Aplicação funcional:** [docs/06-aplicacao.md](docs/06-aplicacao.md)
5. **Avaliação e métricas:** [docs/04-metricas.md](docs/04-metricas.md)
6. **Pitch:** [docs/05-pitch.md](docs/05-pitch.md)

## Testes

```bash
python -m pytest -q
```

Os testes verificam cálculos, origem, reserva, recusa de ação e tratamento de informações ausentes. O resultado obtido durante a criação está documentado em `docs/04-metricas.md`; resultados de IA externa não foram medidos.

## Limitações

- Dados simulados de **outubro de 2025**, não sincronizados com contas reais.
- Meta com prazo **junho de 2026** já passado, não recalculado automaticamente.
- Produtos e remunerações listados são **exemplos históricos**, não preços ou taxas atuais.
- O modo local usa regras simples e não compreende todas as formas de pergunta.
- O modo de IA depende de credenciais, conectividade e validação humana; suas respostas podem conter erros.

## Ética e segurança

Sem coleta de CPF, senhas ou dados bancários. Recusa transferências e não dá garantia de rendimento. O conteúdo da base de exemplo não deve ser substituído por dados reais sem cuidado com privacidade, consentimento e proteção de credenciais.
# Construa-seu-Assistente-Virtual-com-Intelig-ncia-Artificial-DIO
