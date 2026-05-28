# PRD — Landing Page + Chatbot Finca Los Pinos

> **Product Requirements Document**
> Versión 1.0 · Documento inicial
>
> Documento complementario al archivo `RULES.md` ya cargado en Antigravity. Mientras `RULES.md` define cómo trabajar (instrucciones imperativas para el agente), este PRD define qué se construye y por qué.

---

## 1. Resumen ejecutivo

### 1.1 Visión
Construir una **landing page de captación independiente** para Finca Los Pinos, premiada **7 años consecutivos** con los Wedding Awards de Bodas.net (2020–2026), con un **chatbot inteligente integrado** que responda dudas frecuentes 24/7 y capture leads cualificados hacia el equipo comercial.

### 1.2 Problema a resolver
- La web institucional `fincapinos.com` no es propiedad ni está gestionada por el equipo que ejecuta este proyecto.
- Las consultas de tarifas, disponibilidad y servicios llegan por canales dispersos (teléfono, email, redes sociales, bodas.net) sin centralización.
- No existe automatización en la primera línea de atención: cada consulta consume tiempo del comercial.
- No hay un canal propio que permita captar tráfico desde campañas Meta/Google y derivar contactos cualificados.

### 1.3 Solución propuesta
Una landing page moderna, emocional y de alta conversión, alojada en un dominio propio o subdominio dedicado, con:
- Información completa y transparente (incluida tabla de tarifas).
- Widget de chatbot que resuelve consultas frecuentes y captura leads.
- Integración con n8n y Airtable para automatizar el flujo comercial.
- Pruebas sociales claras (premios verificables, valoración 4.9/5 en bodas.net, 370+ parejas).

### 1.4 Métricas de éxito (KPIs)
| KPI | Objetivo a 6 meses |
|---|---|
| Visitas mensuales únicas | 1.500+ |
| Tasa de conversión visita → lead | ≥ 3% |
| Leads cualificados/mes (con fecha y nº invitados) | 30–50 |
| Tasa de respuesta del chatbot sin intervención humana | ≥ 70% |
| Lighthouse Performance/SEO/Accessibility/Best Practices | > 90 todas |
| Tiempo de carga (LCP) en móvil 4G | < 2.5 s |

> ⚠️ Estos objetivos son orientativos y deben validarse con el cliente. Si el volumen actual de consultas es mucho menor, conviene ajustarlos a la baja para los primeros meses.

---

## 2. Contexto del cliente

### 2.1 Sobre Finca Los Pinos
- **Ubicación:** Calle Lomo Obrero 21, Firgas, Gran Canaria, Las Palmas (España).
- **Capacidad:** hasta 300 invitados.
- **Año de actividad:** más de 15 años de experiencia (según el PDF aportado).
- **Posicionamiento:** espacio exclusivo, natural, premium, rodeado de jardines y arboledas.
- **Servicios principales:** alquiler de finca para bodas y eventos, alojamiento (7 habitaciones, hasta 14 personas), suite de novios.

### 2.2 Reconocimientos verificables
- **Wedding Awards Bodas.net** consecutivos: **2020, 2021, 2022, 2023, 2024, 2025 y 2026** (7 ediciones a fecha actual).
- **Valoración Bodas.net:** 4.9/5 con 181 opiniones, **98% de parejas recomiendan**.
- **Más de 370 parejas** han contratado el espacio.
- **Recomendado en Zankyou** (badge presente en la web oficial).
- Distintivo **Health & Safety**.

> **Estos datos son los únicos verificables y los únicos que deben usarse como prueba social. No se inventarán testimonios, premios ni reconocimientos adicionales.**

### 2.3 Audiencia objetivo (buyer persona)
- **Perfil principal:** parejas de 28–42 años, residentes en Gran Canaria o canarios en la diáspora que vuelven a casarse a la isla.
- **Perfil secundario:** parejas de Península/Europa que buscan destination wedding en Canarias.
- **Comportamiento digital:** uso intensivo de Instagram, Pinterest, bodas.net. Comparan 5–10 fincas antes de decidir.
- **Motivadores:** belleza del espacio, pruebas sociales, transparencia de precios, facilidad para contactar.
- **Frenos:** falta de información clara, opacidad de precios, fincas que parecen industriales o frías.

