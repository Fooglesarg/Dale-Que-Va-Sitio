// Configuración del sitio de Dale Que Va.
// SERVICIO: dirección del servicio de pagos (Cloudflare Worker). Vacío = la venta todavía no está habilitada.
const SERVICIO = "";
const APK = "https://github.com/Fooglesarg/Dale-Que-Va-Sitio/releases/latest/download/DaleQueVa.apk";

const pesos = (n) => new Intl.NumberFormat("es-AR", { style: "currency", currency: "ARS", maximumFractionDigits: 0 }).format(n);

async function pedir(ruta, opciones) {
  const r = await fetch(SERVICIO + ruta, opciones);
  const datos = await r.json().catch(() => ({}));
  return { estado: r.status, ...datos };
}

async function cargarPrecio() {
  const lugares = document.querySelectorAll("[data-precio]");
  if (!lugares.length) return null;
  if (!SERVICIO) {
    lugares.forEach((e) => (e.textContent = "Muy pronto"));
    return null;
  }
  try {
    const { precio } = await pedir("/precio");
    if (!precio) throw new Error();
    lugares.forEach((e) => (e.textContent = pesos(precio)));
    return precio;
  } catch {
    lugares.forEach((e) => (e.textContent = "Muy pronto"));
    return null;
  }
}

document.querySelectorAll("[data-apk]").forEach((a) => (a.href = APK));
document.querySelectorAll("[data-anio]").forEach((e) => (e.textContent = new Date().getFullYear()));
const precioListo = cargarPrecio();
