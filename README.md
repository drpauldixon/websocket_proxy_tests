# Websocket proxy test

Test rig to see how websockets pass through multiple reverse proxies. Fooling around and finding out.

**Websocket code taken from:** https://github.com/dpallot/simple-websocket-server/tree/master

We'll be using HAProxy and Zeus (aka Pulse Secure Virtual Traffic Manager / aka Ivanti Virtual Traffic Manager) as the reverse proxies in the proxy chain (`client web browser -> haproxy -> zeus -> webserver`).

We'll use `docker compose` and the internal DNS that docker compose provides to configure the reverse proxies.

## Running

```
docker compose up
```

Then use a web browser to open the file **websocket.html** in this repo.

**Zeus admin interface:** https://localhost:9090 - user: admin, password: admin

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
