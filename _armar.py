"""
Arma las páginas del sitio de Dale Que Va con el mismo encabezado y pie.
Uso: python3 _armar.py   (GitHub Pages no publica archivos que empiezan con «_»)

Las tarjetas de juegos salen de _juegos.html (generado desde el catálogo de la app).
"""
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))
URL = "https://dalequeva.byfoogles.app"


def pagina(ruta, titulo, descripcion, cuerpo, scripts=""):
    canonica = URL + "/" + (ruta + "/" if ruta else "")
    html = f"""<!DOCTYPE html>
<html lang="es-AR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{titulo}</title>
  <meta name="description" content="{descripcion}">
  <meta name="theme-color" content="#07060d">
  <meta name="rating" content="adult">
  <link rel="canonical" href="{canonica}">
  <link rel="icon" href="/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descripcion}">
  <meta property="og:url" content="{canonica}">
  <meta property="og:image" content="{URL}/img/compartir.jpg">
  <meta property="og:locale" content="es_AR">
  <link rel="preload" href="/fuentes/outfit.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="stylesheet" href="/estilos.css">
</head>
<body>
  <header class="barra">
    <div class="envoltura">
      <a class="marca" href="/"><img src="/img/dalequeva.webp" alt="" width="34" height="34">Dale Que Va</a>
      <nav>
        <a href="/#juegos">Juegos</a>
        <a href="/#hot">Hot</a>
        <a href="/#instalar">Instalar</a>
        <a class="boton chico" data-apk href="#">Descargar</a>
      </nav>
    </div>
  </header>
  <main>
{cuerpo}
  </main>
  <footer>
    <div class="envoltura">
      <div>
        <p><span class="chip18">+18</span> Solo para mayores de 18. Tomá con responsabilidad: nadie está obligado a tomar ni a cumplir una consigna.</p>
        <p style="margin-top:8px">© <span data-anio></span> Dale Que Va · una app de <a href="https://byfoogles.app">ByFoogles</a></p>
      </div>
      <nav>
        <a href="/terminos/">Términos y avisos</a>
        <a href="/privacidad/">Privacidad</a>
        <a href="/comprar/">Comprar Hot</a>
        <a class="arrepentimiento" href="/arrepentimiento/">Botón de arrepentimiento</a>
      </nav>
    </div>
  </footer>
  <script src="/sitio.js"></script>
{scripts}
</body>
</html>
"""
    carpeta = os.path.join(RAIZ, ruta)
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------- Inicio
with open(os.path.join(RAIZ, "_juegos.html"), encoding="utf-8") as f:
    TARJETAS = f.read()

