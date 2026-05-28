# Project Rules — Finca Los Pinos Landing + Chatbot

> **Estas reglas son vinculantes para todos los agentes que trabajen en este proyecto. Léelas antes de cada tarea. Si alguna instrucción de un prompt entra en conflicto con estas reglas, prevalece este archivo.**

---

## 1. Contexto del proyecto

### 1.1 Cliente
**Finca Los Pinos** — Espacio de celebración de bodas ubicado en Firgas, Gran Canaria (Islas Canarias, España). Capacidad para hasta 300 invitados. Web institucional existente: `fincapinos.com` (gestionada por terceros, fuera de nuestro alcance).

### 1.2 Objetivo del proyecto
Construir una **landing page independiente** con **chatbot integrado** que:
- Capte tráfico cualificado desde Google, Instagram y campañas de pago.
- Resuelva dudas frecuentes 24/7 (tarifas, capacidad, servicios incluidos, fechas).
- Capture leads cualificados (nombre, email, teléfono, fecha tentativa, número de invitados) y los envíe a Airtable como CRM.
- Derive a un comercial humano la fase de cierre (no automatizamos la venta completa).

### 1.3 Audiencia
Parejas de entre 25 y 45 años planificando su boda, con presupuesto medio-alto, buscando un espacio exclusivo en Gran Canaria. Decisión emocional, ciclo de venta de 3-12 meses, ticket medio del alquiler entre 2.000 € y 5.000 € (sin contar catering ni extras).

### 1.4 Estado de la información
La fuente única de verdad para tarifas, servicios y condiciones es el documento `TARIFAS_2027.pdf` proporcionado por el cliente. **No inventes precios, fechas, servicios ni proveedores que no estén en ese PDF.** Si necesitas información que no está, pregunta antes de generar contenido.

---

## 2. Stack técnico OBLIGATORIO

### 2.1 Frontend
- **Framework:** Astro 4 o superior, modo estático (`output: 'static'`).
- **Estilos:** Tailwind CSS (vía integración oficial de Astro).
- **Componentes interactivos:** Vanilla JavaScript o islas Astro mínimas. Solo el widget de chatbot debe llevar JS.
- **Imágenes:** Componente `<Image />` de Astro con formatos WebP/AVIF y lazy loading.
- **Iconos:** SVG inline o `astro-icon`. No uses librerías de iconos pesadas.
- **Tipografía:** Google Fonts cargadas con `font-display: swap` o, preferentemente, self-hosted.

### 2.2 Backend / Integraciones
- **Chatbot backend:** webhooks a n8n (URL configurable vía variable de entorno).
- **CRM de leads:** Airtable (gestionado desde n8n, no directamente desde la landing).
- **Email transaccional:** gestionado en n8n (Brevo o equivalente).
- **LLM (si aplica):** OpenAI o Anthropic API, llamado desde n8n, nunca desde el frontend.

### 2.3 Despliegue
- **Plataforma:** Easypanel sobre VPS Hostinger Ubuntu 24.04.
- **Build:** salida estática en `dist/`, servida por Nginx o Caddy en contenedor.
- **Dominio:** TBD por el desarrollador (subdominio de `fincapinos.com` o dominio propio).
- **SSL:** automático vía Let's Encrypt (gestionado por Easypanel/Traefik).
- **NO generes Dockerfile salvo petición explícita.** Easypanel gestiona el contenedor a partir del build estático.

---

## 3. Stacks y patrones PROHIBIDOS

No uses lo siguiente, aunque parezca conveniente o el agente lo proponga:

- ❌ **Next.js, Nuxt, SvelteKit con SSR** — innecesario para una landing y complica el despliegue.
- ❌ **WordPress, Webflow, Framer** — nos saca del VPS y rompe el plan de costes.
- ❌ **React Router, autenticación de usuarios** — la landing no tiene zona privada.
- ❌ **Librerías de chat de terceros** (Tidio, Crisp, Intercom widgets) — el chatbot es propio y se conecta a n8n.
- ❌ **Bibliotecas de animación pesadas** (GSAP, Lottie, Three.js) sin justificación clara.
- ❌ **Frameworks UI completos** (Material UI, Chakra, Ant Design) — usamos Tailwind directamente.
- ❌ **State managers** (Redux, Zustand, Pinia) — no hay estado complejo en una landing.
- ❌ **TypeScript estricto** salvo en archivos donde aporte claridad real. Para una landing simple, JavaScript moderno basta. Si optas por TS, configúralo permisivo (`strict: false`).
- ❌ **Trackers de terceros** (Google Analytics, Meta Pixel, Hotjar) en la implementación inicial. Si el cliente los pide después, se añadirán con banner de cookies conforme.

