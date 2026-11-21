# Agentes de marketplace da Orig Têxtil

Extraia o ZIP e abra a pasta extraída no Claude Code. A pasta oculta .claude contém 37 especialistas. A sessão principal funciona como diretor. Os agentes têm acesso somente à leitura de arquivos locais. Os limites em config-operacao.yaml são campos de configuração para o projeto e, na operação real, precisam ser validados pelo serviço intermediário.

## Primeiro comando no Claude Code

> Conduza o diagnóstico inicial da Orig Têxtil. Leia CLAUDE.md, config-operacao.yaml e RELATORIO.md. Use dados/ para os arquivos de entrada. Delegue aos agentes de cada canal com dados disponíveis, aos especialistas pertinentes e à auditoria. Compare últimos 7 dias com os 7 anteriores e use 30 dias para contexto. Relate bloqueios e devolva um único relatório. Priorize Shopee e TikTok Shop. Não faça alterações nas contas.

## Arquivos de entrada

Coloque em dados/ exportações por loja e canal e identifique o período no nome. Comece pelos últimos 30 dias, sem nome, endereço ou contato de clientes. Preserve identificadores de pedido e SKU necessários à reconciliação.

| Fonte | Campos esperados |
|---|---|
| Pedidos e repasses | canal, conta, pedido, data, status, SKU, quantidade, preço, desconto, tarifa, frete, repasse, estorno |
| Custos e estoques | SKU, cor, tamanho, custo de fabricação, embalagem, tributação validada, disponível, reservado, em produção, composição dos kits |
| Catálogo e tráfego | anúncio, SKU, título, status, impressões, cliques e conversão quando disponíveis |
| Ads e afiliados | campanha, criativo, criador, SKU, gasto, comissão, vendas e receita atribuídas, janela de atribuição |
| Expedição | pedido, prazo, despacho, situação e cancelamento |

## Ativação

1. Compare uma primeira rodada de leitura com os painéis. Teste a reconciliação de um pedido normal, um kit, um estorno e uma venda com mídia.
2. Confirme se Bling, Upseller ou AvantPro já entregam os dados necessários. Consulte os escopos reais das APIs oficiais para preencher lacunas. Eleja uma fonte de estoque e um serviço autorizado a gravar em cada combinação de loja e ação. Use integração separada para mídia quando necessário.
3. Conecte operações comprovadas por MCP ou serviço equivalente e agende a coleta e geração em ambiente com acesso às fontes. Teste permissões, erros, dados desatualizados e alertas. Sugestão de relatório diário às 8h, horário de São Paulo, e resumo semanal às segundas.
4. Libere primeiro rotinas reversíveis e verificadas, por exemplo sincronização de estoque por regra do ERP ou pausa de mídia sob um teto configurado. Use limites aprovados, lista de contas autorizadas, log e possibilidade de interrupção. Mudanças de piso, aumento do teto de gasto, alteração de conta e disputas fora da política são decisões do responsável.
5. Compare cada rodada com o painel e amplie a automação por tipo de ação e conta. Para operação contínua, mantenha coleta e alertas de falha independentes da sessão de chat.

Integrações de produção, agendamento, acesso às lojas e envio de relatórios precisam ser implantados. Este pacote contém os agentes e o fluxo de diagnóstico.

## Custos da Orig

O cadastro importado e o mapa de SKUs estão em dados/. A rotina de importação está descrita no CLAUDE.md. Esta versão inclui 37 especialistas.

A operacao de afiliados usa AFILIADOS.md e dados/afiliados_pipeline.csv.

Os agentes de pós-venda e relacionamento usam POS-VENDA.md e as filas em dados/.

Use RESPONSABILIDADES.md para identificar quem lidera cada etapa da operação.

Veja SETORES.md para o organograma, o fluxo de ranking e preco e as instrucoes do painel.
