# JupyterHubLab


### Для того, чтобы развернуть Hub:
1. Собрать образы
```bash
docker-compose build
```
2. Запустить следующую команду в директории с *docker-compose.yml*
```bash
docker-compose up -d
```

Завершать работу JupyterHub следует через веб-интерфейс admin панели. (Shutdown Hub)

![alt text](https://github.com/Ohlomonchick/JupyterHubLab/blob/main/shutdown.png?raw=true)

Не рекомендуется использовать **docker-compose down** для завершения работы. 
Если вы все же воспользовались этой командой и испытывайте трудности с повторным запуском, 
исправьте это, корректно остановив все контейнеры командой:
```
docker-compose down --remove-orphans
```

## Об организации Hub

Docker-compose соберёт два образа:
один для контейнера самого hub и proxy, контролирующего отдельных пользователей;
второй - для контейнеров отдельных пользователей. 

Данные каждого пользователя хранятся в отдельном volume jupyterhub-user-{username}.
Также есть volume jupyterhub-shared, где хранятся ноутбуки, которыми пользователи делятся с
другими участниками Hub.
*(в корневой директории пользователя совершён mount на этот volume в качестве папки /shared)*

### Структура папок
```bash
./
├── docker-compose.yml
│
├── jupiterlab
│   └── Dockerfile
│
└── jupyterhub
    ├── Dockerfile
    └── jupyterhub_config.py
```

### Аунтификация
Для контроля аунтификации был выбран [FirstUseAuthenticator](https://github.com/jupyterhub/firstuseauthenticator).
При первом вводе логина и пароля будет создан аккаунт с такими данными.
При этом права администратора есть только у пользователя c именем admin.

### Дополнительная возможность
Можно загрузить ноутбуки в Hub при его сборке из определённой папки. По умолчанию это папка */notebooks*
Изменить эту папку можно аргументом **NOTEBOOKS_FROM** в *docker-compose.yml*, учтите,
что путь должен быть прописан относительно папки, в которой лежит *docker-compose.yml*.
Можно также изменить целевую папку загрузки аргументом **HUB_PATH**.

Параметр **DOCKER_NOTEBOOK_DIR** отвечает за директорию, в которой могут работать пользователи.