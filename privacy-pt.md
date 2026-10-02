---
title: Política de Privacidade · Calisthenics Skills – Ranked
permalink: /privacy/pt/
---

> *Esta é uma tradução. Em caso de divergência, prevalece a [versão inglesa](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).*

# Política de Privacidade · Calisthenics Skills – Ranked

**Última atualização: 2026-10-02**

Esta política descreve o que o Ranked recolhe, para onde vão os dados e o que pode fazer a esse respeito. Foi redigida com base no código real da aplicação, não num modelo; se houver aqui algum erro, é o código que deve ser verificado.

O Ranked é operado por **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suíça**, contacto **dylan.schmid538@gmail.com**. Ela é a responsável pelo tratamento aqui descrito.

---

## 1. Em resumo

**A sua idade, sexo, altura e peso corporal nunca saem do dispositivo.** A fórmula de classificação usa-os no telemóvel. Não são enviados para nós nem para o serviço de análise.

Apenas duas categorias de dados saem do dispositivo:

1. **Estatísticas de utilização anónimas**, para percebermos como a aplicação é usada. Pode desativá-las a qualquer momento na aplicação.
2. **Dados de compra**, para verificar a assinatura da App Store. A Apple processa o pagamento; nunca vemos os seus dados de pagamento.

O Ranked não o segue entre outras aplicações ou sites, não apresenta publicidade e não lê dados da Apple Health.

---

## 2. O que fica no dispositivo

Os seguintes dados são guardados na base de dados da aplicação no seu telemóvel e nunca são transmitidos:

- Cada treino, série, repetição, tempo de sustentação e peso adicional que regista
- O seu plano de treino, calendário, lembretes e preferências
- As medidas corporais que introduziu (idade, sexo, altura e peso corporal)
- As suas notas de treino

A aplicação não exclui esta base de dados da cópia de segurança do dispositivo. Se usar uma cópia de segurança do iCloud ou do computador, os dados de treino farão parte dela e serão repostos quando restaurar a cópia — segundo as condições da Apple, não as nossas.

Eliminar a aplicação apaga estes dados do dispositivo. Não os podemos recuperar porque nunca os tivemos.

---

## 3. O que sai do dispositivo

### 3.1 Estatísticas de utilização (PostHog)

Usamos o **PostHog**, alojado na **União Europeia**, para compreender como a aplicação é usada. A aplicação envia uma lista fixa de eventos:

- a etapa de configuração a que chegou, que concluiu ou da qual voltou atrás, e a duração de cada etapa;
- o resultado da avaliação inicial: quantas linhas de habilidades e etapas indicou, a habilidade escolhida como objetivo, o seu nível inicial e o nível de cada uma das seis regiões corporais;
- quando o ecrã de compra foi apresentado ou fechado e quando uma compra foi iniciada, concluída ou restaurada, com o produto e a oferta respetivos; quando a aplicação observa mais tarde um período de teste ativo ou uma assinatura paga, com o produto e a indicação de compra em ambiente de testes (isto não é um registo de cada cobrança e não é enviado enquanto a aplicação está fechada);
- quando o seu nível mudou e a habilidade que causou a mudança;
- quando concluiu uma etapa: a habilidade e a etapa, e se resultou de uma série registada, de um treino inserido posteriormente ou de uma indicação manual;
- os ecrãs que abre e quando termina um treino. O evento de fim de treino não contém pormenores: nem exercícios, nem séries, nem números.

O software do PostHog na aplicação também anexa a cada evento informações técnicas habituais, como o modelo do dispositivo, a versão do iOS, a versão da aplicação, o idioma e o fuso horário, e regista quando a aplicação é aberta ou passa para segundo plano. Como qualquer serviço de Internet, o PostHog recebe o endereço IP do pedido e pode inferir dele uma localização aproximada (país ou cidade).

**O que não está incluído:** nome, endereço de e-mail (a aplicação nunca o pede), identificador de conta (não existe), idade, sexo, altura, peso corporal ou conteúdo dos treinos.

**Como é identificado:** o PostHog gera um identificador aleatório na primeira execução da aplicação e guarda-o no dispositivo. Todos os eventos são agrupados sob esse identificador. A aplicação nunca informa o PostHog de quem é, nem existe uma conta ou e-mail que pudesse comunicar.

**Como desativar:** Definições ▸ Privacidade ▸ *Partilhar dados de utilização anónimos*. Desativar esta opção impede a aplicação de enviar eventos a partir desse momento. A definição fica guardada no dispositivo e mantém-se após atualizações.

### 3.2 Atribuição da Apple Search Ads

Se instalou o Ranked depois de tocar num anúncio da Apple Search Ads, a aplicação pergunta uma vez à Apple, na primeira abertura, de onde veio a instalação. A Apple responde com a campanha, o grupo de anúncios, a palavra-chave e o conjunto criativo do anúncio, o país ou região e a data do clique, e se foi uma primeira instalação ou uma nova transferência. A aplicação associa estes valores ao identificador anónimo do PostHog descrito em §3.1, permitindo agrupar os eventos posteriores pelo anúncio que o trouxe.

Isto usa a estrutura **AdServices** da Apple, que não utiliza o identificador de publicidade (IDFA) e que a Apple não considera rastreamento; por isso, não é apresentado um pedido de autorização de rastreamento. Se não chegou através de um anúncio, a Apple indica-o e nada mais é associado. Desativar as estatísticas de utilização (§3.1) também interrompe isto.

### 3.3 Compras (Apple e RevenueCat)

As assinaturas são vendidas e cobradas pela **Apple** através da App Store. Nunca vemos os seus dados de pagamento, a sua Conta Apple ou o seu nome.

