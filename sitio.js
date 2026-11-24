// Configuración del sitio de Dale Que Va.
// SERVICIO: dirección del servicio de pagos (Cloudflare Worker). Vacío = la venta todavía no está habilitada.
// Modo prueba escondido: entrar con ?prueba=1 activa la venta solo en ese navegador (?prueba=0 la apaga).
// Sirve para probar con las credenciales de prueba de Mercado Pago sin abrir la venta al público.
const SERVICIO_PRUEBA = "https://dalequeva-pagos.dalequeva-pagos.workers.dev";
const modoPrueba = (() => {
  const p = new URLSearchParams(location.search).get("prueba");
  try {
    if (p === "1") localStorage.setItem("dqv-prueba", "1");
    if (p === "0") localStorage.removeItem("dqv-prueba");
    return localStorage.getItem("dqv-prueba") === "1";
  } catch { return false; }
})();
const SERVICIO = modoPrueba ? SERVICIO_PRUEBA : "";
if (modoPrueba) {
  const aviso = document.createElement("a");
  aviso.className = "aviso-prueba";
  aviso.href = "?prueba=0";
  aviso.textContent = "Modo prueba · pagos ficticios · tocá para salir";
  document.body.append(aviso);
}
const APK = "https://github.com/Fooglesarg/Dale-Que-Va-Sitio/releases/latest/download/DaleQueVa.apk";

const pesos = (n) => new Intl.NumberFormat("es-AR", { style: "currency", currency: "ARS", maximumFractionDigits: 0 }).format(n);

async function pedir(ruta, opciones) {
  const r = await fetch(SERVICIO + ruta, opciones);
  const datos = await r.json().catch(() => ({}));
  return { estado: r.status, ...datos };
}

// Precios por producto: { amiguitas, pack }. Cada lugar con data-precio="amiguitas|pack" muestra el suyo.
async function cargarPrecio() {
  const lugares = document.querySelectorAll("[data-precio]");
  const pendiente = () => lugares.forEach((e) => (e.textContent = "Muy pronto"));
  if (!SERVICIO) { pendiente(); return null; }
  try {
    const { precios } = await pedir("/precio");
    if (!precios || !precios.pack) throw new Error();
    lugares.forEach((e) => (e.textContent = pesos(precios[e.dataset.precio || "pack"])));
    return precios;
  } catch {
    pendiente();
    return null;
  }
}

document.querySelectorAll("[data-apk]").forEach((a) => (a.href = APK));
document.querySelectorAll("[data-anio]").forEach((e) => (e.textContent = new Date().getFullYear()));
const precioListo = cargarPrecio();
