---
title: Política de privacidad · Calisthenics Skills – Ranked
permalink: /privacy/es/
---

> Esta es una traducción. En caso de discrepancia, prevalece la [versión en inglés](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Política de privacidad · Calisthenics Skills – Ranked

**Última actualización: 29 de septiembre de 2026**

Esta política explica qué datos recopila Ranked, adónde van y qué puede hacer usted al respecto. Se redactó a partir del código real de la aplicación, no de una plantilla; si algo aquí es incorrecto, hay que comprobar el código.

Ranked está operada por **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suiza**, contacto **dylan.schmid538@gmail.com**. Ella es la responsable del tratamiento descrito aquí.

---

## 1. En pocas palabras

Ranked **no tiene cuentas de usuario ni servidor propio**. Todo lo relacionado con su entrenamiento —cada serie registrada, su progreso en cada habilidad, su rango, su Power Level y su mapa corporal— se almacena en su teléfono y no se sube a ningún sitio.

**Su edad, sexo, altura y peso corporal nunca salen de su dispositivo.** La fórmula del rango los utiliza en el teléfono. No se nos envían a nosotros ni al servicio de análisis.

Solo salen de su dispositivo estas dos categorías:

1. **Estadísticas anónimas de uso**, para saber cómo se utiliza la aplicación. Puede desactivarlas en la aplicación en cualquier momento.
2. **Datos de compra**, para verificar la suscripción de App Store. Apple gestiona el pago; nosotros nunca vemos sus datos de pago.

Ranked no le rastrea entre otras aplicaciones o sitios web, no muestra publicidad y no lee nada de Apple Health.

---

## 2. Qué permanece en su dispositivo

Lo siguiente se guarda en la base de datos de la aplicación en su teléfono y nunca se transmite:

- Cada entrenamiento, serie, repetición, mantenimiento y peso añadido que registre
- Su progreso en cada habilidad y etapa, su historial de rangos y su Power Level
- Su plan y horario de entrenamiento, recordatorios y preferencias
- Las medidas corporales que haya introducido (edad, sexo, altura y peso corporal)
- Sus notas de entrenamiento

La aplicación no excluye esta base de datos de la copia de seguridad de su dispositivo. Si usa iCloud Backup o una copia de seguridad en un ordenador, sus datos de entrenamiento forman parte de ella y vuelven al restaurarla, según las condiciones de Apple, no las nuestras.

Al borrar la aplicación, se elimina todo esto del dispositivo. No podemos recuperarlo porque nunca lo tuvimos.

---

## 3. Qué sale de su dispositivo

### 3.1 Estadísticas de uso (PostHog)

Utilizamos **PostHog**, alojado en la **Unión Europea**, para entender cómo se usa la aplicación. La aplicación le envía una lista fija de eventos:

- a qué paso de configuración llegó, cuál completó o desde cuál retrocedió y cuánto tardó cada uno;
- qué resultó de la evaluación inicial: cuántas líneas de habilidades y etapas marcó como logradas, qué habilidad eligió como objetivo, su rango inicial y el rango de cada una de sus seis regiones corporales;
- cuándo se mostró o cerró la pantalla de compra y cuándo se inició, completó o restauró una compra, con el producto y la oferta correspondientes; cuándo la aplicación detecta después un período de prueba o de suscripción de pago activo, con el producto y si se trata de una compra de prueba (no es un registro de todos los cargos y no se envía mientras la aplicación está cerrada);
- cuándo cambió su rango y qué habilidad provocó el cambio;
- cuándo completó una etapa: qué habilidad y etapa, y si procedía de una serie registrada, un entrenamiento añadido a posteriori o una confirmación manual;
- qué pantallas abre y cuándo termina un entrenamiento. El evento de fin de entrenamiento no contiene detalles: ni ejercicios, ni series, ni cifras.

El software de PostHog dentro de la aplicación también añade a cada evento información técnica habitual, como el modelo de su dispositivo, la versión de iOS y de la aplicación, el idioma y la zona horaria, y registra cuándo se abre la aplicación y cuándo pasa a segundo plano. Como cualquier servicio de internet, PostHog recibe la dirección IP de la solicitud; puede deducir de ella una ubicación aproximada (país o ciudad).

**Qué no se incluye:** ni nombre, ni dirección de correo electrónico (la aplicación nunca la pide), ni identificador de cuenta (no existe), ni edad, sexo, altura, peso corporal o contenido de sus entrenamientos.

**Cómo se le identifica:** PostHog genera un identificador aleatorio cuando la aplicación se ejecuta por primera vez y lo guarda en su dispositivo. Todos los eventos se agrupan bajo ese identificador. La aplicación nunca le dice a PostHog quién es usted y no hay cuenta ni correo electrónico que pudiera comunicarle.

**Desactivación:** Ajustes ▸ Privacidad ▸ *Compartir datos de uso anónimos*. Al desactivarlo, la aplicación deja de enviar eventos desde ese momento. El ajuste se guarda en su dispositivo y se mantiene tras las actualizaciones.

### 3.2 Atribución de Apple Search Ads

Si instaló Ranked después de tocar un anuncio de Apple Search Ads, la aplicación pregunta a Apple una sola vez, en el primer inicio, de dónde vino la instalación. Apple responde con la campaña, el grupo de anuncios, la palabra clave y el conjunto creativo del anuncio, el país o región y la fecha del clic, y si fue una descarga nueva o repetida. La aplicación adjunta esos valores al identificador anónimo de PostHog descrito en §3.1 para agrupar cada evento posterior según el anuncio que le llevó a la aplicación.

Esto utiliza el framework **AdServices** de Apple, que no emplea el identificador publicitario (IDFA) y que Apple no considera seguimiento; por eso no aparece un diálogo de permiso de seguimiento. Si no llegó mediante un anuncio, Apple lo indica y no se adjunta nada más. Desactivar las estadísticas de uso (§3.1) también detiene esto.

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
| Estadísticas de uso (§3.1) | Interés legítimo en entender y mejorar la aplicación; puede oponerse en cualquier momento desactivándolas, véase §8 |
| Atribución de Search Ads (§3.2) | Interés legítimo en saber qué publicidad funciona; oposición como arriba |

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

En cualquier momento puede:

- **Desactivar las estadísticas de uso** en Ajustes ▸ Privacidad. Es su derecho a oponerse y, cuando el tratamiento se base en el consentimiento, a retirarlo; tiene efecto inmediato y no necesita dar razones.
- **Eliminar sus datos.** Como Ranked no guarda nada sobre usted en un servidor, al borrar la aplicación se elimina todo lo que almacena la propia aplicación.
- **Pedirnos que eliminemos su perfil analítico anónimo.** No podemos localizarlo por nombre porque no lo tiene; si nos escribe con la fecha aproximada en que usó la aplicación por primera vez y el dispositivo utilizado, lo localizaremos manualmente y lo eliminaremos.
- **Solicitar una copia** de los datos que tenga un servicio bajo su identificador, pedir que se **corrijan** o que se **limite** su tratamiento mientras se estudia una solicitud.
- **Reclamar ante una autoridad de control** de su país; en Suiza, el Comisionado Federal de Protección de Datos y Transparencia (FDPIC).

Escriba a **dylan.schmid538@gmail.com** para cualquiera de estos asuntos.

---

## 9. Menores

Ranked está destinada a personas de **16 años o más**. La aplicación pregunta su edad durante la configuración porque la fórmula del rango depende de ella y no está dirigida a menores de esa edad. No recopilamos deliberadamente datos de menores de 16 años.

---

## 10. Cambios

La versión publicada en esta dirección es la vigente, y la fecha del principio indica cuándo se modificó por última vez. Las versiones anteriores permanecen visibles en el historial público del repositorio desde el que se publican estas páginas, para que pueda ver qué cambió y cuándo.

---

> **⚠️ No es asesoramiento jurídico.** Este documento fue redactado por un ingeniero a partir del código fuente de la aplicación, no por un abogado. Describe el sistema con precisión a la fecha indicada; cada afirmación se comprobó frente a lo que la aplicación realmente envía. **No** se ha revisado su cumplimiento del RGPD, la revDSG suiza, la CCPA ni ninguna otra normativa. Publicarlo satisface a Apple, pero no garantiza el cumplimiento legal. Pida a un abogado que lo revise cuando la aplicación genere ingresos.