pagina("", "Dale Que Va · Juegos de previa para el celu",
       "24 juegos de previa en una app para Android: Verdad o Reto, Yo Nunca, El Juego del Rey, Ruleta Rusa y más. Sin internet, un solo celu que pasa de mano en mano. +18.",
       f"""    <section class="portada">
      <div class="envoltura">
        <div>
          <p class="etiqueta">Juegos de previa · Android</p>
          <h1 class="logo-neon">DALE<br>QUE VA</h1>
          <p class="lema">24 juegos para la previa en un solo celu que pasa de mano en mano. Cargás los nombres una vez y la app se encarga del resto.</p>
          <div class="acciones">
            <a class="boton" data-apk href="#">Descargar para Android</a>
            <a class="boton contorno cian" href="#juegos">Ver los juegos</a>
          </div>
          <p class="nota"><span class="chip18">+18</span>&nbsp; Gratis con Amigos y Amiguitas · Funciona sin internet · Sin anuncios</p>
        </div>
        <img class="icono-grande" src="/img/dalequeva.webp" alt="Ícono de Dale Que Va" width="340" height="340">
      </div>
    </section>

    <section>
      <div class="envoltura cifras">
        <div class="cifra"><b>24</b><span>juegos</span></div>
        <div class="cifra"><b>3</b><span>niveles de picante</span></div>
        <div class="cifra"><b>0</b><span>internet necesario</span></div>
        <div class="cifra"><b>1</b><span>celu para toda la ronda</span></div>
      </div>
    </section>

    <section id="niveles">
      <div class="envoltura">
        <div class="titulo-seccion">
          <p class="etiqueta">Elegí el clima</p>
          <h2>Tres niveles, la misma ronda</h2>
          <p class="bajada">Cada juego se adapta al grupo: arrancás tranqui y subís cuando la previa lo pide.</p>
        </div>
        <div class="niveles">
          <div class="nivel"><span class="precio-nivel">GRATIS</span><h3>Amigos</h3><p>Para arrancar: tragos, risas, anécdotas y retos para cualquier grupo.</p></div>
          <div class="nivel amiguitas"><span class="precio-nivel">GRATIS</span><h3>Amiguitas</h3><p>Más confianza: chamuyo, confesiones, picos y un poco de roce.</p></div>
          <div class="nivel hot"><span class="precio-nivel">+18 · PAGO</span><h3>Hot</h3><p>Sin filtros: deseos, fantasías, prendas y retos para grupos sin tabúes.</p></div>
        </div>
      </div>
    </section>

    <section id="juegos">
      <div class="envoltura">
        <div class="titulo-seccion">
          <p class="etiqueta">El catálogo</p>
          <h2>24 juegos para toda la noche</h2>
          <p class="bajada">Algunos se juegan en el celu y otros son clásicos de mesa: para esos, la app te da las reglas, los premios y los castigos.</p>
        </div>
        <div class="leyenda">
          <span><i class="punto amigos"></i>Amigos</span>
          <span><i class="punto amiguitas"></i>Amiguitas</span>
          <span><i class="punto hot"></i>Hot</span>
          <span><span class="sin-celu" style="margin:0">SIN CELU</span>se juega en la mesa, la app guía</span>
        </div>
        <div class="juegos">
{TARJETAS}
        </div>
      </div>
    </section>

    <section id="hot">
      <div class="envoltura">
        <div class="caja-hot">
          <p class="etiqueta">Nivel Hot</p>
          <h2>Desbloqueá el Hot para siempre</h2>
          <p class="bajada">Una sola compra por Mercado Pago y el nivel Hot queda abierto en todos los juegos que lo tienen, incluidos Dados del Deseo y Strip Poker.</p>
          <ul>
            <li>Pago único: sin suscripciones ni cobros escondidos.</li>
            <li>Recibís un código al instante y lo activás con un toque.</li>
            <li>Si reinstalás la app, el mismo código te sirve.</li>
          </ul>
          <p class="precio"><span data-precio>…</span> <small>pago único</small></p>
          <div class="fila-botones">
            <a class="boton hot" href="/comprar/">Comprar Hot</a>
          </div>
        </div>
      </div>
    </section>

    <section id="instalar">
      <div class="envoltura">
        <div class="titulo-seccion">
          <p class="etiqueta">Cómo instalarla</p>
          <h2>En un minuto la tenés</h2>
          <p class="bajada">Dale Que Va se descarga desde acá, no desde Play Store. Android te va a pedir permiso para instalarla: es normal con las apps que se bajan de un sitio.</p>
        </div>
        <div class="pasos">
          <div class="paso"><h3>Descargala</h3><p>Tocá «Descargar para Android» desde el celu. Se baja el archivo <b>DaleQueVa.apk</b>.</p></div>
          <div class="paso"><h3>Abrí el archivo</h3><p>Desde la notificación de descarga o desde la carpeta Descargas.</p></div>
          <div class="paso"><h3>Dale permiso</h3><p>Si Android pregunta, activá «Permitir de esta fuente» para tu navegador y volvé atrás.</p></div>
          <div class="paso"><h3>Instalá y jugá</h3><p>Tocá «Instalar», abrila, cargá los nombres de la ronda y elegí un juego.</p></div>
        </div>
      </div>
    </section>

    <section id="preguntas">
      <div class="envoltura">
        <div class="titulo-seccion"><p class="etiqueta">Preguntas</p><h2>Lo que nos suelen preguntar</h2></div>
        <details><summary>¿Es gratis?</summary><p>Sí. Los niveles Amigos y Amiguitas son gratis y sin anuncios. Solo el nivel Hot se paga, una única vez.</p></details>
        <details><summary>¿Necesita internet?</summary><p>No. Todo funciona sin conexión. Solo se usa internet para comprar el Hot.</p></details>
        <details><summary>¿Está en Play Store?</summary><p>Por ahora no: se descarga desde este sitio. Por eso Android pide permiso para instalarla.</p></details>
        <details><summary>¿Hay versión para iPhone?</summary><p>Todavía no. Por ahora es solo para Android.</p></details>
        <details><summary>Compré el Hot y perdí el código</summary><p>Entrá a <a href="/comprar/">Comprar Hot</a> y usá «Ya pagué»: con el número de operación de Mercado Pago lo recuperás.</p></details>
        <details><summary>¿Guardan mis datos?</summary><p>No. La app no tiene cuentas ni manda datos a ningún lado: los nombres de los jugadores quedan solo en tu celu. Más detalles en <a href="/privacidad/">Privacidad</a>.</p></details>
      </div>
    </section>

    <section>
      <div class="envoltura">
        <div class="aviso"><b>Solo para mayores de 18.</b> Todo es voluntario: nadie está obligado a tomar, a cumplir una prenda ni un reto, y cualquiera puede dejar de jugar cuando quiera. Lo que tenga contacto físico, solo si todos los involucrados están de acuerdo. Si vas a manejar, no tomes. <a href="/terminos/">Leer términos y avisos</a>.</div>
      </div>
    </section>""")

