# Websocket proxy test

Test rig to see how websockets pass through multiple reverse proxies. Fooling around and finding out.

We'll be using HAProxy and Zeus (aka Pulse Secure Virtual Traffic Manager / aka Ivanti Virtual Traffic Manager) as the reverse proxies in the proxy chain (`client web browser -> haproxy -> zeus -> webserver`).

We'll use `docker comppose` and the internal DNS that docker compose provides to configure the reverse proxies.

## Running

```
docker compose up
```

Then open `websocket.html` in a browser

Code from: https://github.com/dpallot/simple-websocket-server/tree/master

## Tests

Open `websocket.html`

**Endpoint:** ws://localhost:8000/
**Network path:** `haproxy:8000 -> zeus:8080 -> web:8000`

---

**Endpoint:** ws://localhost:8001/
**Network path:** `haproxy:8001 -> web:8000`

---

**Endpoint:** ws://localhost:8080/
**Network path:** `zeus:8080 -> web:8000`