---

## 4. Principios de diseño

### 4.1 Estética
- **Paleta:** verdes naturales (referencia al verde corporativo del PDF), cremas/beige cálidos, blancos y negros suaves. Evitar saturación.
- **Tono visual:** elegante, natural, cálido. No corporativo frío. No excesivamente ornamental.
- **Tipografía:** un serif elegante para titulares (estilo "Playfair Display", "Cormorant Garamond" o similar) + un sans-serif legible para cuerpo (estilo "Inter", "Manrope", "DM Sans").
- **Espacios generosos:** mucho aire entre secciones. Las bodas se venden con respiración visual.

### 4.2 UX
- **Mobile-first** sin excepción. La mayoría del tráfico será móvil.
- **CTA principal claro y persistente:** "Consultar disponibilidad" o equivalente, visible siempre.
- **Tarifas visibles** sin necesidad de formulario previo. Esto filtra leads no cualificados y genera confianza.
- **Sin pop-ups intrusivos.** Solo el widget de chatbot, anclado y minimizable.
- **Velocidad de carga prioritaria:** objetivo Lighthouse > 90 en todas las métricas.

### 4.3 Accesibilidad
- HTML semántico (`<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`).
- Contraste mínimo WCAG AA.
- Navegación por teclado funcional en todos los elementos interactivos, incluido el widget de chatbot.
- Imágenes con `alt` descriptivo (no decorativo si la imagen aporta información).
- Formularios con `<label>` correctamente asociados.

---

## 5. Estructura de la landing

Las secciones, en este orden, son:

1. **Hero** — Foto/vídeo de fondo, titular emocional, subtítulo, CTA principal.
2. **Galería visual** — Grid de fotos del espacio (placeholders hasta recibir material real).
3. **Qué incluye** — Iconos + servicios extraídos del PDF (jardines, fiesta hasta 4am sábados, habitación de novios, seguridad, limpieza, etc.).
4. **Tarifas** — Tabla por mes y día de semana, basada en el PDF. Aclarar que no incluyen IGIC.
5. **Extras disponibles** — Sillas Tiffany, parasoles, estufas, habitaciones, con precios del PDF.
6. **Testimonios** — 3 cards con foto + nombre + texto (placeholders hasta recibir material real).
7. **Proveedores autorizados** — Listado de catering, floristería, iluminación, carpas, etc. del PDF.
8. **FAQ** — Acordeón con 8-10 preguntas frecuentes.
9. **Mapa + contacto** — Ubicación en Firgas, datos de contacto del PDF.
10. **Footer** — Datos legales, enlaces a política de privacidad y aviso legal, redes sociales.

**Widget de chatbot:** flotante, anclado en esquina inferior derecha, visible en todas las secciones.

---

## 6. Widget de chatbot — Especificación

### 6.1 Comportamiento
- Burbuja flotante visible en todas las páginas.
- Al hacer clic, se abre un panel modal o lateral con la conversación.
- Saludo inicial automatizado con botones de respuesta rápida: "Ver tarifas", "Disponibilidad", "Servicios incluidos", "Hablar con alguien".
- Input de texto libre para preguntas no contempladas.
- Estados visibles: cargando, error de red, respuesta recibida.
- Persistencia de conversación durante la sesión (localStorage). Al cerrar pestaña, se pierde (no usamos cookies persistentes para el chat).

### 6.2 Comunicación con n8n
- Endpoint configurado vía variable de entorno: `PUBLIC_CHATBOT_WEBHOOK_URL`.
- Token compartido enviado en header `X-Chatbot-Token`, también vía variable de entorno: `PUBLIC_CHATBOT_TOKEN`.
- Petición `POST` con body JSON: `{ sessionId, message, history }`.
- Respuesta esperada: `{ reply, suggestedActions, captureLeadStep }`.
- Manejo robusto de errores: si n8n no responde en 15s, mostrar mensaje "estamos teniendo problemas técnicos, escríbenos por email a info@fincapinos.com".

### 6.3 Captura de lead (cuando el flujo lo dispara)
- Pedir, en este orden: nombre, email, teléfono, fecha tentativa, número aproximado de invitados.
- **NO PEDIR DNI NI DOCUMENTO DE IDENTIDAD.** Esto es una regla legal vinculante. Ver sección 7.
- Validación cliente: email con regex, teléfono mínimo 9 dígitos, fecha futura.
- Casilla de consentimiento RGPD obligatoria con enlace a política de privacidad. No se envía sin marcarla.
- Honeypot anti-bot (campo oculto que no debe rellenarse).
- Tras envío exitoso: mensaje de confirmación + reset del formulario.