# ---------------------------------------------------------------- Comprar
pagina("comprar", "Comprar el nivel Hot · Dale Que Va",
       "Desbloqueá el nivel Hot de Dale Que Va con un pago único por Mercado Pago.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Nivel Hot</p>
        <h1>Desbloqueá el Hot</h1>
        <p>Una sola compra y el nivel Hot queda abierto para siempre en todos los juegos que lo tienen. Al pagar recibís un código que activás con un toque desde el celu.</p>

        <div class="tarjeta hot">
          <p class="precio"><span data-precio>…</span> <small>pago único · Mercado Pago</small></p>
          <label class="casilla"><input type="checkbox" id="mayor"><span>Tengo 18 años o más.</span></label>
          <label class="casilla"><input type="checkbox" id="acepto"><span>Leí y acepto los <a href="/terminos/" target="_blank">términos y avisos</a>.</span></label>
          <div class="fila-botones">
            <button class="boton hot" id="pagar" disabled>Pagar con Mercado Pago</button>
          </div>
          <p class="mensaje error oculto" id="error-pago"></p>
        </div>

        <div class="tarjeta">
          <h2 style="margin-top:0">Ya pagué</h2>
          <p>Si cerraste la página antes de ver tu código o lo perdiste, ingresá el número de operación que figura en el comprobante de Mercado Pago.</p>
          <div class="fila-botones">
            <input class="campo" id="operacion" inputmode="numeric" placeholder="Número de operación" style="flex:1;min-width:200px">
            <button class="boton contorno hot" id="recuperar">Ver mi código</button>
          </div>
          <p class="mensaje error oculto" id="error-recuperar"></p>
        </div>

        <h2>Cómo funciona</h2>
        <ol>
          <li>Pagás con Mercado Pago (tarjeta, dinero en cuenta u otros medios).</li>
          <li>Volvés a esta página y aparece tu código.</li>
          <li>Tocás «Activar en la app» desde el celu, o copiás el código y lo pegás en la app (Ajustes → Ingresar código).</li>
        </ol>
        <p>Antes de comprar, instalá la app desde <a href="/#instalar">la página principal</a>. Si algo falla, usá el <a href="/arrepentimiento/">botón de arrepentimiento</a> dentro de los 10 días.</p>
      </div>
    </section>""",
       """  <script>
    const mayor = document.getElementById("mayor"), acepto = document.getElementById("acepto"), pagar = document.getElementById("pagar");
    const mostrar = (id, texto) => { const e = document.getElementById(id); e.textContent = texto; e.classList.toggle("oculto", !texto); };
    precioListo.then((precio) => {
      const actualizar = () => (pagar.disabled = !(precio && mayor.checked && acepto.checked));
      mayor.onchange = acepto.onchange = actualizar;
      actualizar();
      if (!precio) mostrar("error-pago", "La compra se habilita muy pronto.");
    });
    if (new URLSearchParams(location.search).get("error") === "pago") mostrar("error-pago", "El pago no se completó. Podés intentar de nuevo.");
    pagar.onclick = async () => {
      pagar.disabled = true; mostrar("error-pago", "");
      try {
        const r = await pedir("/preferencia", { method: "POST" });
        if (!r.url) throw new Error(r.error);
        location.href = r.url;
      } catch (e) {
        mostrar("error-pago", e.message || "No pudimos conectar con Mercado Pago. Probá de nuevo.");
        pagar.disabled = false;
      }
    };
    document.getElementById("recuperar").onclick = () => {
      const op = document.getElementById("operacion").value.replace(/\\D/g, "");
      if (!op) return mostrar("error-recuperar", "Ingresá el número de operación.");
      location.href = "/gracias/?payment_id=" + op;
    };
  </script>""")

# ---------------------------------------------------------------- Gracias
pagina("gracias", "Tu código · Dale Que Va",
       "Tu código para desbloquear el nivel Hot de Dale Que Va.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Nivel Hot</p>
        <h1 id="titulo">Buscando tu pago…</h1>
        <div class="tarjeta hot oculto" id="listo">
          <p>¡Gracias por la compra! Este es tu código. Guardalo: te sirve si reinstalás la app.</p>
          <div class="codigo" id="codigo"></div>
          <div class="fila-botones">
            <a class="boton hot" id="activar" href="#">Activar en la app</a>
            <button class="boton contorno hot" id="copiar">Copiar código</button>
          </div>
          <p style="margin-top:16px">«Activar en la app» funciona desde el celu donde tenés Dale Que Va instalada. Si no, copiá el código y pegalo en la app: <b>Ajustes → Ingresar código</b>.</p>
        </div>
        <p class="mensaje error oculto" id="error"></p>
        <p style="margin-top:24px"><a href="/comprar/">Volver a Comprar Hot</a></p>
      </div>
    </section>""",
       """  <script>
    const parametros = new URLSearchParams(location.search);
    const pago = parametros.get("payment_id") || parametros.get("collection_id");
    const titulo = document.getElementById("titulo");
    const error = (texto, tituloTexto = "No pudimos darte el código") => {
      titulo.textContent = tituloTexto;
      const e = document.getElementById("error"); e.textContent = texto; e.classList.remove("oculto");
    };
    (async () => {
      if (!pago || pago === "null") return error("No llegó el número de operación. Si pagaste, buscalo en el comprobante de Mercado Pago y usalo en «Ya pagué».");
      if (!SERVICIO) return error("La compra todavía no está habilitada.");
      try {
        const r = await pedir("/codigo?pago=" + encodeURIComponent(pago));
        if (r.pendiente) return error(r.error, "Tu pago está pendiente");
        if (!r.codigo) return error(r.error || "Probá de nuevo en un rato.");
        titulo.textContent = "¡Hot desbloqueado!";
        document.getElementById("codigo").textContent = r.codigo;
        document.getElementById("activar").href = "dalequeva://activar?c=" + encodeURIComponent(r.codigo);
        document.getElementById("copiar").onclick = async (ev) => {
          await navigator.clipboard.writeText(r.codigo);
          ev.target.textContent = "¡Copiado!";
        };
        document.getElementById("listo").classList.remove("oculto");
      } catch {
        error("No pudimos conectar. Revisá tu internet y recargá la página.");
      }
    })();
  </script>""")

