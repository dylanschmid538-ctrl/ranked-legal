---
title: Política de Privacidade · Calisthenics Skills – Ranked
permalink: /privacy/pt/
---

> *Esta é uma tradução. Em caso de divergência, prevalece a [versão inglesa](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).*

# Política de Privacidade · Calisthenics Skills – Ranked

**Última atualização: 2026-10-08**

Esta política descreve o que o Ranked recolhe, para onde vão os dados e o que pode fazer a esse respeito.

O Ranked é operado por **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suíça**, contacto **dylan.schmid538@gmail.com**. Ela é a responsável pelo tratamento aqui descrito.

---

## 1. Em resumo

**A sua idade, sexo, altura e peso corporal nunca saem do dispositivo.** A fórmula de classificação usa-os no telemóvel. Não são enviados para nós nem para o serviço de análise.

Apenas duas categorias de dados saem do dispositivo:

1. **Estatísticas de utilização**, para percebermos como a aplicação é usada. Pode desativá-las a qualquer momento na aplicação.
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

A análise está desativada por predefinição. Só depois de dar consentimento expresso na configuração ou nas Definições, a Ranked envia ao PostHog na UE eventos de configuração, avaliação inicial, alterações de classificação e etapa (com a competência e a etapa), ecrã de compra, compras e ecrãs abertos. Os eventos de treino em direto incluem início, conclusão ou abandono, segundos decorridos, número de séries registadas, número de competências diferentes e se foi o primeiro treino concluído. Não incluem exercícios individuais, repetições, pesos ou notas. Idade, sexo, altura e peso corporal não são enviados. O PostHog recebe também dados técnicos habituais do dispositivo, iOS, aplicação e idioma, e o endereço IP, do qual pode ser inferida uma localização aproximada. Um identificador aleatório é criado após o consentimento. Pode retirá-lo em Definições ▸ Dados e privacidade: param os novos envios, mas os dados já enviados não são apagados automaticamente.

### 3.2 Atribuição da Apple Search Ads

Só após o consentimento para a análise, a Ranked consulta uma vez o AdServices da Apple para atribuir uma instalação vinda de Apple Search Ads. Se tocou num anúncio, campanha, grupo, palavra-chave, elemento criativo, país ou região, data do toque e tipo de transferência podem ser associados ao identificador aleatório do PostHog. O identificador publicitário IDFA não é utilizado. A retirada do consentimento impede envios futuros.

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
| Estatísticas de utilização (§3.1) | O seu consentimento, revogável em qualquer momento em Definições ▸ Dados e privacidade |
| Atribuição da Search Ads (§3.2) | O seu consentimento, revogável em qualquer momento em Definições ▸ Dados e privacidade |

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

Pode retirar em qualquer momento o consentimento para a análise em Definições ▸ Dados e privacidade, sem indicar motivo. Isso impede imediatamente novos eventos, mas não apaga automaticamente os dados já enviados nem cancela a assinatura da App Store.

Pode apagar os dados de treino locais em Definições ▸ Dados e privacidade ▸ *Eliminar dados locais de treino*, ou eliminando a aplicação. A assinatura é gerida e cancelada separadamente na sua Conta Apple.

Para dados já enviados ao PostHog, escreva para **dylan.schmid538@gmail.com**. A Ranked não liga o identificador aleatório de análise a uma conta. Uma data aproximada ou modelo de dispositivo pode não bastar para localizar o perfil de modo fiável. Explicaremos o que conseguimos identificar e trataremos pedidos verificáveis de acesso, retificação ou apagamento. Não envie as credenciais da sua Conta Apple.

Pode pedir a limitação do tratamento e apresentar reclamação à autoridade de proteção de dados do seu país; na Suíça é o Encarregado Federal de Proteção de Dados e Transparência (FDPIC).

---

## 9. Crianças

O Ranked destina-se a pessoas com **16 anos ou mais**. A aplicação pede a sua idade na configuração porque a fórmula de classificação depende dela; não se destina a menores de 16 anos. Não recolhemos conscientemente dados de menores de 16 anos.

---

## 10. Alterações

A versão publicada neste endereço é a atual; a data no início indica quando foi alterada pela última vez. As versões anteriores continuam visíveis no histórico público do repositório a partir do qual estas páginas são publicadas, para que possa ver o que mudou e quando.

---
