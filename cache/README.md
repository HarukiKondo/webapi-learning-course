# 動かし方

```bash
docker compose up --build
```

以下のようにフロントとバックエンドが両方起動していればOK!

```bash
Attaching to api-1
api-1  |  * Serving Flask app 'app'
api-1  |  * Debug mode: on
api-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
api-1  |  * Running on all addresses (0.0.0.0)
api-1  |  * Running on http://127.0.0.1:8080
api-1  |  * Running on http://172.18.0.2:8080
api-1  | Press CTRL+C to quit
api-1  |  * Restarting with stat
api-1  |  * Debugger is active!
api-1  |  * Debugger PIN: 244-214-685
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:18] "GET / HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:18] "GET /favicon.ico HTTP/1.1" 404 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:31] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 -
api-1  | /api/app.py:18: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
api-1  |   now = datetime.utcnow()
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:33] "GET /cache/no-stale-while-revalidate HTTP/1.1" 200 -
api-1  | /api/app.py:34: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
api-1  |   now = datetime.utcnow()
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:47] "GET /cache/with-stale-while-revalidate HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:01:49] "GET /cache/no-stale-while-revalidate HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:02:19] "GET /cache/no-stale-while-revalidate HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:02:08] "GET /cache/with-stale-while-revalidate HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:02:25] "GET /cache/with-stale-while-revalidate HTTP/1.1" 200 -
api-1  | 172.18.0.1 - - [29/Sep/2025 01:02:37] "GET /cache/no-stale-while-revalidate HTTP/1.1" 200 -
```