# ---------------------------------------------------------------- Términos
pagina("terminos", "Términos y avisos · Dale Que Va",
       "Términos de uso, avisos legales y condiciones de compra de Dale Que Va.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Legal</p>
        <h1>Términos y avisos</h1>
        <p>Al descargar, instalar o usar Dale Que Va aceptás estos términos. Son los mismos avisos que muestra la app.</p>

        <h2>Solo para mayores de 18</h2>
        <p>Dale Que Va es un juego para adultos: tiene juegos con alcohol y contenido sexual. Al usar la app confirmás que vos y todas las personas que juegan tienen 18 años o más (o la edad legal para tomar alcohol en tu país, si es mayor).</p>

        <h2>Nadie está obligado a nada</h2>
        <p>Participar es voluntario. Cualquiera puede no jugar, pasar una consigna, negarse a una prenda o a un reto, o dejar de jugar en cualquier momento. Las consecuencias que propone el juego (tomar, prendas, castigos) también son opcionales: nadie puede obligar a otra persona a cumplirlas ni presionarla para que lo haga.</p>

        <h2>Consentimiento, siempre</h2>
        <p>Las consignas con besos, contacto físico o quitarse ropa se hacen solo si todas las personas involucradas están de acuerdo, de forma clara y en ese momento. Un «no», un silencio o una duda es un no. Respetá los límites de cada uno: si alguien quiere parar, se para.</p>

        <h2>Alcohol con responsabilidad</h2>
        <p>Tomar es opcional: se puede jugar con agua o bebidas sin alcohol. No tomes si vas a manejar, si estás embarazada, si tomás medicación que no lo permite o si ya tomaste de más. Tomá agua y comé algo.</p>

        <h2>Privacidad</h2>
        <p>No saques fotos ni grabes a nadie sin su permiso, y no compartas lo que pasa en el juego sin el acuerdo de todos. Sobre los datos, ver la <a href="/privacidad/">política de privacidad</a>.</p>

        <h2>Responsabilidad</h2>
        <p>Las consignas son propuestas para divertirse entre adultos. Cada jugador decide qué hace y es responsable de sus actos, y debe respetar las leyes del lugar donde juega. El desarrollador no se responsabiliza por el uso que se haga de la app ni por los daños que resulten de no respetar estos avisos o la ley.</p>

        <h2>Compra del nivel Hot</h2>
        <ul>
          <li>Los niveles Amigos y Amiguitas son gratis. El nivel Hot se desbloquea con un pago único por Mercado Pago, sin suscripción.</li>
          <li>Al aprobarse el pago recibís un código de desbloqueo de uso personal. Si lo perdés, lo recuperás con el número de operación desde <a href="/comprar/">Comprar Hot</a>.</li>
          <li>El pago lo procesa Mercado Pago; nosotros no vemos ni guardamos los datos de tu tarjeta.</li>
          <li>Podés arrepentirte de la compra dentro de los 10 días corridos desde el pago con el <a href="/arrepentimiento/">botón de arrepentimiento</a>, sin dar explicaciones, y te devolvemos el dinero por el mismo medio.</li>
        </ul>

        <h2>Cambios</h2>
        <p>Podemos actualizar la app y estos términos. Si hay cambios importantes, los vas a ver en esta página.</p>
      </div>
    </section>""")

# ---------------------------------------------------------------- Privacidad
pagina("privacidad", "Política de privacidad · Dale Que Va",
       "Qué datos usa Dale Que Va: la app no tiene cuentas ni envía datos; los pagos los procesa Mercado Pago.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Legal</p>
        <h1>Política de privacidad</h1>
        <p>Corta y clara: Dale Que Va está hecha para no saber nada de vos.</p>

        <h2>La app</h2>
        <ul>
          <li>No tiene cuentas, ni registro, ni anuncios, ni herramientas de seguimiento.</li>
          <li>Los nombres de los jugadores, los favoritos y los ajustes se guardan solo en tu celu y no se envían a ningún lado.</li>
          <li>Funciona sin internet. Solo usa la conexión si abrís la página de compra.</li>
          <li>El código de desbloqueo se guarda en tu celu para recordar que compraste el Hot.</li>
        </ul>

        <h2>Este sitio</h2>
        <ul>
          <li>No usa cookies ni herramientas de estadísticas.</li>
          <li>Lo aloja GitHub Pages, que como cualquier servidor puede registrar datos técnicos de las visitas (como la dirección IP) por seguridad.</li>
        </ul>

        <h2>Los pagos</h2>
        <ul>
          <li>Los pagos los procesa Mercado Pago según su propia política de privacidad. Nosotros no vemos ni guardamos los datos de tu tarjeta.</li>
          <li>Para darte el código, nuestro servicio de pagos consulta a Mercado Pago si la operación está aprobada. No guardamos una base de datos de compradores.</li>
          <li>Mercado Pago nos informa los datos de cada venta (por ejemplo, el monto y el correo del comprador), que usamos solo para gestionar la compra, la facturación y los pedidos de arrepentimiento.</li>
        </ul>

        <h2>Tus derechos</h2>
        <p>Podés pedir acceso, rectificación o eliminación de tus datos personales, conforme a la Ley 25.326 de Protección de Datos Personales de Argentina.</p>
      </div>
    </section>""")