---

## 3. Alcance del proyecto

### 3.1 Dentro del alcance (MVP)
- Landing page de página única (one-page) con anclas de navegación.
- Sistema de diseño completo y consistente (paleta, tipografía, componentes).
- Galería visual con placeholders preparados para fotografía profesional posterior.
- Tabla de tarifas interactiva (selector mes + día → precio orientativo).
- Sección de FAQs.
- Widget de chatbot integrado, conectado a n8n vía webhook.
- Captura de leads con consentimiento RGPD, integración con Airtable vía n8n.
- Páginas legales (política de privacidad, aviso legal, política de cookies si aplica).
- Despliegue en Easypanel sobre VPS Hostinger existente.
- Configuración de dominio y SSL automático.
- Documentación técnica básica (README de despliegue).

### 3.2 Fuera del alcance (futuro)
- Sistema de reservas online (la finca usa Amenitiz para alojamiento, que queda fuera).
- Pasarela de pago.
- Multi-idioma (la v1 será solo español; inglés en fase 2 si la captación internacional lo justifica).
- Blog o sección de noticias.
- Integración con CRM externo (Hubspot, Salesforce…).
- App móvil nativa.
- Chatbot por voz.
- Automatización completa del cierre comercial (la conversión final sigue siendo humana).

### 3.3 Asunciones
- El equipo del proyecto tiene acceso al VPS Hostinger con n8n ya instalado.
- El cliente proporcionará material fotográfico profesional antes del lanzamiento (o se contratará sesión específica).
- El cliente revisará y aprobará textos legales antes de publicación.
- Existe un correo de contacto y teléfono activos para incluir como fallback humano.

### 3.4 Restricciones
- No se modifica `fincapinos.com` (dominio gestionado por terceros).
- No se contrata SaaS de chat de terceros (Intercom, Crisp, etc.).
- No se usa WordPress ni constructores visuales (Webflow, Framer).
- Stack obligatorio definido en `RULES.md` (Astro + Tailwind + Vanilla JS).

---

## 4. Requisitos funcionales

### 4.1 RF-001 · Hero principal
- Imagen o vídeo de fondo de alta calidad (placeholder en v1).
- Titular emocional que conecte con la promesa del espacio.
- Subtítulo con el dato diferencial (capacidad, ubicación, premio).
- Badge de Wedding Awards Bodas.net visible.
- CTA primario "Consultar disponibilidad" que abre el chatbot.
- CTA secundario "Ver tarifas" que hace scroll a la sección.

### 4.2 RF-002 · Reconocimientos y prueba social
- Badge oficial Wedding Awards Bodas.net (2020–2026).
- Mención: "Más de 370 parejas nos han elegido".
- Valoración 4.9/5 con enlace al perfil de Bodas.net para verificar.
- Logos de medios o reconocimientos verificados (Zankyou, Health & Safety).

### 4.3 RF-003 · Galería visual
- Mínimo 8 imágenes + opcionalmente 1 vídeo corto.
- Grid responsive con lazy loading.
- Lightbox al hacer clic en cada imagen.
- Placeholders inteligentes en v1 (con texto que indique "Imagen pendiente de fotografía profesional").

### 4.4 RF-004 · Servicios incluidos
Reproducir literalmente del PDF la sección "Incluye":
- Uso de los jardines.
- Iluminación básica.
- Personal de seguridad.
- Fiesta hasta 04:00 sábados / 02:00 viernes / 23:59 domingos.
- 12 horas para eventos de día (excepto domingos).
- Derechos SGAE y AGEDI.
- Habitación de los novios (incluida noche de boda).
- 5 horas de limpieza de baños durante el evento.
- Habitación con desayuno incluido.

Cada servicio acompañado de icono SVG inline.

### 4.5 RF-005 · Tabla de tarifas
- Tabla mensual con tres columnas: Viernes, Sábado, Domingo.
- 12 filas (una por mes).
- Precios extraídos exactos del PDF `TARIFAS_2027.pdf`.
- Aviso visible: "Precios no incluyen IGIC".
- Aviso: "Tarifas válidas para contrataciones hasta diciembre 2026 (revisar con la finca)".
- Versión móvil: tabla colapsable o selector dropdown (mes + día → precio).

