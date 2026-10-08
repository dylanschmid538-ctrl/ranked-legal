---
title: Política de privacidad · Calisthenics Skills – Ranked
permalink: /privacy/es/
---

> Esta es una traducción. En caso de discrepancia, prevalece la [versión en inglés](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Política de privacidad · Calisthenics Skills – Ranked

**Última actualización: 2026-10-08**

Esta política explica qué datos recopila Ranked, adónde van y qué puede hacer usted al respecto.

Ranked está operada por **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suiza**, contacto **dylan.schmid538@gmail.com**. Ella es la responsable del tratamiento descrito aquí.

---

## 1. En pocas palabras

**Su edad, sexo, altura y peso corporal nunca salen de su dispositivo.** La fórmula del rango los utiliza en el teléfono. No se nos envían a nosotros ni al servicio de análisis.

Solo salen de su dispositivo estas dos categorías:

1. **Estadísticas de uso**, para saber cómo se utiliza la aplicación. Puede desactivarlas en la aplicación en cualquier momento.
2. **Datos de compra**, para verificar la suscripción de App Store. Apple gestiona el pago; nosotros nunca vemos sus datos de pago.

Ranked no le rastrea entre otras aplicaciones o sitios web, no muestra publicidad y no lee nada de Apple Health.

---

## 2. Qué permanece en su dispositivo

Lo siguiente se guarda en la base de datos de la aplicación en su teléfono y nunca se transmite:

- Cada entrenamiento, serie, repetición, mantenimiento y peso añadido que registre
- Su plan y horario de entrenamiento, recordatorios y preferencias
- Las medidas corporales que haya introducido (edad, sexo, altura y peso corporal)
- Sus notas de entrenamiento

La aplicación no excluye esta base de datos de la copia de seguridad de su dispositivo. Si usa iCloud Backup o una copia de seguridad en un ordenador, sus datos de entrenamiento forman parte de ella y vuelven al restaurarla, según las condiciones de Apple, no las nuestras.

Al borrar la aplicación, se elimina todo esto del dispositivo. No podemos recuperarlo porque nunca lo tuvimos.

---

## 3. Qué sale de su dispositivo

### 3.1 Estadísticas de uso (PostHog)

El análisis está desactivado de forma predeterminada. Solo si da su consentimiento expreso durante la configuración o después en Ajustes, Ranked envía a PostHog en la UE eventos sobre la configuración, la evaluación inicial, cambios de rango y etapa (con la habilidad y etapa), la pantalla de compra, las compras y las pantallas abiertas. Los eventos de entrenamiento en directo indican el inicio, fin o abandono, los segundos transcurridos, el número de series registradas, el número de habilidades distintas y si es el primer entrenamiento completado. No incluyen ejercicios individuales, repeticiones, pesos ni notas. No se transmiten edad, sexo, altura ni peso corporal. PostHog recibe además datos técnicos habituales del dispositivo, iOS, la aplicación y el idioma, y la dirección IP, de la que puede deducirse una ubicación aproximada. Se crea un identificador aleatorio después del consentimiento. Puede retirarlo en Ajustes ▸ Datos y privacidad: cesan los nuevos envíos, pero los datos ya enviados no se borran automáticamente.

### 3.2 Atribución de Apple Search Ads

Solo después de su consentimiento para el análisis, Ranked consulta una vez mediante AdServices de Apple la atribución de una instalación procedente de Apple Search Ads. Si tocó un anuncio, la campaña, el grupo de anuncios, la palabra clave, el elemento creativo, el país o región, la fecha del clic y el tipo de descarga pueden asociarse al identificador aleatorio de PostHog. No se usa el identificador publicitario IDFA. La retirada del consentimiento detiene futuros envíos.

### 3.3 Compras (Apple y RevenueCat)

**Apple** vende y factura las suscripciones a través de App Store. Nunca vemos sus datos de pago, su Cuenta de Apple ni su nombre.

Para comprobar si su suscripción está activa, la aplicación utiliza **RevenueCat**. RevenueCat recibe el registro de compra de App Store —el producto comprado, cuándo comenzó y cuándo vence— junto con información técnica habitual, como la versión de iOS y de la aplicación. Identifica su instalación mediante un identificador aleatorio que genera y guarda en su dispositivo. No proporcionamos a RevenueCat su nombre, correo electrónico ni ninguna otra identidad; como Ranked no tiene cuentas, no existe tal identidad que proporcionarle.

Cuando toca **Restaurar compras**, la aplicación pide a Apple las compras realizadas con la Cuenta de Apple iniciada en el dispositivo y pasa el resultado a RevenueCat de la misma manera.

---

## 4. Qué no hace Ranked

- **Sin cuentas.** Nunca inicia sesión. No hay ningún perfil suyo en un servidor.
- **Sin Apple Health.** Ranked no lee ni escribe datos en la aplicación Salud.
- **Sin cámara, fotos, micrófono, ubicación ni contactos.** La aplicación no solicita esos permisos.
- **Sin seguimiento entre aplicaciones o sitios web**, identificador publicitario, anuncios en la aplicación ni venta o entrega de datos a intermediarios de datos.
- **Sin servidor de notificaciones push.** Los recordatorios que puede enviar Ranked se programan localmente en su teléfono; nada de ellos sale del dispositivo. Se le pide permiso antes del primero y puede desactivarlos en los ajustes de iOS en cualquier momento.

---

## 5. Base jurídica (RGPD y revDSG suiza)

| Tratamiento | Base |
|---|---|
| Compras y verificación de suscripciones (§3.3) | Ejecución de un contrato |
| Estadísticas de uso (§3.1) | Su consentimiento; puede retirarlo en cualquier momento en Ajustes ▸ Datos y privacidad |
| Atribución de Search Ads (§3.2) | Su consentimiento; puede retirarlo en cualquier momento en Ajustes ▸ Datos y privacidad |

**Aquí se aplican dos leyes, no una.** Ranked se opera desde Suiza, por lo que este tratamiento se rige por la Ley Federal de Protección de Datos suiza revisada (**revDSG**, vigente desde septiembre de 2023). El **RGPD** se aplica además cuando la aplicación se utiliza desde la Unión Europea o el Reino Unido. Si difieren, seguimos la norma más estricta. Los residentes en Suiza tienen los mismos derechos fundamentales enumerados en §8 conforme al artículo 25 y siguientes de la revDSG.

---

## 6. Dónde se tratan los datos

- **PostHog** trata las estadísticas de uso en la Unión Europea.
- **RevenueCat, Inc.** tiene su sede en Estados Unidos y trata allí los datos de compra descritos en §3.3.
- **Apple** trata la propia compra y la solicitud de atribución de Search Ads conforme a su propia política de privacidad, que se aplica a su Cuenta de Apple independientemente de esta aplicación.

---

## 7. Durante cuánto tiempo los conservamos

Las estadísticas de uso se conservan durante el período de retención de PostHog correspondiente a nuestro plan. No prometemos un número fijo de meses porque PostHog no nos permite establecerlo; una cifra que nadie puede cumplir es peor en una política de privacidad que no dar ninguna.

RevenueCat conserva los registros de compra mientras existan la suscripción y su historial, como requiere la verificación de una suscripción.

Todo lo que está en su dispositivo permanece allí hasta que borre la aplicación.

---

## 8. Sus derechos

Puede retirar en cualquier momento su consentimiento para el análisis en Ajustes ▸ Datos y privacidad, sin dar explicaciones. Esto detiene inmediatamente los nuevos eventos, pero no borra automáticamente los datos ya enviados ni cancela su suscripción de App Store.

Puede borrar los datos de entrenamiento locales en Ajustes ▸ Datos y privacidad ▸ *Eliminar datos locales de entrenamiento*, o eliminando la aplicación. La suscripción se gestiona y cancela por separado en su Cuenta de Apple.

Para los datos ya enviados a PostHog, escriba a **dylan.schmid538@gmail.com**. Ranked no vincula el identificador analítico aleatorio con una cuenta. Una fecha aproximada o un modelo de dispositivo puede no bastar para localizar su perfil de forma fiable. Explicaremos qué podemos identificar y atenderemos solicitudes verificables de acceso, rectificación o eliminación. No envíe las credenciales de su Cuenta de Apple.

Puede pedir la limitación del tratamiento y presentar una reclamación ante la autoridad de protección de datos de su país; en Suiza es el Comisionado Federal de Protección de Datos y Transparencia (FDPIC).

---

## 9. Menores

Ranked está destinada a personas de **16 años o más**. La aplicación pregunta su edad durante la configuración porque la fórmula del rango depende de ella y no está dirigida a menores de esa edad. No recopilamos deliberadamente datos de menores de 16 años.

---

## 10. Cambios

La versión publicada en esta dirección es la vigente, y la fecha del principio indica cuándo se modificó por última vez. Las versiones anteriores permanecen visibles en el historial público del repositorio desde el que se publican estas páginas, para que pueda ver qué cambió y cuándo.

---
