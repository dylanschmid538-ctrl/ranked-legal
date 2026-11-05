---
title: Política de privacidad · Calisthenics Skills – Ranked
permalink: /privacy/es/
---

> Esta es una traducción. En caso de discrepancia, prevalece la [versión en inglés](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Política de privacidad · Calisthenics Skills – Ranked

**Última actualización: 2026-11-05**

Esta política explica qué datos recopila Ranked, adónde van y qué puede hacer usted al respecto.

Ranked está operada por **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suiza**, contacto **dylan.schmid538@gmail.com**. Ella es la responsable del tratamiento descrito aquí.

---

## 1. En pocas palabras

**Su edad, sexo, altura y peso corporal nunca salen de su dispositivo.** La fórmula del rango los utiliza en el teléfono. No se nos envían a nosotros ni al servicio de análisis.

Cuatro tipos de datos pueden salir de su dispositivo:

1. **Estadísticas de uso**, para saber cómo se utiliza la aplicación. Puede desactivarlas en la aplicación en cualquier momento.
2. **Datos de compra**, para verificar la suscripción de App Store. Apple gestiona el pago; nosotros nunca vemos sus datos de pago.
3. **Mensajes de opinión o asistencia**, solo si decide enviarlos. Puede consentir por separado en facilitar un correo electrónico o teléfono para recibir respuesta.
4. **YouTube (§3.4)**

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

El nombre, la foto de perfil y la foto inicial se guardan en este dispositivo.

---

## 3. Qué sale de su dispositivo

### 3.1 Estadísticas de uso (PostHog)

El análisis está desactivado de forma predeterminada. Solo si da su consentimiento expreso durante la configuración o después en Ajustes, Ranked envía a PostHog en la UE eventos sobre la configuración, la evaluación inicial, cambios de rango y etapa (con la habilidad y etapa), la pantalla de compra, las compras y las pantallas abiertas. Los eventos de entrenamiento en directo indican el inicio, fin o abandono, los segundos transcurridos, el número de series registradas, el número de habilidades distintas y si es el primer entrenamiento completado. No incluyen ejercicios individuales, repeticiones, pesos ni notas. No se transmiten edad, sexo, altura ni peso corporal. PostHog recibe además datos técnicos habituales del dispositivo, iOS, la aplicación y el idioma, y la dirección IP, de la que puede deducirse una ubicación aproximada. Se crea un identificador aleatorio después del consentimiento. Puede retirarlo en Ajustes ▸ Datos y privacidad: cesan los nuevos envíos, pero los datos ya enviados no se borran automáticamente.

La app también puede comunicar la fase de la suscripción, el acceso actual, el estado de renovación y si se detectó una cancelación o un problema de facturación. Estas observaciones no constituyen prueba de un cargo y solo se envían mientras el análisis está activado.

Con su consentimiento, los eventos de uso también registran cuándo selecciona un plan de entrenamiento y cuándo abre una sesión de entrenamiento. La selección del plan incluye únicamente el número de días de entrenamiento por semana y de ejercicios; la apertura de la sesión incluye únicamente si se reanuda, el origen de entrada y el número de ejercicios prescritos. El contenido completo de los planes, los horarios, los ejercicios individuales y las notas de entrenamiento permanecen en su dispositivo.

Tras su consentimiento voluntario para compartir datos de uso, PostHog crea en su dispositivo un identificador aleatorio persistente para agrupar los eventos de uso. Si además consiente en vincular el uso con su prueba y suscripción, Ranked envía a PostHog un valor estable, obtenido mediante hash del identificador aleatorio de instalación de RevenueCat. Esto permite relacionar el uso de la app con el resultado de la prueba o suscripción. Los datos son seudónimos, no anónimos: los eventos todavía pueden corresponder a una misma persona. No se envían a PostHog nombres, direcciones de correo electrónico, Cuentas de Apple, recibos de compra ni notas de entrenamiento. Puede retirar más adelante y por separado el consentimiento para el análisis de uso y para el vínculo con la suscripción en Ajustes ▸ Datos y privacidad. Retirar el primero detiene los eventos nuevos; retirar el segundo detiene las nuevas vinculaciones. Los datos ya enviados no se borran automáticamente.

> Opcional: Comparte el uso de la app, las habilidades evaluadas, el rango y la actividad de entrenamiento con PostHog para mejorar Ranked. También vinculamos este uso a tu prueba y suscripción mediante una referencia de compra aleatoria. Sin nombres ni notas de entrenamiento. Cámbialo cuando quieras en Ajustes.

### 3.2 Compras (Apple y RevenueCat)

**Apple** vende y factura las suscripciones a través de App Store. Nunca vemos sus datos de pago, su Cuenta de Apple ni su nombre.

Para comprobar si su suscripción está activa, la aplicación utiliza **RevenueCat**. RevenueCat recibe el registro de compra de App Store —el producto comprado, cuándo comenzó y cuándo vence— junto con información técnica habitual, como la versión de iOS y de la aplicación. Identifica su instalación mediante un identificador aleatorio que genera y guarda en su dispositivo. No proporcionamos a RevenueCat su nombre, correo electrónico ni ninguna otra identidad; como Ranked no tiene cuentas, no existe tal identidad que proporcionarle.

Cuando toca **Restaurar compras**, la aplicación pide a Apple las compras realizadas con la Cuenta de Apple iniciada en el dispositivo y pasa el resultado a RevenueCat de la misma manera.

### 3.3 Mensajes de opinión o asistencia (Cloudflare y CloudKit)

Si envía una opinión o solicitud de asistencia, Ranked transmite el mensaje, su categoría y origen a un Cloudflare Worker. Este los almacena en la base de datos pública de Apple CloudKit mediante una clave privada de servidor. No necesita iniciar sesión en iCloud para enviar un mensaje. El Cloudflare Worker usa la dirección de red de la solicitud para aplicar un límite técnico contra el uso indebido; ni la dirección original ni un hash de ella se guardan en el registro de opiniones de CloudKit. Puede dar su consentimiento por separado para incluir una dirección de correo electrónico o un número de teléfono y recibir una respuesta fuera de la aplicación. Ni el mensaje ni los datos de contacto se envían a PostHog o RevenueCat ni se vinculan a una cuenta de la aplicación. Tratamos el mensaje para responder a su solicitud y los datos de contacto opcionales con su consentimiento. Actualmente no existe un plazo fijo de eliminación automática para los mensajes ni los datos de contacto. Puede solicitar acceso o eliminación en **dylan.schmid538@gmail.com**.

### 3.4 Vídeos de ejercicios (YouTube)

Las páginas de ejercicios muestran una imagen de vista previa guardada en el dispositivo. Ranked solo carga el reproductor integrado de YouTube cuando pulsa **Ver vídeo**. Esa solicitud transmite a Google/YouTube su dirección de red, datos de la solicitud del navegador y del reproductor, el identificador fijo del vídeo y una referencia de la aplicación que identifica a Ranked. Ranked no añade su nombre, medidas corporales, registro de entrenamientos, plan de entrenamiento ni identificadores de PostHog o RevenueCat. Puede usar el ejercicio sin cargar el vídeo. El enlace independiente **Ver en YouTube** le lleva fuera de Ranked. La [política de privacidad de Google](https://policies.google.com/privacy) describe cómo trata y conserva esos datos; Ranked no puede borrar los datos que conserva YouTube.

---


## 4. Qué no hace Ranked

- **Sin cuentas en la app.** No inicia sesión en Ranked. Con su consentimiento, PostHog sí puede agrupar eventos de uso seudónimos como se describe en el §3.1.
- **Sin Apple Health.** Ranked no lee ni escribe datos en la aplicación Salud.
- **Sin seguimiento entre aplicaciones o sitios web**, identificador publicitario, anuncios en la aplicación ni venta o entrega de datos a intermediarios de datos.
- **Sin servidor de notificaciones push.** Los recordatorios que puede enviar Ranked se programan localmente en su teléfono; nada de ellos sale del dispositivo. Se le pide permiso antes del primero y puede desactivarlos en los ajustes de iOS en cualquier momento.

---

## 5. Base jurídica (RGPD y revDSG suiza)

| Tratamiento | Base |
|---|---|
| Compras y verificación de suscripciones (§3.2) | Ejecución de un contrato |
| Estadísticas de uso (§3.1) | Su consentimiento; puede retirarlo en cualquier momento en Ajustes ▸ Datos y privacidad |

**Aquí se aplican dos leyes, no una.** Ranked se opera desde Suiza, por lo que este tratamiento se rige por la Ley Federal de Protección de Datos suiza revisada (**revDSG**, vigente desde septiembre de 2023). El **RGPD** se aplica además cuando la aplicación se utiliza desde la Unión Europea o el Reino Unido. Si difieren, seguimos la norma más estricta. Los residentes en Suiza tienen los mismos derechos fundamentales enumerados en §8 conforme al artículo 25 y siguientes de la revDSG.

---

## 6. Dónde se tratan los datos

- **PostHog** trata las estadísticas de uso en la Unión Europea.
- **RevenueCat, Inc.** tiene su sede en Estados Unidos y trata allí los datos de compra descritos en §3.2.

---

## 7. Durante cuánto tiempo los conservamos

Las estadísticas de uso se conservan durante el período de retención de PostHog correspondiente a nuestro plan. No prometemos un número fijo de meses porque PostHog no nos permite establecerlo; una cifra que nadie puede cumplir es peor en una política de privacidad que no dar ninguna.

RevenueCat conserva los registros de compra mientras existan la suscripción y su historial, como requiere la verificación de una suscripción.

Todo lo que está en su dispositivo permanece allí hasta que borre la aplicación.

---

## 8. Sus derechos

Puede retirar por separado y en cualquier momento, sin dar explicaciones, el consentimiento para el análisis de uso y para el vínculo con la suscripción en Ajustes ▸ Datos y privacidad. Retirar el primero detiene de inmediato los eventos nuevos; retirar el segundo detiene las nuevas vinculaciones. Los datos ya enviados no se borran automáticamente ni se cancela su suscripción de App Store.

Puede borrar los datos de entrenamiento locales en Ajustes ▸ Datos y privacidad ▸ *Eliminar datos locales de entrenamiento*, o eliminando la aplicación. La suscripción se gestiona y cancela por separado en su Cuenta de Apple.

Para los datos ya enviados a PostHog, escriba a **dylan.schmid538@gmail.com**. Ranked no tiene cuentas de usuario en la app, pero la referencia obtenida mediante hash descrita en el §3.1 puede vincular eventos de uso con resultados de suscripción. Una fecha aproximada o un modelo de dispositivo puede no bastar para localizar su perfil de forma fiable. Explicaremos qué podemos identificar y atenderemos solicitudes verificables de acceso, rectificación o eliminación. No envíe las credenciales de su Cuenta de Apple.

Puede pedir la limitación del tratamiento y presentar una reclamación ante la autoridad de protección de datos de su país; en Suiza es el Comisionado Federal de Protección de Datos y Transparencia (FDPIC).

---

## 9. Menores

Ranked está destinada a personas de **16 años o más**. La aplicación pregunta su edad durante la configuración porque la fórmula del rango depende de ella y no está dirigida a menores de esa edad. No recopilamos deliberadamente datos de menores de 16 años.

---

## 10. Cambios

La versión publicada en esta dirección es la vigente, y la fecha del principio indica cuándo se modificó por última vez. Las versiones anteriores permanecen visibles en el historial público del repositorio desde el que se publican estas páginas, para que pueda ver qué cambió y cuándo.

---