### 4.6 RF-006 · Extras y servicios adicionales
Listado de extras del PDF con precios:
- Sillas Tiffany champagne: 2 €/unidad.
- Parasoles 3x3 m: 25 €/unidad.
- Estufas de calor: 60 €/unidad.
- Personal limpieza baños: 25 €/persona/hora.
- Habitaciones Deluxe: 180 €/noche (IGIC incluido).
- Suite Los Pinos: 200 €/noche (IGIC incluido).

Aviso: "No está permitida la pirotecnia, el arroz ni el confeti. Sí pétalos y productos biodegradables."

### 4.7 RF-007 · Testimonios
- 3 testimonios destacados (placeholders en v1).
- Cada uno con: foto, nombre/iniciales, fecha de la boda, texto.
- Enlace a las opiniones completas en Bodas.net (4.9/5, 181 reseñas).

### 4.8 RF-008 · Proveedores autorizados
Listado del PDF agrupado por categorías:
- **Catering:** La Vaquita, Vintia, Yanioma, Chef Jose Rojano, Casa Pueblo, Barbacoa Canaria.
- **Floristería:** El Arriate.
- **Iluminación y sonido:** Grupo Ruido.
- **Carpas:** Tentación, Garcitecnia, Loype, Celebraciones Pg, Tents and Events.
- **Glitter:** Glitter Party.
- **Hora loca:** Party Animal.

Mostrar como grid de logos (placeholders si no se dispone de logos reales) o como listado tipográfico elegante.

### 4.9 RF-009 · FAQs
Acordeón con al menos 8 preguntas. Sugeridas:
1. ¿Cuál es la capacidad máxima?
2. ¿Qué incluye el alquiler de la finca?
3. ¿Hasta qué hora puede durar la fiesta?
4. ¿Se puede celebrar la ceremonia civil en la finca?
5. ¿Hay alojamiento para los invitados?
6. ¿Qué política tienen sobre arroz, confeti o pirotecnia?
7. ¿Cómo y cuándo se formaliza la reserva?
8. ¿Puedo elegir mi propio catering?

Las respuestas se extraen del PDF cuando estén ahí; si no, se marcan como TODO para validación con cliente.

### 4.10 RF-010 · Mapa y contacto
- Mapa estático (imagen o iframe ligero) con la ubicación: Calle Lomo Obrero 21, Firgas, Gran Canaria.
- Teléfono: +34 636 418 627 (con `tel:` link).
- Email: info@fincapinos.com.
- Enlaces a Instagram (`@finca_los_pinos`) y Facebook.
- Botón de WhatsApp directo opcional (con número del comercial).
- Indicaciones breves: "A 20 minutos de Las Palmas de Gran Canaria".

### 4.11 RF-011 · Footer
- Logo.
- Datos legales mínimos (razón social y NIF — placeholder hasta que el cliente confirme).
- Enlaces a páginas legales.
- Redes sociales.
- Crédito discreto del desarrollador (opcional, a decisión del cliente).

### 4.12 RF-012 · Widget de chatbot
Especificación detallada en `RULES.md` sección 6. Resumen:
- Burbuja flotante en esquina inferior derecha.
- Saludo automático al entrar (con delay 5–10 s para no ser invasivo).
- Botones rápidos: "Ver tarifas", "Disponibilidad", "Servicios", "Hablar con alguien".
- Input libre para preguntas no contempladas.
- Captura de lead: nombre, email, teléfono, fecha tentativa, nº invitados.
- **Prohibido pedir DNI o documento de identidad.**
- Casilla de consentimiento RGPD obligatoria.
- Comunicación con n8n vía webhook autenticado.

### 4.13 RF-013 · Páginas legales
- `/politica-de-privacidad`
- `/aviso-legal`
- `/politica-de-cookies` (solo si finalmente se usan cookies no esenciales)

Plantillas con placeholders claros para datos del responsable que el cliente debe completar.

---

## 5. Requisitos no funcionales

### 5.1 Rendimiento
- LCP (Largest Contentful Paint) < 2.5 s en móvil 4G.
- CLS (Cumulative Layout Shift) < 0.1.
- TTI (Time to Interactive) < 3.5 s.
- Peso total inicial < 500 KB (sin contar imágenes lazy-loaded).
- Imágenes optimizadas en WebP/AVIF con fallback JPG.