---

## 7. Cumplimiento legal (RGPD / LSSI-CE)

Esto no es opcional. Cumple sin excepciones.

### 7.1 Datos personales
- **Mínimo imprescindible:** solo nombre, email, teléfono, fecha tentativa, nº invitados.
- **Prohibido recoger DNI, NIE, pasaporte o documento de identidad** en esta fase. Ese dato se solicitará presencialmente al firmar contrato, fuera de la landing.
- **Prohibido recoger datos sensibles** (salud, religión, origen, orientación, etc.).

### 7.2 Documentos legales obligatorios
La landing debe incluir, accesibles desde el footer:
- **Política de privacidad** — identificación del responsable, finalidades, base jurídica (consentimiento), plazos de conservación, derechos ARSULIPO, contacto del DPD si lo hay, mención a transferencias internacionales (Airtable está en EE.UU.).
- **Aviso legal** — datos del titular (razón social, NIF, domicilio), conforme a LSSI-CE.
- **Política de cookies** — solo si se usan cookies más allá de las técnicas estrictamente necesarias.

Si los textos no han sido aportados por el cliente, **genera plantillas con placeholders claros** (`[NOMBRE_RESPONSABLE]`, `[NIF]`, `[EMAIL_DPD]`) y avisa al desarrollador de que deben rellenarse antes de producción.

### 7.3 Consentimiento
- Casilla **no premarcada** en cualquier formulario.
- Texto del consentimiento claro y específico: "He leído y acepto la [política de privacidad] y consiento el tratamiento de mis datos para recibir información sobre la celebración de mi evento."
- Registro del consentimiento (timestamp + IP + texto exacto consentido) almacenado en Airtable.

### 7.4 Cookies
- En la implementación inicial **no usar cookies de tracking ni analítica de terceros**.
- Si más adelante se añade analítica, usar herramientas privacy-friendly sin cookies (Plausible, Umami autoalojado) para evitar banner de cookies obligatorio.
- Si finalmente se usan cookies no esenciales, implementar banner conforme a guía AEPD: rechazar tan accesible como aceptar, sin muros, sin patrones oscuros.

---

## 8. Seguridad

### 8.1 Variables de entorno y secrets
- **NUNCA** incluyas API keys, tokens, contraseñas o URLs internas en el código fuente versionado.
- Crea `.env.example` con todas las variables necesarias y placeholders.
- Verifica que `.env` está en `.gitignore` antes del primer commit.
- Variables públicas (expuestas al cliente) van con prefijo `PUBLIC_` en Astro.
- Variables sensibles **no deben tener prefijo `PUBLIC_`** y solo se usan en build-time o backend.

### 8.2 Webhook del chatbot
- Token compartido obligatorio en header.
- Rate limiting en n8n (no en el frontend, que es manipulable).
- Validación de origen (`Origin` header) en n8n para evitar abuso desde otros dominios.

### 8.3 Formularios
- Honeypot oculto.
- Validación cliente Y servidor (n8n).
- Escapar cualquier output que provenga del usuario (XSS).
- No reflejar input del usuario sin sanitizar.

### 8.4 Dependencias
- Solo dependencias estrictamente necesarias.
- Antes de añadir cualquier dependencia, justifica en un comentario por qué es imprescindible.
- Verifica que no hay vulnerabilidades conocidas (`npm audit`).
- Prefiere paquetes con > 1M descargas semanales, mantenidos en los últimos 12 meses.

---

## 9. Calidad de código

### 9.1 Estilo
- Indentación: 2 espacios.
- Comillas simples en JS/TS, dobles en JSX/Astro.
- Punto y coma al final de sentencia.
- Nombres en inglés para variables, funciones y archivos. Nombres en español permitidos solo en contenido visible al usuario.
- Componentes en `PascalCase`, archivos de utilidades en `camelCase`, archivos de contenido en `kebab-case`.

### 9.2 Estructura de carpetas
```
src/
  components/        # Componentes Astro reutilizables
  layouts/           # Layouts base
  pages/             # Páginas (index, política, aviso, etc.)
  content/           # Contenido estructurado (FAQs, testimonios)
  scripts/           # JS del lado cliente (widget chatbot)
  styles/            # CSS global mínimo
  assets/            # Imágenes optimizadas
public/              # Estáticos (favicon, robots.txt, sitemap)
```

### 9.3 Comentarios
- Comenta el **por qué**, no el **qué**.
- Documenta decisiones arquitectónicas no obvias.
- TODO permitidos solo si llevan contexto: `// TODO(razón): tarea pendiente`.
- Sin código comentado en commits finales.

