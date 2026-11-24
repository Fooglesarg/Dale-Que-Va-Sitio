// Dale Que Va · animaciones del sitio (cada parte se activa solo si la página tiene lo necesario)
const reducido = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ------------------------------------------------ Partir textos en letras */
function partir(elemento, retrasoBase = 0) {
  let i = 0;
  const recorrer = (nodo) => {
    [...nodo.childNodes].forEach((hijo) => {
      if (hijo.nodeType === Node.TEXT_NODE) {
        if (!hijo.textContent.trim()) return hijo.remove();
        // Cada palabra va en un bloque que no se corta, y adentro cada letra se anima sola.
        const fragmento = document.createDocumentFragment();
        hijo.textContent.replace(/\s+/g, " ").split(/( )/).forEach((parte) => {
          if (!parte) return;
          if (parte === " ") return fragmento.appendChild(document.createTextNode(" "));
          const palabra = document.createElement("span");
          palabra.className = "palabra";
          [...parte].forEach((caracter) => {
            const span = document.createElement("span");
            span.className = "letra";
            span.textContent = caracter;
            span.style.setProperty("--i", i++);
            span.style.setProperty("--d", retrasoBase + "ms");
            palabra.appendChild(span);
          });
          fragmento.appendChild(palabra);
        });
        hijo.replaceWith(fragmento);
      } else if (hijo.nodeType === Node.ELEMENT_NODE) {
        recorrer(hijo);
      }
    });
  };
  elemento.setAttribute("aria-label", elemento.textContent.replace(/\s+/g, " ").trim());
  recorrer(elemento);
}
document.querySelectorAll("[data-partir]").forEach((e) => partir(e, +(e.dataset.partir || 0)));

/* ------------------------------------------------ Pantalla de carga (solo inicio) */
(function carga() {
  const pantalla = document.querySelector(".carga");
  if (!pantalla) return document.body.classList.remove("cargando");
  const letras = [...pantalla.querySelectorAll(".carga-nombre span")];
  const numero = pantalla.querySelector(".carga-numero");
  const terminar = () => document.body.classList.remove("cargando");
  if (reducido || sessionStorage.getItem("visto")) {
    letras.forEach((l) => l.classList.add("on"));
    return setTimeout(terminar, reducido ? 0 : 250);
  }
  sessionStorage.setItem("visto", "1");
  // Como en la app: cada letra parpadea y queda prendida.
  letras.map((l) => [l, Math.random()]).sort((a, b) => a[1] - b[1]).forEach(([l], k) => {
    const base = 100 + k * 110;
    [0, 60, 130, 210].forEach((t, j) => setTimeout(() => l.classList.toggle("on", j % 2 === 0 || j === 3), base + t));
  });
  const inicio = performance.now(), duracion = 1600;
  (function contar(ahora) {
    const p = Math.min(1, (ahora - inicio) / duracion);
    numero.textContent = String(Math.round(p * 100)).padStart(3, "0");
    if (p < 1) requestAnimationFrame(contar); else setTimeout(terminar, 220);
  })(inicio);
})();

