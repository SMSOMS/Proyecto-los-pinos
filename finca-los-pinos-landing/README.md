# Finca Los Pinos — Landing Page & Chatbot

Este proyecto comprende la landing page de captación independiente y el widget de chatbot integrado para la **Finca Los Pinos**, un espacio exclusivo de bodas y eventos en Firgas (Gran Canaria, España) con capacidad para hasta 300 invitados.

El desarrollo está basado en **Astro 6** (generación estática) y **Tailwind CSS v4** para asegurar un rendimiento de Lighthouse > 90 en todos los apartados, diseño responsive mobile-first y una experiencia de usuario sumamente fluida.

---

## 🚀 Estructura del Proyecto

```text
finca-los-pinos-landing/
├── public/                # Archivos estáticos (imágenes extraídas, favicon, robots, sitemap)
├── src/
│   ├── components/        # Componentes Astro modulares (Hero, Pricing, FAQ, etc.)
│   │   └── Chatbot/       # Widget del Chatbot (ChatbotWidget.astro)
│   ├── layouts/           # Plantillas base (BaseLayout.astro con Schema JSON-LD)
│   ├── pages/             # Páginas del sitio (Index y Páginas Legales obligatorias)
│   └── styles/            # Hoja de estilos global de Tailwind v4
├── .env.example           # Plantilla de variables de entorno de configuración
├── package.json           # Dependencias y scripts del proyecto
└── README.md              # Este manual de integración y despliegue
```

---

## 🛠️ Configuración Local e Instalación

1. **Instalar dependencias**:
   ```bash
   npm install
   ```

2. **Configurar variables de entorno**:
   Copia el archivo `.env.example` como `.env` y rellena las variables:
   ```bash
   cp .env.example .env
   ```

3. **Iniciar servidor de desarrollo**:
   ```bash
   npm run dev
   ```
   El portal estará accesible en `http://localhost:4321/`.

4. **Compilar para producción**:
   ```bash
   npm run build
   ```
   El output estático listo para servir se generará en el directorio `dist/`.

---

## 📋 Variables de Entorno

El frontend interactúa con el webhook externo de n8n para la lógica de conversación y captura de leads. Las siguientes variables son obligatorias en tiempo de compilación (llevan el prefijo `PUBLIC_` para ser accesibles en el cliente de Astro):

- `PUBLIC_CHATBOT_WEBHOOK_URL`: Dirección completa del webhook de producción en tu VPS de n8n (ej. `https://n8n.tudominio.com/webhook/chatbot`).
- `PUBLIC_CHATBOT_TOKEN`: Token secreto compartido que se envía en las cabeceras (`X-Chatbot-Token`) para que n8n valide el origen legítimo de las peticiones.

---

## 🗄️ CRM de Leads (Airtable Schema)

Para que el backend funcione correctamente, debes crear una tabla en Airtable denominada **`Leads`** con la siguiente estructura exacta de columnas:

| Nombre de Columna | Tipo de Campo Airtable | Descripción / Uso |
| :--- | :--- | :--- |
| `ID` | Autonumber | Identificador secuencial único de la consulta |
| `Nombre` | Single line text | Nombre completo del usuario |
| `Email` | Email | Correo electrónico de contacto validado |
| `Telefono` | Phone | Número telefónico de contacto |
| `Fecha Tentativa` | Date | Fecha estimada del evento (formato AAAA-MM-DD) |
| `Invitados` | Number | Número aproximado de invitados al evento |
| `Consentimiento` | Checkbox | Estado de aceptación de la política de privacidad |
| `Consentimiento_TS` | Date (with time) | Marca de tiempo exacta del envío del consentimiento |
| `SessionID` | Single line text | UUID para rastrear la sesión del chat |
| `Origen` | Single line text | Identificador del portal originario (ej. `finca_pinos_landing`) |

---

## 🤖 Integración del Chatbot con n8n

El widget de chatbot realiza peticiones HTTP POST asíncronas al webhook de n8n. Espera recibir respuestas estructuradas en JSON.

### 1. Flujo de Mensajería General (LLM)
- **Carga de Envío (POST)**:
  ```json
  {
    "sessionId": "uuid-de-sesion",
    "message": "Mensaje escrito por el usuario",
    "history": [
      { "sender": "bot", "text": "¡Hola!..." },
      { "sender": "user", "text": "Hola, ¿tenéis precios?" }
    ]
  }
  ```
- **Respuesta esperada de n8n**:
  ```json
  {
    "reply": "Respuesta en HTML básico del bot resolviendo la duda...",
    "suggestedActions": ["Ver tarifas", "Servicios incluidos", "Hablar con alguien"]
  }
  ```

