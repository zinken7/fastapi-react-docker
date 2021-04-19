
## Project Layout

```
000
├─ backend
│  ├─ alembic
│  │  ├─ versions
│  │  ├─ env.py
│  │  └─ script.py.mako
│  ├─ app
│  │  ├─ api
│  │  │  ├─ api_v1
│  │  │  │  ├─ routers
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ auth.py
│  │  │  │  │  └─ users.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ core
│  │  │  ├─ __init__.py
│  │  │  ├─ auth.py
│  │  │  ├─ celery.py
│  │  │  ├─ config.py
│  │  │  └─ security.py
│  │  ├─ crud
│  │  │  ├─ __init__.py
│  │  │  ├─ base.py
│  │  │  └─ user.py
│  │  ├─ db
│  │  │  ├─ __init__.py
│  │  │  ├─ base_class.py
│  │  │  ├─ base.py
│  │  │  ├─ init_db.py
│  │  │  └─ session.py
│  │  ├─ lib
│  │  │  ├─ __init__.py
│  │  │  └─ vi_en.py
│  │  ├─ models
│  │  │  ├─ __init__.py
│  │  │  └─ user.py
│  │  ├─ schemas
│  │  │  ├─ __init__.py
│  │  │  ├─ token.py
│  │  │  └─ user.py
│  │  ├─ __init__.py
│  │  ├─ initial_data.py
│  │  ├─ main.py
│  │  └─ tasks.py
│  ├─ alembic.ini
│  ├─ Dockerfile
│  └─ requirements.txt
├─ frontend
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ src
│  │  ├─ __tests__
│  │  │  ├─ home.test.tsx
│  │  │  └─ login.test.tsx
│  │  ├─ admin
│  │  │  ├─ Users
│  │  │  │  ├─ index.ts
│  │  │  │  ├─ UserCreate.tsx
│  │  │  │  ├─ UserEdit.tsx
│  │  │  │  └─ UserList.tsx
│  │  │  ├─ Admin.tsx
│  │  │  ├─ authProvider.ts
│  │  │  └─ index.ts
│  │  ├─ config
│  │  │  └─ index.tsx
│  │  ├─ utils
│  │  │  ├─ api.ts
│  │  │  ├─ auth.ts
│  │  │  └─ index.ts
│  │  ├─ views
│  │  │  ├─ Home.tsx
│  │  │  ├─ index.ts
│  │  │  ├─ Login.tsx
│  │  │  ├─ PrivateRoute.tsx
│  │  │  ├─ Protected.tsx
│  │  │  └─ SignUp.tsx
│  │  ├─ App.tsx
│  │  ├─ decs.d.ts
│  │  ├─ index.css
│  │  ├─ index.tsx
│  │  ├─ logo.svg
│  │  ├─ react-app-env.d.ts
│  │  └─ Routes.tsx
│  ├─ .dockerignore
│  ├─ .eslintrc.js
│  ├─ .prettierrc.js
│  ├─ Dockerfile
│  ├─ package.json
│  ├─ run.sh
│  └─ tsconfig.json
├─ scripts
│  └─ build.sh
├─ webserver
│  ├─ nginx
│  │  ├─ default.conf
│  │  ├─ myphammuahe.live.conf
│  │  └─ nginx.conf
│  └─ register_ssl.sh
├─ docker-compose.yml
├─ Makefile
└─ README.md
```