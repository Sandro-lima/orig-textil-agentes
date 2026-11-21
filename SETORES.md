# Operação por setor

A sessão principal coordena a equipe e reúne as recomendações por SKU, loja e período.

| Setor | Novos agentes | Áreas existentes |
|---|---|---|
| Diretoria e planejamento | planejamento-financeiro | campanhas-crescimento, auditoria |
| Comercial | ranking-e-preco | especialistas por canal, concorrência, precificação, mídia, afiliados, CRM |
| Financeiro | financeiro-geral, conciliacao-bancaria, fiscal-contabil | financeiro-repasses |
| Operações | compras-suprimentos | estoque-produção, produto-qualidade, pedidos-logística |
| Pessoas | rh-departamento-pessoal | responsáveis humanos pela folha e gestão de pessoas |
| Dados e tecnologia | — | dados, integracoes-operacao |

## Como a decisão de preço circula

1. O diretor solicita ao canal e a concorrencia posição observada, contexto, preço final e conversão.
2. Solicita a precificacao o preço mínimo e a contribuição unitária e total esperada por cenário, na faixa de taxa correta.
3. Entrega as duas análises a ranking-e-preco para recomendar manter, testar ou ajustar outro fator.
4. planejamento-financeiro incorpora a decisão a volume, capacidade, capital de giro e caixa projetado.
5. auditoria confere fontes, datas e premissas. O gestor aprova testes comerciais.

## Painel e fontes

O painel.html é um protótipo local em modo demonstração. Para trocar os números, importe um JSON conforme o exemplo dados-painel-demo.json. Para produção, um serviço autenticado deve coletar fontes autorizadas, normalizar chaves e publicar os indicadores agregados. A interface atualiza a idade dos dados a cada segundo. A frequência de novos dados depende de cada fonte e precisa ser exibida. Dados de banco e RH exigem acesso por função.

Bling: validar importação OFX e disponibilidade de leitura das baixas na integração. Para extratos automáticos, validar banco PJ e instituição receptora de Open Finance com consentimento, escopo de consulta e identificadores de transação. Nunca grave extratos, folhas, tokens ou qualquer dado pessoal no repositório.
