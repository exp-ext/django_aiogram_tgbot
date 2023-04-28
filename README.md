<h2>Django Aiogram tgbot</h2>

<p>Template for developing Telegram bot on Django with Aiogram on ASGI server.</p

![статус](https://github.com/exp-ext/django_aiogram_tgbot/actions/workflows/backend.yml/badge.svg?event=push)

<p align="center">
<img src="https://github.com/exp-ext/django_aiogram_tgbot/blob/main/backend/static/img/top-banner.jpg?raw=true" width="1200">
</p>
<hr />
<h3>Technology Stack</h3>
<ul>
<li>Python</li>
<li>Django</li>
<li>Aiogram</li>
<li>PostgreSQL</li>
<li>Docker</li>
<li>Github Actions</li>
</ul>

<hr />
<h3>Dependencies</h3>
<ul>
<li>Listed in the file backend/requirements.txt</li>
</ul>

<hr />
<h3>Development</h3>
<ul>
<li>Clone the repository to your server;</li>


```bash
$ git clone https://github.com/exp-ext/django_aiogram_tgbot.git
```

<li>Create the file `/infra/.env`. The template for filling the file is in /infra/.env.example;</li>
<li>When running without certificates, use docker-compose with the DEBUG=1 parameter in .env. This gives nginx a certificate-free configuration;</li>

<li>docker-compose-debug.yml is made to run the project in DEBUG mode with the ability to change the code without restarting the containers;</li>

```bash
$ docker compose -f docker-compose-debug.yml up --build
```

</ul>

<hr />
<h3>Deployment on a server with a certificate</h3>
<ul>
<li>Install docker and docker-compose-plugin on the server;</li>
<li>Clone the repository to your server;</li>
<li>Create the file `/infra/.env`;</li>
<li>Get certificates in Let's Encrypt by running the script</li>

```bash
$ sudo ./init-letsencrypt.sh
```

<li>Run the command `docker compose up -d -build`;</li>
<br /><br />
</ul>
<hr />

GITHUB: [exp-ext](https://github.com/exp-ext)

[![Join Telegram](https://img.shields.io/badge/My%20Telegram-Join-blue)](https://t.me/Borokin)