### 2. Flujo de Captura de Lead
Cuando n8n detecta que el usuario tiene intención de reservar o visitar la finca, responde con la bandera `captureLeadStep` en `true`:
- **Respuesta de n8n**:
  ```json
  {
    "reply": "Perfecto, para agendar una visita o darte disponibilidad detallada, ¿puedes dejarme tus datos?",
    "captureLeadStep": true
  }
  ```
El frontend despliega inmediatamente el formulario modal del lead. Al enviarse, realiza un POST con los datos del formulario:
- **Carga de Envío (POST)**:
  ```json
  {
    "sessionId": "uuid-de-sesion",
    "type": "lead_capture",
    "leadData": {
      "name": "Nombre Usuario",
      "email": "user@email.com",
      "phone": "600000000",
      "date": "2027-09-18",
      "guests": "150",
      "consentTimestamp": "2026-05-27T21:30:00Z"
    }
  }
  ```
- **Lógica de n8n al recibir el Lead**:
  1. Valida el origen (`Origin` header) y el token secreto (`X-Chatbot-Token`).
  2. Inserta el registro en la tabla `Leads` de Airtable (almacenando el timestamp de consentimiento y la IP del remitente).
  3. Envía un correo electrónico transaccional de confirmación de recepción al usuario (vía Brevo, Postmark o similar).
  4. Envía una alerta inmediata al comercial (vía Telegram Bot, Slack webhook o Email de aviso).

---

## 🚀 Despliegue en Easypanel (VPS Hostinger)

Dado que la landing se compila a un sitio puramente estático (`output: 'static'` en Astro), el despliegue es sumamente sencillo en Easypanel:

1. **Crear una nueva aplicación estática** en el panel de Easypanel.
2. **Vincular el repositorio Git** (GitHub/GitLab) donde se aloja el proyecto.
3. En la sección de configuración de Easypanel:
   - Configura el comando de construcción (*Build Command*): `npm install && npm run build`
   - Configura el directorio de publicación (*Publish Directory*): `dist`
4. **Variables de entorno**: Agrega las variables `PUBLIC_CHATBOT_WEBHOOK_URL` y `PUBLIC_CHATBOT_TOKEN` en la pestaña de variables de entorno de la aplicación en Easypanel para que se inyecten durante el build de Astro.
5. **Dominio**: Vincula el dominio definitivo (ej. `bodas.fincapinos.com` o similar). Traefik/Easypanel gestionará automáticamente la emisión y renovación del certificado SSL con Let's Encrypt de forma transparente.

---

## 📝 Registro de Cambios (8 de Junio de 2026)

Hoy se han realizado varias correcciones críticas para dejar el proyecto listo para producción a falta de vincular el dominio definitivo:

1. **Corrección de Variables de Entorno en Compilación Docker (Easypanel)**:
   - Modificado el `Dockerfile` de producción para declarar explícitamente los argumentos de compilación (`ARG`) para Astro: `PUBLIC_CHATBOT_WEBHOOK_URL` y `PUBLIC_CHATBOT_TOKEN`.
   - Mapeados estos argumentos a variables de entorno (`ENV`) para que estén disponibles durante la fase `RUN npm run build` de Docker en la compilación remota.
   - *Nota de configuración*: Estas variables deben estar definidas en la sección **Environment** del servicio de la landing page en Easypanel para que se inyecten en el despliegue.

2. **Resolución de Variables en Plantillas de Correo (n8n)**:
   - Se ha corregido la sintaxis de variables en los nodos de envío de correos (**Send Confirmation Email** y **Notify Sales Team**) en el flujo de n8n.
   - Cambiado el uso de template literals de JavaScript (\` y `${}`) por la sintaxis estándar de expresiones de n8n con doble llave (`{{ ... }}`).
   - El flujo remoto ya está actualizado, guardado y activado. Las confirmaciones de leads ahora envían datos reales.

3. **Adaptabilidad del Chatbot en Móviles**:
   - Corregido un descuadre en dispositivos móviles donde el panel de chat se recortaba a la izquierda debido al uso de `w-full` junto con un desplazamiento fijo a la derecha (`right-6`).
   - Actualizado el contenedor a `left-4 right-4 bottom-4` en móviles para centrarlo con márgenes de 16px, y configurada la transición adaptativa a `sm:left-auto sm:right-6 sm:bottom-6 sm:w-[360px]` en pantallas de escritorio.

---

## 📌 Próximos Pasos / Tareas Pendientes

- **Vincular el Dominio Definitivo**: Configurar el dominio final de producción en Easypanel (ej. `bodas.fincapinos.com` o subdominio similar) y apuntar los registros DNS correspondientes para habilitar el SSL automático de Let's Encrypt de forma transparente.