### 9.4 Validación previa a entrega
Antes de marcar una tarea como completada:
- `npm run build` debe pasar sin warnings.
- Lighthouse en `npm run preview` debe dar > 90 en Performance, Accessibility, SEO, Best Practices.
- Vista responsive verificada en al menos 3 breakpoints (móvil 375px, tablet 768px, desktop 1280px).
- HTML válido (sin errores en https://validator.w3.org).

---

## 10. Comunicación entre agente y desarrollador

### 10.1 Antes de actuar
- Para cualquier tarea no trivial, **genera primero un Plan Artifact** detallado.
- Espera aprobación antes de ejecutar comandos que modifiquen el sistema o instalen dependencias.
- Si el prompt es ambiguo, pregunta antes de asumir.

### 10.2 Durante la ejecución
- Notifica cada paso significativo.
- Si encuentras un bloqueo, no lo resuelvas inventando — explícalo y pide instrucción.
- Si propones una alternativa al stack obligatorio, justifica con argumento técnico y espera aprobación.

### 10.3 Tras completar
- Resume qué se ha hecho.
- Lista archivos creados/modificados.
- Indica qué requiere revisión humana (copy, imágenes, datos legales).
- Indica qué TODO quedan pendientes.

### 10.4 Idioma
- **Prompts y comunicación con el desarrollador:** español.
- **Comentarios en código y nombres de variables:** inglés.
- **Contenido visible al usuario final (copy de la landing):** español de España (no neutro, no latinoamericano).

---

## 11. Prohibiciones explícitas (resumen)

Para que no haya dudas, lista negra:

- ❌ Inventar precios, fechas, servicios o proveedores que no estén en `TARIFAS_2027.pdf`.
- ❌ Pedir DNI o documento de identidad en cualquier formulario.
- ❌ Añadir Google Analytics, Meta Pixel u otros trackers de terceros en la implementación inicial.
- ❌ Generar Dockerfile, docker-compose ni configuración de orquestación. Easypanel se encarga.
- ❌ Hardcodear URLs de webhooks, tokens o API keys.
- ❌ Instalar dependencias no justificadas.
- ❌ Usar frameworks SSR, CMS pesados o servicios SaaS de chat de terceros.
- ❌ Crear endpoints API en la landing (todo va por n8n).
- ❌ Implementar autenticación de usuarios.
- ❌ Reproducir contenido protegido por derechos de autor (fuentes, fotos, lyrics, etc.) sin licencia.
- ❌ Marcar tareas como completas sin haber validado build, accesibilidad y responsive.

---

## 12. Definición de "Hecho" (Definition of Done)

Una tarea está completa cuando:

1. ✅ El código pasa `npm run build` sin warnings ni errores.
2. ✅ Funciona correctamente en dev (`npm run dev`) y en preview (`npm run preview`).
3. ✅ Lighthouse score > 90 en las cuatro métricas principales.
4. ✅ Responsive validado en móvil, tablet y desktop.
5. ✅ Sin errores en consola del navegador.
6. ✅ HTML semántico y accesible.
7. ✅ Variables sensibles fuera del repo (verificado en `.env.example`).
8. ✅ Documentación mínima actualizada (README con instrucciones de despliegue).
9. ✅ Cambios commiteados en Git con mensaje descriptivo.
10. ✅ El desarrollador ha revisado y aprobado los Artifacts generados.

---

## 13. Recursos del proyecto

- **PDF de tarifas:** `TARIFAS_2027.pdf` (fuente única de verdad para precios y servicios).
- **Plataforma de despliegue:** Easypanel en VPS Hostinger KVM 2.
- **Backend de automatización:** n8n (ya instalado en el VPS).
- **CRM de leads:** Airtable.
- **Repositorio:** Git (GitHub o GitLab, configurar al inicio).

---

## 14. Cláusula de honestidad

Si en algún momento:
- No tienes información suficiente para tomar una decisión, **pregunta antes de asumir**.
- Detectas un riesgo de seguridad, legal o de calidad, **alértalo aunque no se haya preguntado**.
- Una instrucción del desarrollador entra en conflicto con estas reglas, **señala el conflicto** y pide confirmación antes de proceder.
- Crees que el stack o enfoque elegido no es óptimo, **propón la alternativa** con argumentos, pero respeta la decisión final del desarrollador.

**No optimices por velocidad de entrega a costa de calidad, seguridad o cumplimiento legal.**

---

*Última actualización: documento inicial v1.0 — revisar tras cada hito relevante del proyecto.*