/* ------------------------------------------------ Aurora (WebGL) */
(function aurora() {
  const lienzo = document.getElementById("aurora");
  if (!lienzo) return;
  const gl = lienzo.getContext("webgl", { antialias: false, alpha: false, powerPreference: "low-power" });
  if (!gl) return;
  const vertice = `attribute vec2 p; void main(){ gl_Position = vec4(p, 0., 1.); }`;
  const fragmento = `
    precision mediump float;
    uniform vec2 r; uniform float t; uniform vec2 m;
    float h(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float n(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.-2.*f);
      return mix(mix(h(i), h(i+vec2(1,0)), f.x), mix(h(i+vec2(0,1)), h(i+vec2(1,1)), f.x), f.y); }
    float fbm(vec2 p){ float v = 0., a = .5; for (int i = 0; i < 5; i++){ v += a * n(p); p = p * 2.03 + 3.1; a *= .5; } return v; }
    void main(){
      vec2 uv = gl_FragCoord.xy / r; vec2 p = uv; p.x *= r.x / r.y;
      vec2 q = p * 1.5 + (m - .5) * .35;
      float tt = t * .05;
      float a = fbm(q + vec2(tt, -tt * .6));
      float b = fbm(q * 1.3 + a * 1.8 + vec2(-tt * .7, tt));
      float c = fbm(q * .7 + b * 1.2 + tt * .3);
      vec3 negro = vec3(.03, .02, .05);
      vec3 vino = vec3(.45, .05, .32);
      vec3 magenta = vec3(1., .18, .77);
      vec3 hot = vec3(1., .23, .36);
      vec3 cian = vec3(.13, .9, 1.);
      vec3 col = mix(negro, vino, smoothstep(.25, .85, b));
      col = mix(col, magenta, smoothstep(.55, .95, c) * .85);
      col = mix(col, hot, smoothstep(.62, .95, a) * .35);
      col = mix(col, cian, smoothstep(.65, .98, a * b * 1.9) * .5);
      float d = distance(uv, m); col += magenta * .2 * exp(-d * d * 9.);
      col *= smoothstep(1.25, .25, distance(uv, vec2(.65, .45)));
      gl_FragColor = vec4(col, 1.);
    }`;
  const compilar = (tipo, codigo) => { const s = gl.createShader(tipo); gl.shaderSource(s, codigo); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, compilar(gl.VERTEX_SHADER, vertice));
  gl.attachShader(prog, compilar(gl.FRAGMENT_SHADER, fragmento));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;
  gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const ubic = gl.getAttribLocation(prog, "p");
  gl.enableVertexAttribArray(ubic);
  gl.vertexAttribPointer(ubic, 2, gl.FLOAT, false, 0, 0);
  const uR = gl.getUniformLocation(prog, "r"), uT = gl.getUniformLocation(prog, "t"), uM = gl.getUniformLocation(prog, "m");
  const ajustar = () => {
    lienzo.width = Math.max(1, Math.round(lienzo.clientWidth * .5));
    lienzo.height = Math.max(1, Math.round(lienzo.clientHeight * .5));
    gl.viewport(0, 0, lienzo.width, lienzo.height);
  };
  ajustar();
  addEventListener("resize", ajustar);
  let mx = .65, my = .5, ox = mx, oy = my, enPantalla = true;
  addEventListener("pointermove", (e) => { mx = e.clientX / innerWidth; my = 1 - e.clientY / innerHeight; });
  new IntersectionObserver(([e]) => (enPantalla = e.isIntersecting)).observe(lienzo);
  const inicio = performance.now();
  (function cuadro(ahora) {
    if (enPantalla) {
      ox += (mx - ox) * .04; oy += (my - oy) * .04;
      gl.uniform2f(uR, lienzo.width, lienzo.height);
      gl.uniform1f(uT, reducido ? 20 : (ahora - inicio) / 1000);
      gl.uniform2f(uM, ox, oy);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    if (!reducido) requestAnimationFrame(cuadro);
  })(inicio);
})();

/* ------------------------------------------------ Cursor */
(function cursor() {
  const c = document.querySelector(".cursor");
  if (!c || matchMedia("(hover: none)").matches) return;
  let x = -100, y = -100, cx = x, cy = y;
  addEventListener("pointermove", (e) => { x = e.clientX; y = e.clientY; });
  document.addEventListener("pointerover", (e) => c.classList.toggle("grande", !!e.target.closest("a, button, summary, label")));
  (function mover() {
    cx += (x - cx) * .2; cy += (y - cy) * .2;
    c.style.left = cx + "px"; c.style.top = cy + "px";
    requestAnimationFrame(mover);
  })();
})();

/* ------------------------------------------------ Reloj de la previa */
(function reloj() {
  const e = document.getElementById("hora");
  if (!e) return;
  const f = new Intl.DateTimeFormat("es-AR", { hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false, timeZone: "America/Argentina/Buenos_Aires" });
  const poner = () => (e.textContent = f.format(new Date()));
  poner(); setInterval(poner, 1000);
})();

/* ------------------------------------------------ Revelar al entrar en pantalla */
document.querySelectorAll(".juegos .juego").forEach((j, k) => j.style.setProperty("--n", k % 4));
const observador = new IntersectionObserver((entradas) => {
  entradas.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("visible"); observador.unobserve(e.target); } });
}, { threshold: .15 });
document.querySelectorAll(".revelar, .juego, [data-partir]:not(.portada [data-partir])").forEach((e) => observador.observe(e));

/* Luz que sigue al mouse en las tarjetas de juegos */
document.querySelectorAll(".juego").forEach((j) => j.addEventListener("pointermove", (e) => {
  const r = j.getBoundingClientRect();
  j.style.setProperty("--mx", `${e.clientX - r.left}px`);
  j.style.setProperty("--my", `${e.clientY - r.top}px`);
}));

/* ------------------------------------------------ Efectos atados al scroll */
(function scroll() {
  const barra = document.querySelector(".barra");
  const portada = document.querySelector(".portada-contenido");
  const izq = document.querySelector(".titulo-gigante .izq");
  const der = document.querySelector(".titulo-gigante .der");
  const icono = document.querySelector(".escena-icono");
  const escena = document.querySelector(".escena");
  const hotFondo = document.querySelector(".hot-fondo");
  const claras = [...document.querySelectorAll(".clara")];
  let pendiente = false;
  const actualizar = () => {
    pendiente = false;
    const y = scrollY, alto = innerHeight;
    barra.classList.toggle("solida", y > 40);
    barra.classList.toggle("clara", claras.some((s) => { const r = s.getBoundingClientRect(); return r.top < 36 && r.bottom > 36; }));
    if (reducido) return;
    if (portada) {
      portada.style.transform = `translate3d(0, ${y * -0.25}px, 0)`;
      portada.style.opacity = String(Math.max(0, 1 - y / (alto * .8)));
    }
    if (escena) {
      const r = escena.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, 1 - (r.top + r.height / 2) / alto));
      const abrir = (p - .5) * 2 * (innerWidth < 760 ? .35 : 1);
      izq.style.transform = `translate3d(${abrir * -6}vw, 0, 0)`;
      der.style.transform = `translate3d(${abrir * 6}vw, 0, 0)`;
      icono.style.setProperty("--sube", `${(0.5 - p) * 120}px`);
      icono.style.setProperty("--giro", `${(0.5 - p) * -16}deg`);
    }
    if (hotFondo) {
      const r = hotFondo.parentElement.getBoundingClientRect();
      hotFondo.style.transform = `translate3d(${(r.top / alto) * 12}vw, 0, 0)`;
    }
  };
  addEventListener("scroll", () => { if (!pendiente) { pendiente = true; requestAnimationFrame(actualizar); } }, { passive: true });
  addEventListener("resize", actualizar);
  actualizar();
})();

/* ------------------------------------------------ Candado: en celus (sin mouse) se abre al aparecer */
(function candado() {
  const c = document.querySelector(".candado");
  if (!c || matchMedia("(hover: hover)").matches) return;
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting) setTimeout(() => c.classList.add("abierto"), 500);
    else c.classList.remove("abierto");
  }, { threshold: 0.8 }).observe(c);
})();
