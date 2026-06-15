const REALM = "Hilel Calculator";

function getEnv(name) {
  if (globalThis.Netlify && globalThis.Netlify.env) {
    return globalThis.Netlify.env.get(name) || "";
  }

  if (globalThis.Deno && globalThis.Deno.env) {
    return globalThis.Deno.env.get(name) || "";
  }

  return "";
}

function unauthorized() {
  return new Response("Authentication required.", {
    status: 401,
    headers: {
      "WWW-Authenticate": `Basic realm="${REALM}"`,
      "Cache-Control": "no-store",
    },
  });
}

function parseBasicAuth(request) {
  const header = request.headers.get("authorization") || "";
  const [scheme, encoded] = header.split(" ");

  if (scheme !== "Basic" || !encoded) {
    return null;
  }

  try {
    const decoded = atob(encoded);
    const separatorIndex = decoded.indexOf(":");

    if (separatorIndex === -1) {
      return null;
    }

    return {
      username: decoded.slice(0, separatorIndex),
      password: decoded.slice(separatorIndex + 1),
    };
  } catch {
    return null;
  }
}

async function sha256Hex(value) {
  const bytes = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", bytes);

  return Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

function constantTimeEqual(a, b) {
  if (a.length !== b.length) {
    return false;
  }

  let mismatch = 0;
  for (let index = 0; index < a.length; index += 1) {
    mismatch |= a.charCodeAt(index) ^ b.charCodeAt(index);
  }

  return mismatch === 0;
}

export default async (request, context) => {
  const expectedUser = getEnv("CALCULATOR_AUTH_USER");
  const expectedHash = getEnv("CALCULATOR_AUTH_PASSWORD_HASH");
  const salt = getEnv("CALCULATOR_AUTH_PASSWORD_SALT");

  if (!expectedUser || !expectedHash || !salt) {
    return new Response("Calculator authentication is not configured.", {
      status: 503,
      headers: {
        "Cache-Control": "no-store",
      },
    });
  }

  const credentials = parseBasicAuth(request);

  if (!credentials || credentials.username !== expectedUser) {
    return unauthorized();
  }

  const passwordHash = await sha256Hex(`${salt}:${credentials.password}`);

  if (!constantTimeEqual(passwordHash, expectedHash)) {
    return unauthorized();
  }

  // Authenticated: serve the page but prevent shared/proxy caches from storing
  // the protected content.
  const response = await context.next();
  response.headers.set("Cache-Control", "private, no-store");
  return response;
};