Para verificar se a assinatura está ativa, a aplicação usa a **RevenueCat**. A RevenueCat recebe o registo de compra da App Store relativo à assinatura — o produto comprado, quando começou e quando expira — juntamente com informações técnicas habituais, como a versão do iOS e da aplicação. Identifica a instalação por um identificador aleatório que ela própria gera e guarda no dispositivo. Não fornecemos à RevenueCat o seu nome, e-mail ou qualquer outra identidade; como o Ranked não tem contas, não existe uma para fornecer.

Quando toca em **Restaurar compras**, a aplicação pede à Apple as compras efetuadas com a Conta Apple iniciada no dispositivo e transmite o resultado à RevenueCat da mesma forma.

---

## 4. O que o Ranked não faz

- **Sem contas.** Nunca inicia sessão. Não existe um perfil seu em nenhum servidor.
- **Sem Apple Health.** O Ranked não lê nem escreve dados na aplicação Saúde.
- **Sem câmara, fotografias, microfone, localização ou contactos.** A aplicação não pede nenhuma destas permissões.
- **Sem rastreamento entre aplicações ou sites**, identificador de publicidade, anúncios na aplicação ou venda/entrega de dados a corretores de dados.
- **Sem servidor de notificações push.** Os lembretes são agendados localmente no telemóvel; nada sobre eles sai do dispositivo. É solicitada autorização antes de agendar o primeiro e pode desativá-los a qualquer momento nas Definições do iOS.

---

## 5. Fundamento jurídico (RGPD e LPD suíça revista)

| Tratamento | Fundamento |
|---|---|
| Compras e verificação da assinatura (§3.3) | Execução de um contrato |
| Estatísticas de utilização (§3.1) | Interesse legítimo em compreender e melhorar a aplicação; pode opor-se a qualquer momento desativando-as, ver §8 |
| Atribuição da Search Ads (§3.2) | Interesse legítimo em saber que publicidade funciona; oposição conforme acima |

**Aplicam-se duas leis, não apenas uma.** O Ranked é operado a partir da Suíça, pelo que este tratamento está sujeito à Lei Federal Suíça de Proteção de Dados revista (**LPD revista**, em vigor desde setembro de 2023). O **RGPD** aplica-se adicionalmente quando a aplicação é usada na União Europeia ou no Reino Unido. Se diferirem, seguimos a regra mais rigorosa. Os residentes suíços têm os mesmos direitos essenciais enumerados em §8, nos termos do artigo 25.º e seguintes da LPD revista.

---

## 6. Onde os dados são tratados

- O **PostHog** trata as estatísticas de utilização na União Europeia.
- A **RevenueCat, Inc.** está sediada nos Estados Unidos e trata aí os dados de compra descritos em §3.3.
- A **Apple** trata a compra e o pedido de atribuição da Search Ads segundo a sua própria política de privacidade, aplicável à sua Conta Apple independentemente desta aplicação.

---

## 7. Durante quanto tempo são conservados

As estatísticas de utilização são conservadas enquanto se aplicar o período de retenção do nosso plano PostHog. Não prometemos um número fixo de meses porque o PostHog não nos permite defini-lo; um prazo que não podemos cumprir seria pior nesta política do que não indicar nenhum.

Os registos de compra são conservados pela RevenueCat enquanto existirem a assinatura e o seu histórico, necessários para verificar a assinatura.

Os dados no dispositivo permanecem até eliminar a aplicação.

---

## 8. Os seus direitos

Pode, a qualquer momento:

- **Desativar as estatísticas de utilização** em Definições ▸ Privacidade. É o seu direito de oposição e, quando o tratamento se baseia no consentimento, de o retirar. Produz efeitos imediatamente e não exige justificação.
- **Eliminar os seus dados.** Como o Ranked não guarda nada sobre si num servidor, eliminar a aplicação remove tudo o que a própria aplicação armazena.
- **Pedir a eliminação do seu perfil analítico anónimo.** Não o podemos localizar pelo nome, pois não tem nenhum, mas se nos escrever indicando a data aproximada da primeira utilização e o dispositivo usado, procurá-lo-emos manualmente e eliminá-lo-emos.
- **Pedir uma cópia** dos dados que um serviço guarda sob o seu identificador, pedir-nos que os **corrijamos** ou que **limitemos** o tratamento enquanto analisamos o pedido.
- **Apresentar reclamação a uma autoridade de controlo** no seu país; na Suíça, ao Encarregado Federal da Proteção de Dados e da Transparência (FDPIC).

Escreva para **dylan.schmid538@gmail.com** para exercer qualquer um destes direitos.

---

## 9. Crianças

O Ranked destina-se a pessoas com **16 anos ou mais**. A aplicação pede a sua idade na configuração porque a fórmula de classificação depende dela; não se destina a menores de 16 anos. Não recolhemos conscientemente dados de menores de 16 anos.

---

## 10. Alterações

A versão publicada neste endereço é a atual; a data no início indica quando foi alterada pela última vez. As versões anteriores continuam visíveis no histórico público do repositório a partir do qual estas páginas são publicadas, para que possa ver o que mudou e quando.

---

> **⚠️ Não constitui aconselhamento jurídico.** Este documento foi redigido a partir do código-fonte da aplicação por um engenheiro, não por um advogado. Descreve o sistema com precisão na data acima; cada afirmação foi verificada face ao que a aplicação realmente envia. **Não** foi revisto quanto à conformidade com o RGPD, a LPD suíça revista, a CCPA ou qualquer outro regime. A publicação satisfaz a Apple; não garante a conformidade legal. Peça a um advogado que o reveja quando a aplicação começar a gerar receitas.