### 5.2 SEO
- Etiquetas meta completas (`title`, `description`, `og:`, `twitter:`).
- Schema.org markup `EventVenue` o `LocalBusiness` con datos estructurados.
- Sitemap.xml automático.
- robots.txt configurado.
- URL canónicas.
- Hreflang preparado para futura versión inglesa (no obligatorio en v1).

### 5.3 Accesibilidad
- WCAG 2.1 nivel AA mínimo.
- Contraste validado.
- Navegación por teclado completa.
- Lectores de pantalla compatibles.
- Foco visible.

### 5.4 Compatibilidad
- Navegadores: últimas 2 versiones de Chrome, Firefox, Safari, Edge.
- iOS Safari 15+, Chrome Android últimas 3 versiones.
- Resoluciones: 360px – 2560px de ancho.

### 5.5 Seguridad
- HTTPS obligatorio (Let's Encrypt vía Easypanel).
- Headers de seguridad: CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy.
- Rate limiting en webhook de n8n.
- Validación de origen en peticiones al chatbot.
- Variables sensibles en `.env`, nunca en repo.

### 5.6 Mantenibilidad
- Código documentado en lo no obvio.
- Estructura de carpetas clara.
- README con instrucciones de despliegue paso a paso.
- Variables de entorno documentadas en `.env.example`.

---

## 6. Sistema de diseño

### 6.1 Fuentes de inspiración
El sistema visual combina tres fuentes:

1. **PDF `TARIFAS_2027.pdf`** (en carpeta `/creación` del proyecto): aporta paleta corporativa actual (verdes naturales, cremas, blancos), tipografía con serif elegante para títulos.
2. **Web actual `fincapinos.com`**: aporta tono romántico/natural, fotografía de jardines, posicionamiento "donde tus sueños se hacen realidad".
3. **Archivo de referencia `muestralanding`** (en carpeta `/creación` del proyecto): modelo estructural y estético a emular en composición, ritmo visual y nivel de modernidad.

> ⚠️ **Importante:** No tengo acceso directo al archivo `muestralanding` desde aquí. **El agente de Antigravity debe abrirlo, analizar su composición, paleta concreta, tipografía, animaciones y ritmo visual, y combinarlo con las directrices abajo antes de empezar a maquetar.**

### 6.2 Paleta de colores propuesta

Basada en la observación del PDF (verde corporativo + cremas) y a validar/refinar con el archivo `muestralanding`:

| Rol | Color | Hex (orientativo) | Uso |
|---|---|---|---|
| **Verde principal** | Verde botánico profundo | `#3A6B47` aprox. | Titulares, CTAs primarios, acentos |
| **Verde secundario** | Verde sage suave | `#8FA98B` aprox. | Detalles, badges, hover states |
| **Crema base** | Crema cálida | `#F5EFE6` aprox. | Fondos de sección |
| **Blanco roto** | Off-white | `#FAFAF7` | Fondo principal |
| **Negro suave** | Carbón | `#2A2A2A` | Texto principal |
| **Gris medio** | Stone gray | `#7A7A7A` | Texto secundario |
| **Acento dorado** (opcional) | Champagne | `#C9A876` aprox. | Detalles premium, badges de premio |

> Los hex son **orientativos**. El agente debe extraer los valores exactos del PDF y del `muestralanding` y consolidar la paleta final.

### 6.3 Tipografía

| Uso | Familia sugerida | Alternativas |
|---|---|---|
| **Titulares (display serif)** | Playfair Display | Cormorant Garamond, DM Serif Display |
| **Cuerpo (sans-serif)** | Inter | DM Sans, Manrope |
| **Acentos / cursiva decorativa** | Italianno o similar | (uso muy puntual, no como cuerpo) |

Pesos: 400, 500, 600, 700.
Tamaños base: 16px cuerpo móvil, 18px cuerpo desktop. Escala modular ratio 1.25.

### 6.4 Tono visual y ritmo
- **Espacios generosos:** secciones con `padding-y` amplio (96–160px en desktop, 64–96px en móvil).
- **Composiciones asimétricas** sutiles, no perfectamente centradas.
- **Imágenes grandes** que respiren, sin marcos pesados.
- **Animaciones discretas** al hacer scroll (fade-in, slide-up suave). Nada que distraiga.
- **Hover states refinados** en CTAs y cards.
- **Iconografía:** SVG inline minimalista, lineal, no rellenos de color saturado.

### 6.5 Tono de copy
- **Cálido pero no empalagoso.**
- Trato en **vosotros** ("vuestra boda", "vuestros invitados") siguiendo la línea del PDF y la web oficial.
- **Frases cortas**, ritmo emocional.
- Evitar topicazos ("el día más importante de tu vida", "sueño hecho realidad" se usan con moderación, ya están en la web).
- **Datos concretos** generan confianza: "300 invitados", "7 años de Wedding Awards", "20 minutos de Las Palmas".

---

## 7. Arquitectura técnica

### 7.1 Stack
- **Framework frontend:** Astro 4+ (modo estático).
- **Estilos:** Tailwind CSS.
- **JS interactivo:** Vanilla JS (solo widget chatbot).
- **Backend lógica:** n8n (existente en VPS).
- **CRM/almacenamiento leads:** Airtable.
- **Email transaccional:** Brevo (gestionado en n8n).
- **(Opcional) LLM:** OpenAI o Anthropic API, llamada desde n8n.

### 7.2 Diagrama de despliegue

```
   Cloudflare (DNS + cache + protección)
                │
                ▼
   IP pública del VPS Hostinger
                │
                ▼
   Easypanel (Traefik interno con SSL automático)
                │
        ┌───────┴────────┐
        ▼                ▼
   bodas.dominio    n8n.dominio
   (landing Astro)  (n8n existente)
                         │
                         ▼
                   Webhook chatbot
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Airtable    LLM API    Brevo email
```

### 7.3 Flujo de captura de lead

```
1. Usuario abre chatbot en landing
2. Conversación → si detecta intención de reserva, pide datos
3. Usuario rellena: nombre, email, teléfono, fecha, nº invitados
4. Marca consentimiento RGPD
5. POST a webhook n8n con token autenticación
6. n8n valida token + origin
7. n8n inserta en Airtable (con timestamp consentimiento)
8. n8n envía email automático al usuario (confirmación)
9. n8n notifica al comercial (email/Telegram/Slack)
10. Comercial contacta por WhatsApp/teléfono en <24h
```

### 7.4 Estructura del repositorio

```
finca-los-pinos-landing/
├── .antigravity/
│   └── rules.md              # Reglas del proyecto (ya creadas)
├── creación/
│   ├── TARIFAS_2027.pdf
│   └── muestralanding/        # Diseño de referencia
├── src/
│   ├── components/
│   │   ├── Hero.astro
│   │   ├── Awards.astro
│   │   ├── Gallery.astro
│   │   ├── Includes.astro
│   │   ├── Pricing.astro
│   │   ├── Extras.astro
│   │   ├── Testimonials.astro
│   │   ├── Vendors.astro
│   │   ├── FAQ.astro
│   │   ├── ContactMap.astro
│   │   ├── Footer.astro
│   │   └── Chatbot/
│   │       ├── ChatbotWidget.astro
│   │       ├── chatbot.js
│   │       └── chatbot.css
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── politica-de-privacidad.astro
│   │   ├── aviso-legal.astro
│   │   └── politica-de-cookies.astro
│   ├── content/
│   │   ├── pricing.json
│   │   ├── faq.json
│   │   ├── vendors.json
│   │   └── testimonials.json
│   ├── styles/
│   │   └── global.css
│   └── assets/
│       └── images/
├── public/
│   ├── favicon.svg
│   ├── robots.txt
│   └── og-image.jpg
├── .env.example
├── .gitignore
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
└── README.md
```

---

## 8. Cumplimiento legal

### 8.1 Marco normativo aplicable
- **RGPD** (Reglamento UE 2016/679).
- **LOPDGDD** (Ley Orgánica 3/2018 de Protección de Datos y Garantía de Derechos Digitales).
- **LSSI-CE** (Ley 34/2002 de Servicios de la Sociedad de la Información).

### 8.2 Datos personales recogidos
| Dato | Obligatorio | Finalidad |
|---|---|---|
| Nombre | Sí | Personalización trato |
| Email | Sí | Envío de información solicitada |
| Teléfono | Sí | Contacto comercial |
| Fecha tentativa boda | Recomendado | Filtrar disponibilidad |
| Nº invitados | Recomendado | Calcular tarifa orientativa |
| **DNI/documento identidad** | **NO SE RECOGE** | Solo en firma de contrato presencial |

### 8.3 Base jurídica
**Consentimiento expreso** del interesado (Art. 6.1.a RGPD), obtenido vía casilla no premarcada en formularios de la landing y del chatbot.

### 8.4 Plazo de conservación
- Si no se contrata: **2 años** desde la última interacción.
- Si se contrata: el plazo legal aplicable a la operación comercial.
- El usuario puede solicitar supresión en cualquier momento.

### 8.5 Documentos a generar
- Política de privacidad (placeholder con datos del responsable a completar).
- Aviso legal (LSSI-CE).
- Política de cookies (solo si se usan cookies no esenciales).

### 8.6 Transferencias internacionales
- **Airtable:** servidor en EE.UU. — actualmente bajo Data Privacy Framework.
- **OpenAI/Anthropic (si se usan):** EE.UU. — bajo cláusulas contractuales tipo / DPF.
- Mencionar en política de privacidad.

---

## 9. Métricas, monitorización y analítica

### 9.1 Analítica web
- **Recomendado:** Plausible o Umami autoalojado en el mismo VPS — privacy-friendly, sin cookies, sin banner obligatorio.
- **No recomendado en v1:** Google Analytics 4, Meta Pixel — exigen banner de cookies y rompen la simplicidad.

### 9.2 Métricas a trackear
- Sesiones / usuarios únicos.
- Tasa de rebote por sección.
- Profundidad de scroll (¿llegan a la tabla de tarifas?, ¿al CTA final?).
- Eventos: apertura chatbot, mensaje enviado, lead capturado.
- Origen del tráfico (orgánico, redes, directo, ads).

### 9.3 Monitorización de salud
- **Uptime Kuma** autoalojado para alertas de caída.
- Logs de n8n revisables en Easypanel.
- Backup diario de Airtable (export CSV automatizado mensual al menos).

---

## 10. Plan de implementación

### Fase 0 — Preparación (1–2 días)
- Decisión final de dominio.
- Endurecimiento de n8n existente (2FA, token webhooks, backup externo).
- Configuración de DNS y Cloudflare.

### Fase 1 — Cimientos del proyecto (1–2 días)
- Inicialización del repo Astro + Tailwind.
- Sistema de diseño base (paleta, tipografías, componentes atómicos).
- Layout base + estructura de carpetas.
- Análisis del archivo `muestralanding` y consolidación de la paleta final.

### Fase 2 — Maquetación de secciones (3–5 días)
- Hero + Awards.
- Galería + Includes.
- Pricing + Extras.
- Testimonios + Vendors.
- FAQ + Contact + Footer.

### Fase 3 — Chatbot (2–3 días)
- Diseño del componente widget.
- Implementación de comunicación con n8n.
- Configuración de workflow n8n (recepción, lógica, captura lead).
- Integración con Airtable.
- Pruebas end-to-end.

### Fase 4 — Cumplimiento legal (1 día)
- Páginas legales con placeholders.
- Casillas de consentimiento.
- Headers de seguridad.
- Cookies si aplica.

### Fase 5 — Optimización y QA (1–2 días)
- Lighthouse > 90 en todas las métricas.
- Pruebas en distintos navegadores/dispositivos.
- Validación HTML/accesibilidad.
- Optimización de imágenes.

### Fase 6 — Despliegue y lanzamiento (1 día)
- Configuración de Easypanel.
- Conexión Git → deploy automático.
- Configuración de dominio + SSL.
- Pruebas finales en producción.
- Configuración de analítica y uptime.

**Total estimado:** 10–16 días de trabajo efectivo (puede acelerarse con Antigravity en buena parte de las fases 1–2).

---

## 11. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Falta de fotografía profesional para el lanzamiento | Alta | Alto | Plantear sesión fotográfica antes del lanzamiento o lanzar con placeholders explícitos |
| Cliente quiere recoger DNI por presión interna | Media | Alto | El PRD y RULES lo prohíben explícitamente; explicar riesgo legal |
| Datos de tarifas cambian en 2027 | Alta | Medio | Diseñar tabla de tarifas como JSON editable para actualizaciones rápidas |
| n8n cae o se bloquea por uso intensivo | Baja | Alto | Monitorización Uptime Kuma + fallback "envíanos email a info@" |
| Webhook expuesto sin token sufre abuso | Media | Medio | Token + rate limiting + validación de origin |
| Cliente no provee datos legales (NIF, razón social) | Media | Medio | Lanzar con placeholders y advertencia visible hasta tener datos |
| Bodas.net cambia política de badges/enlaces | Baja | Bajo | Dato verificado en propia web del cliente, fuente alternativa |
| Antigravity genera código sobreingeniero | Media | Medio | Reglas estrictas en `RULES.md`, revisión manual de cada Plan Artifact |
| Single point of failure en VPS | Baja | Alto | Backups externos diarios, plan de recuperación documentado |

---

## 12. Dependencias y bloqueantes

### 12.1 Dependencias bloqueantes (sin esto no se puede empezar)
- **Decisión de dominio**: subdominio de `fincapinos.com` (vía gestor del dominio principal) o dominio propio nuevo.
- **Acceso al VPS y Easypanel** verificado y funcional.
- **Acceso a la cuenta de Airtable** (crear o usar existente).

### 12.2 Dependencias importantes (necesarias antes del lanzamiento)
- **Datos legales del responsable**: razón social, NIF, dirección fiscal.
- **Material fotográfico**: fotos profesionales de la finca o autorización para usar las existentes en `fincapinos.com`.
- **Validación legal de textos** (política privacidad, aviso legal) — idealmente revisada por asesor.
- **Cuenta API LLM** si se opta por chatbot híbrido (OpenAI o Anthropic).

### 12.3 Dependencias deseables (mejoran resultado pero no bloquean)
- Logos en alta resolución de proveedores autorizados.
- Testimonios verificados con autorización para publicar (con foto y nombre).
- Vídeo institucional de 30–60 segundos.
- Tour virtual 360º (existe en el perfil de Bodas.net y se puede enlazar).

---

## 13. Definición de éxito del proyecto

El proyecto se considera **exitoso** cuando:

1. ✅ La landing está en producción accesible en HTTPS bajo el dominio acordado.
2. ✅ El chatbot funciona correctamente y los leads llegan a Airtable.
3. ✅ El cliente recibe notificación de cada lead capturado.
4. ✅ Lighthouse > 90 en las cuatro métricas.
5. ✅ Páginas legales publicadas y conformes a RGPD/LSSI-CE.
6. ✅ El equipo de Finca Los Pinos sabe acceder a Airtable y al panel n8n.
7. ✅ Documentación entregada para mantenimiento futuro.
8. ✅ A 3 meses del lanzamiento: al menos 10 leads cualificados capturados.

---

## 14. Anexos y referencias

### 14.1 Documentos del proyecto
- `RULES.md` — Reglas vinculantes para Antigravity (ya cargado en el IDE).
- `TARIFAS_2027.pdf` — Fuente única de verdad para precios y servicios (en `/creación`).
- `muestralanding` — Diseño de referencia (en `/creación`).

### 14.2 Enlaces externos verificados
- Web oficial actual: https://fincapinos.com/
- Perfil Bodas.net: https://www.bodas.net/fincas/finca-los-pinos--e31134
- Instagram: https://www.instagram.com/finca_los_pinos/
- Facebook: https://www.facebook.com/efincapinos/

### 14.3 Datos de contacto del negocio
- Dirección: Calle Lomo Obrero 21, Firgas, Gran Canaria, Las Palmas (España).
- Teléfono: +34 636 418 627.
- Email: info@fincapinos.com.

### 14.4 Lo que no he podido verificar y queda pendiente
- Razón social y NIF de la entidad titular (placeholder en documentos legales hasta confirmar).
- Si existe DPD designado.
- Volumen actual de consultas mensuales (necesario para validar KPIs).
- Detalles del archivo `muestralanding` (debe analizarlo el agente al iniciar el proyecto).

---

*Documento vivo. Versión 1.0. Actualizar tras cada hito relevante o cambio de alcance.*