# ---------------------------------------------------------------- Arrepentimiento
pagina("arrepentimiento", "Botón de arrepentimiento · Dale Que Va",
       "Arrepentite de tu compra del nivel Hot dentro de los 10 días.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Defensa del consumidor</p>
        <h1>Botón de arrepentimiento</h1>
        <p>Si compraste el nivel Hot, podés arrepentirte dentro de los <b>10 días corridos</b> desde el pago, sin dar explicaciones y sin costo. Te devolvemos el dinero por el mismo medio de pago.</p>

        <div class="tarjeta">
          <h2 style="margin-top:0">Cómo pedirlo</h2>
          <p id="contacto-texto">Escribinos con tu <b>número de operación de Mercado Pago</b> y el correo con el que pagaste. Te respondemos con un código de seguimiento del pedido dentro de las 24 horas.</p>
          <div class="fila-botones">
            <a class="boton hot" id="pedir" href="#">Pedir el arrepentimiento</a>
          </div>
        </div>
        <p style="margin-top:20px">Este botón cumple con la Resolución 424/2020 de la Secretaría de Comercio Interior y el artículo 34 de la Ley 24.240 de Defensa del Consumidor.</p>
      </div>
    </section>""",
       """  <script>
    // Correo para los pedidos de arrepentimiento (completar antes de habilitar la venta).
    const CONTACTO = "";
    const boton = document.getElementById("pedir");
    if (CONTACTO) {
      boton.href = "mailto:" + CONTACTO + "?subject=" + encodeURIComponent("Arrepentimiento de compra · Dale Que Va") +
        "&body=" + encodeURIComponent("Número de operación de Mercado Pago:\\nCorreo con el que pagué:\\n");
    } else {
      boton.classList.add("oculto");
    }
  </script>""")

print("Páginas armadas.")
