"""
Arma las páginas del sitio de Dale Que Va con el mismo encabezado y pie.
Uso: python3 _armar.py   (GitHub Pages no publica archivos que empiezan con «_»)

Las tarjetas de juegos salen de _juegos.html (generado desde el catálogo de la app).
"""
import hashlib
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))
URL = "https://dalequeva.byfoogles.app"


def version(archivo):
    """Huella corta del archivo: cambia la URL cuando cambia el contenido y evita la caché vieja."""
    with open(os.path.join(RAIZ, archivo), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:8]


def pagina(ruta, titulo, descripcion, cuerpo, scripts="", carga=False):
    canonica = URL + "/" + (ruta + "/" if ruta else "")
    pantalla_carga = """  <div class="carga" aria-hidden="true">
    <div class="carga-nombre"><span>D</span><span>A</span><span>L</span><span>E</span><br><span>Q</span><span>U</span><span>E</span> <span>V</span><span>A</span></div>
    <div class="carga-pie"><span>Juegos de previa · +18</span><span class="carga-numero">000</span></div>
  </div>
""" if carga else ""
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
  <link rel="preload" href="/fuentes/unbounded.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fuentes/anton.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/estilos.css?v={version('estilos.css')}">
</head>
<body class="cargando">
{pantalla_carga}  <div class="cursor" aria-hidden="true"></div>
  <header class="barra">
    <div class="barra-izq">
      <a class="volver" href="https://byfoogles.app" aria-label="Volver a ByFoogles">
        <span class="volver-flecha" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        <span class="volver-texto">ByFoogles</span>
      </a>
      <a class="marca" href="/"><img src="/img/dalequeva.webp" alt="" width="32" height="32">Dale Que Va</a>
    </div>
    <nav>
      <a href="/#juegos"><i></i>Juegos</a>
      <a href="/#hot">Hot</a>
      <a href="/#instalar">Instalar</a>
    </nav>
    <div class="barra-der">
      <span class="reloj">Hora de previa <span id="hora">--:--</span></span>
      <a class="boton chico" data-apk href="#">Descargar</a>
    </div>
  </header>
  <main>
{cuerpo}
  </main>
  <footer>
    <div class="pie-gigante" aria-hidden="true">DALE QUE VA</div>
    <div class="pie-fila">
      <div>
        <p><span class="chip18">+18</span>&nbsp; Solo para mayores de 18. Tomá con responsabilidad: nadie está obligado a tomar ni a cumplir una consigna.</p>
        <p style="margin-top:8px">© <span data-anio></span> Dale Que Va · una app de <a href="https://byfoogles.app">ByFoogles</a></p>
      </div>
      <nav>
        <a href="/terminos/">Términos y avisos</a>
        <a href="/privacidad/">Privacidad</a>
        <a href="/comprar/">Comprar</a>
        <a class="arrepentimiento" href="/arrepentimiento/">Botón de arrepentimiento</a>
      </nav>
    </div>
  </footer>
  <script src="/sitio.js?v={version('sitio.js')}"></script>
  <script src="/animaciones.js?v={version('animaciones.js')}"></script>
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
      <canvas id="aurora" aria-hidden="true"></canvas>
      <div class="estrellas" aria-hidden="true"></div>
      <div class="grano" aria-hidden="true"></div>

      <div class="portada-contenido">
        <p class="etiqueta">Juegos de previa · Android · <span class="chip18">+18</span></p>
        <h1 class="logo-neon parpadeo" data-partir="150"><span class="linea">DALE</span><span class="linea">QUE VA</span></h1>
        <p class="lema">24 juegos para la previa en un solo celu que pasa de mano en mano. Cargás los nombres una vez y la app se encarga del resto.</p>
        <div class="acciones">
          <a class="boton" data-apk href="#">Descargar para Android <span>↓</span></a>
          <a class="boton contorno cian" href="#juegos">Ver los juegos</a>
        </div>
      </div>

      <aside class="datos-der" aria-hidden="true">
        <p><small>Juegos</small> 24</p>
        <p><small>Internet</small> No hace falta</p>
        <p class="separado"><small>Una app de</small><b>ByFoogles</b></p>
        <img class="icono-flotante" src="/img/dalequeva.webp" alt="" width="150" height="150">
      </aside>

      <div class="lateral" aria-hidden="true">Deslizá para entrar a la previa</div>

      <div class="tira">
        <span class="tira-nivel" style="--c: var(--cian)"><i></i><span>Amigos<br><small>Gratis</small></span></span>
        <span class="tira-nivel" style="--c: var(--violeta)"><i></i><span>Amiguitas<br><small>Pago único</small></span></span>
        <span class="tira-nivel" style="--c: var(--hot)"><i></i><span>Hot<br><small>Pack completo</small></span></span>
        <span class="tira-dato"><b>0</b> anuncios</span>
        <span class="tira-dato" style="margin-left:0"><b>1</b> celu para todos</span>
      </div>
    </section>

    <section class="escena-sec">
      <div class="reparto" aria-hidden="true"><span>Verdad o Reto</span><span>Yo Nunca</span><span>Juego del Rey</span><span>Ruleta Rusa</span></div>
      <div class="escena">
        <h2 class="titulo-gigante" aria-label="La previa"><span class="parte izq">LA</span><span class="parte der">PREVIA</span></h2>
        <div class="escena-icono"><div class="halo"></div><img src="/img/dalequeva.webp" alt="Ícono de Dale Que Va" width="400" height="400"></div>
        <span class="anio">[+18]</span>
        <a class="sello" data-apk href="#" aria-label="Descargar Dale Que Va">
          <svg viewBox="0 0 120 120" aria-hidden="true">
            <defs><path id="circulo" d="M60,60 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
            <text><textPath href="#circulo">DESCARGAR • GRATIS • ANDROID • +18 •</textPath></text>
          </svg>
          <b>↓</b>
        </a>
      </div>
      <div class="escena-pie">
        <div class="revelar">
          <p class="sobre rojo">● Cómo funciona</p>
          <p>Un solo celu que pasa de mano en mano. Elegís el juego y el nivel, y la app arma las rondas con los nombres de todos: quién pregunta, quién responde, quién toma.</p>
        </div>
        <div class="circulos revelar">
          <div class="circulo blanco"><small>Juegos</small><b>24</b></div>
          <div class="circulo rojo"><small>Edad</small><b>+18</b></div>
          <div class="circulo cian"><small>Niveles</small><b>3</b></div>
        </div>
        <blockquote class="cita revelar">“Arrancá tranqui, entrá en confianza y terminá sin filtros.”</blockquote>
      </div>
      <div class="cinta" aria-hidden="true"><div class="cinta-pista"><span>😈 Verdad o Reto</span><span>🙊 Yo Nunca Nunca</span><span>🤴 El Juego del Rey</span><span>🔫 Ruleta Rusa</span><span>🍾 La Botellita</span><span>⚔️ Versus</span><span>🎲 El Viaje Prohibido</span><span>⚖️ ¿Qué Preferís?</span><span>👑 Mazo del Rey Criollo</span><span>🍺 Vaso Lleno</span><span>🃏 Blackjack Criollo</span><span>♠️ Poker</span><span>😈 Verdad o Reto</span><span>🙊 Yo Nunca Nunca</span><span>🤴 El Juego del Rey</span><span>🔫 Ruleta Rusa</span><span>🍾 La Botellita</span><span>⚔️ Versus</span><span>🎲 El Viaje Prohibido</span><span>⚖️ ¿Qué Preferís?</span><span>👑 Mazo del Rey Criollo</span><span>🍺 Vaso Lleno</span><span>🃏 Blackjack Criollo</span><span>♠️ Poker</span></div></div>
    </section>

    <section class="bloque" id="niveles">
      <div class="envoltura">
        <div class="titulo-seccion">
          <p class="etiqueta">● Elegí el clima</p>
          <h2 data-partir>Tres niveles, <em>una ronda</em></h2>
          <p class="bajada revelar">Cada juego se adapta al grupo: arrancás tranqui y subís cuando la previa lo pide.</p>
        </div>
        <div class="niveles">
          <div class="nivel revelar"><span class="num">01</span><span class="precio-nivel">GRATIS</span><h3>Amigos</h3><p>Para arrancar: tragos, risas, anécdotas y retos para cualquier grupo.</p></div>
          <div class="nivel amiguitas revelar"><span class="num">02</span><span class="precio-nivel">PAGO ÚNICO</span><h3>Amiguitas</h3><p>Más confianza: chamuyo, confesiones, picos y un poco de roce.</p></div>
          <div class="nivel hot revelar"><span class="num">03</span><span class="precio-nivel">+18 · PACK COMPLETO</span><h3>Hot</h3><p>Sin filtros: deseos, fantasías, prendas y retos para grupos sin tabúes.</p></div>
        </div>
      </div>
    </section>

    <section class="bloque" id="juegos" style="padding-top:20px">
      <div class="envoltura">
        <div class="titulo-seccion">
          <p class="etiqueta">● El catálogo</p>
          <h2 data-partir>24 juegos para <em>toda la noche</em></h2>
          <p class="bajada revelar">Algunos se juegan en el celu y otros son clásicos de mesa: para esos, la app te da las reglas, los premios y los castigos.</p>
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

    <section class="bloque hot-sec" id="hot">
      <div class="hot-fondo" aria-hidden="true">HOT</div>
      <div class="envoltura">
        <div class="caja-hot amiguitas revelar">
          <div>
            <p class="sobre violeta">● Solo Amiguitas · sin Hot</p>
            <h2>¿Arrancan tranqui? Abrí Amiguitas</h2>
            <p class="bajada">Para el grupo que ya entró en confianza pero todavía no se anima al Hot: chamuyo, confesiones, picos y un poco de roce, en todos los juegos que lo tienen.</p>
            <ul>
              <li>Pago único, más barato que el pack.</li>
              <li>Recibís un código al instante y lo activás con un toque.</li>
              <li>¿Después se calienta la previa? El pack completo trae Amiguitas y Hot.</li>
            </ul>
          </div>
          <div class="lado">
            <div class="candado" aria-hidden="true">
              <svg viewBox="0 0 120 150">
                <path class="candado-arco" d="M36 74 V48 a24 24 0 0 1 48 0 V74"/>
                <rect class="candado-cuerpo" x="16" y="70" width="88" height="70" rx="18"/>
                <circle class="candado-ojo" cx="60" cy="100" r="8"/>
                <rect class="candado-ojo" x="56" y="102" width="8" height="18" rx="4"/>
              </svg>
              <i class="chispa" style="--x:-58px;--y:-40px"></i><i class="chispa" style="--x:56px;--y:-50px"></i><i class="chispa" style="--x:-50px;--y:30px"></i><i class="chispa" style="--x:60px;--y:22px"></i><i class="chispa" style="--x:0px;--y:-70px"></i>
            </div>
            <p class="precio"><span data-precio="amiguitas">…</span><small>solo Amiguitas · pago único</small></p>
            <div class="fila-botones" style="justify-content:center">
              <a class="boton violeta" href="/comprar/?producto=amiguitas">Comprar Amiguitas <span>↗</span></a>
            </div>
          </div>
        </div>

        <div class="caja-hot revelar">
          <div>
            <p class="sobre rojo">● Pack completo · Amiguitas + Hot · +18</p>
            <h2>Desbloqueá todo para siempre</h2>
            <p class="bajada">Amigos es gratis. Con una sola compra por Mercado Pago abrís Amiguitas y Hot en todos los juegos que los tienen, incluidos Dados del Deseo y Strip Poker.</p>
            <ul>
              <li>Pago único: sin suscripciones ni cobros escondidos.</li>
              <li>El mejor precio: Amiguitas y Hot juntos.</li>
              <li>Recibís un código al instante y lo activás con un toque.</li>
              <li>Si reinstalás la app, el mismo código te sirve.</li>
            </ul>
          </div>
          <div class="lado">
            <div class="candado" aria-hidden="true">
              <svg viewBox="0 0 120 150">
                <path class="candado-arco" d="M36 74 V48 a24 24 0 0 1 48 0 V74"/>
                <rect class="candado-cuerpo" x="16" y="70" width="88" height="70" rx="18"/>
                <circle class="candado-ojo" cx="60" cy="100" r="8"/>
                <rect class="candado-ojo" x="56" y="102" width="8" height="18" rx="4"/>
              </svg>
              <i class="chispa" style="--x:-58px;--y:-40px"></i><i class="chispa" style="--x:56px;--y:-50px"></i><i class="chispa" style="--x:-50px;--y:30px"></i><i class="chispa" style="--x:60px;--y:22px"></i><i class="chispa" style="--x:0px;--y:-70px"></i>
            </div>
            <p class="precio"><span data-precio="pack">…</span><small>pack completo · pago único</small></p>
            <div class="fila-botones" style="justify-content:center">
              <a class="boton hot" href="/comprar/?producto=pack">Comprar el pack <span>↗</span></a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="cinta hot" aria-hidden="true"><div class="cinta-pista"><span>🔥 Dados del Deseo</span><span>♠️ Strip Poker</span><span>😈 Retos sin filtro</span><span>🙊 Confesiones +18</span><span>🍾 Botellita Hot</span><span>🤴 El Rey sin piedad</span><span>🎲 Viaje Prohibido Hot</span><span>⚔️ Versus Hot</span><span>🔥 Dados del Deseo</span><span>♠️ Strip Poker</span><span>😈 Retos sin filtro</span><span>🙊 Confesiones +18</span><span>🍾 Botellita Hot</span><span>🤴 El Rey sin piedad</span><span>🎲 Viaje Prohibido Hot</span><span>⚔️ Versus Hot</span></div></div>

    <section class="bloque clara" id="instalar">
      <div class="envoltura">
        <p class="etiqueta">● Cómo instalarla</p>
        <div class="gigante-claro" style="margin-top:20px">
          <span data-partir>Instalala</span><small>en</small><span data-partir="200">1 minuto</span>
        </div>
        <p class="revelar" style="margin-top:28px;max-width:640px;color:rgba(7,6,13,.65)">Dale Que Va se descarga desde acá, no desde Play Store. Android te va a pedir permiso para instalarla: es normal con las apps que se bajan de un sitio.</p>
        <div class="pasos">
          <div class="paso revelar"><h3>Descargala</h3><p>Tocá «Descargar para Android» desde el celu. Se baja el archivo <b>DaleQueVa.apk</b>.</p></div>
          <div class="paso revelar"><h3>Abrí el archivo</h3><p>Desde la notificación de descarga o desde la carpeta Descargas.</p></div>
          <div class="paso revelar"><h3>Dale permiso</h3><p>Si Android pregunta, activá «Permitir de esta fuente» para tu navegador y volvé atrás.</p></div>
          <div class="paso revelar"><h3>Jugá</h3><p>Tocá «Instalar», abrila, cargá los nombres de la ronda y elegí un juego.</p></div>
        </div>
        <div class="acciones">
          <a class="boton" data-apk href="#">Descargar para Android <span>↓</span></a>
        </div>
      </div>
    </section>

    <section class="bloque" id="preguntas">
      <div class="envoltura preguntas-grilla">
        <div class="titulo-seccion"><p class="etiqueta">● Preguntas</p><h2 data-partir>Lo que nos <em>suelen preguntar</em></h2></div>
        <div>
          <details><summary>¿Es gratis?</summary><p>El nivel Amigos es gratis, sin anuncios, en todos los juegos. Amiguitas y Hot se desbloquean con un pago único: Amiguitas sola, o el pack completo con los dos.</p></details>
          <details><summary>¿Necesita internet?</summary><p>No. Todo funciona sin conexión. Solo se usa internet para comprar.</p></details>
          <details><summary>¿Está en Play Store?</summary><p>Por ahora no: se descarga desde este sitio. Por eso Android pide permiso para instalarla.</p></details>
          <details><summary>¿Hay versión para iPhone?</summary><p>Todavía no. Por ahora es solo para Android.</p></details>
          <details><summary>Compré y perdí el código</summary><p>Entrá a <a href="/comprar/">Comprar</a> y usá «Ya pagué»: con el número de operación de Mercado Pago lo recuperás.</p></details>
          <details><summary>¿Guardan mis datos?</summary><p>No. La app no tiene cuentas ni manda datos a ningún lado: los nombres de los jugadores quedan solo en tu celu. Más detalles en <a href="/privacidad/">Privacidad</a>.</p></details>
        </div>
      </div>
      <div class="envoltura" style="margin-top:50px">
        <div class="aviso revelar"><b>Solo para mayores de 18.</b> Todo es voluntario: nadie está obligado a tomar, a cumplir una prenda ni un reto, y cualquiera puede dejar de jugar cuando quiera. Lo que tenga contacto físico, solo si todos los involucrados están de acuerdo. Si vas a manejar, no tomes. <a href="/terminos/">Leer términos y avisos</a>.</div>
      </div>
    </section>""", carga=True)

# ---------------------------------------------------------------- Comprar
pagina("comprar", "Comprar · Dale Que Va",
       "Desbloqueá Amiguitas o el pack completo (Amiguitas + Hot) de Dale Que Va con un pago único por Mercado Pago.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Comprar</p>
        <h1 data-partir>Desbloqueá la previa</h1>
        <p>Amigos es gratis. Elegí qué querés abrir: es una sola compra y queda para siempre en todos los juegos. Al pagar recibís un código que activás con un toque desde el celu.</p>

        <div class="productos" role="radiogroup" aria-label="Qué querés comprar">
          <label class="producto amiguitas">
            <input type="radio" name="producto" value="amiguitas">
            <span class="producto-nombre">Amiguitas</span>
            <span class="producto-precio" data-precio="amiguitas">…</span>
            <span class="producto-detalle">Más confianza: chamuyo, confesiones, picos y un poco de roce.</span>
          </label>
          <label class="producto hot">
            <input type="radio" name="producto" value="pack" checked>
            <span class="producto-sello">Recomendado</span>
            <span class="producto-nombre">Pack completo</span>
            <span class="producto-precio" data-precio="pack">…</span>
            <span class="producto-detalle">Amiguitas + Hot (+18): deseos, fantasías, Dados del Deseo y Strip Poker.</span>
          </label>
        </div>

        <div class="tarjeta hot">
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
          <li>Elegís Amiguitas o el pack completo y pagás con Mercado Pago (tarjeta, dinero en cuenta u otros medios).</li>
          <li>Volvés a esta página y aparece tu código.</li>
          <li>Tocás «Activar en la app» desde el celu, o copiás el código y lo pegás en la app (Ajustes → Ingresar código).</li>
        </ol>
        <p>Antes de comprar, instalá la app desde <a href="/#instalar">la página principal</a>. Si algo falla, usá el <a href="/arrepentimiento/">botón de arrepentimiento</a> dentro de los 10 días.</p>
      </div>
    </section>""",
       """  <script>
    const mayor = document.getElementById("mayor"), acepto = document.getElementById("acepto"), pagar = document.getElementById("pagar");
    const opciones = [...document.querySelectorAll('input[name="producto"]')];
    const mostrar = (id, texto) => { const e = document.getElementById(id); e.textContent = texto; e.classList.toggle("oculto", !texto); };
    const pedido = new URLSearchParams(location.search).get("producto");
    opciones.forEach((o) => (o.checked = o.value === (pedido === "amiguitas" ? "amiguitas" : "pack")));
    const elegido = () => opciones.find((o) => o.checked).value;
    precioListo.then((precios) => {
      const actualizar = () => {
        pagar.disabled = !(precios && mayor.checked && acepto.checked);
        pagar.textContent = precios ? `Pagar ${pesos(precios[elegido()])} con Mercado Pago` : "Pagar con Mercado Pago";
      };
      mayor.onchange = acepto.onchange = actualizar;
      opciones.forEach((o) => (o.onchange = actualizar));
      actualizar();
      if (!precios) mostrar("error-pago", "La compra se habilita muy pronto.");
    });
    if (new URLSearchParams(location.search).get("error") === "pago") mostrar("error-pago", "El pago no se completó. Podés intentar de nuevo.");
    pagar.onclick = async () => {
      pagar.disabled = true; mostrar("error-pago", "");
      try {
        const r = await pedir("/orden", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ producto: elegido() }) });
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
       "Tu código para desbloquear tu compra en Dale Que Va.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Tu compra</p>
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
        <p style="margin-top:24px"><a href="/comprar/">Volver a Comprar</a></p>
      </div>
    </section>""",
       """  <script>
    const parametros = new URLSearchParams(location.search);
    const pago = parametros.get("order_id") || parametros.get("payment_id") || parametros.get("collection_id");
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
        titulo.textContent = r.producto === "amiguitas" ? "¡Amiguitas desbloqueado!" : "¡Pack completo desbloqueado!";
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
        <h1 data-partir>Términos y avisos</h1>
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

        <h2>Compras</h2>
        <ul>
          <li>El nivel Amigos es gratis. El nivel Amiguitas y el pack completo (Amiguitas + Hot) se desbloquean con un pago único por Mercado Pago, sin suscripción.</li>
          <li>Al aprobarse el pago recibís un código de desbloqueo de uso personal. Si lo perdés, lo recuperás con el número de operación desde <a href="/comprar/">Comprar</a>.</li>
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
        <h1 data-partir>Política de privacidad</h1>
        <p>Corta y clara: Dale Que Va está hecha para no saber nada de vos.</p>

        <h2>La app</h2>
        <ul>
          <li>No tiene cuentas, ni registro, ni anuncios, ni herramientas de seguimiento.</li>
          <li>Los nombres de los jugadores, los favoritos y los ajustes se guardan solo en tu celu y no se envían a ningún lado.</li>
          <li>Funciona sin internet. Solo usa la conexión si abrís la página de compra.</li>
          <li>El código de desbloqueo se guarda en tu celu para recordar lo que compraste.</li>
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
       "Arrepentite de tu compra en Dale Que Va dentro de los 10 días.",
       """    <section class="pagina">
      <div class="envoltura">
        <p class="etiqueta">Defensa del consumidor</p>
        <h1 data-partir>Botón de arrepentimiento</h1>
        <p>Si compraste Amiguitas o el pack completo, podés arrepentirte dentro de los <b>10 días corridos</b> desde el pago, sin dar explicaciones y sin costo. Te devolvemos el dinero por el mismo medio de pago.</p>

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
