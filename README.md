<!-- ====================== HEADER ====================== -->
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1f3a5f,100:2563a8&height=200&section=header&text=Denis%20Drobyshev&fontColor=ffffff&fontSize=46&fontAlignY=34&desc=Backend%20Developer%20%C2%B7%20Python%20%C2%B7%20Django%20%2F%20FastAPI&descSize=18&descAlignY=56" alt="header"/>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3200&pause=900&color=2563A8&center=true&vCenter=true&width=640&lines=Backend+Developer+%C2%B7+Python%2C+Django%2C+FastAPI;I+design%2C+build+and+deploy+web+systems;Machine+Learning+%26+Computer+Vision;Open+to+work" alt="typing"/>
</a>

<br/>

<a href="mailto:drobishev.denis@icloud.com"><img src="https://img.shields.io/badge/Email-drobishev.denis%40icloud.com-2563a8?style=for-the-badge&logo=maildotru&logoColor=white"/></a>
<a href="https://t.me/multiheadselfattention"><img src="https://img.shields.io/badge/Telegram-%40multiheadselfattention-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/></a>
<a href="https://github.com/DenisDrobyshev"><img src="https://img.shields.io/badge/GitHub-DenisDrobyshev-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://denisdrobyshev.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-Website-6366f1?style=for-the-badge&logo=githubpages&logoColor=white"/></a>
<a href="https://career.habr.com/denisdrobyshev"><img src="https://img.shields.io/badge/Habr%20Career-Профиль-65A3BE?style=for-the-badge&logo=habr&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Moscow-1f3a5f?style=for-the-badge&logo=googlemaps&logoColor=white"/>
<img src="https://img.shields.io/badge/Open%20to%20Work-2ea44f?style=for-the-badge&logo=statuspage&logoColor=white"/>

</div>

---

## About

Backend developer working mainly in **Python** with **Django** and **FastAPI**. I take a project the whole way: database design, server logic, API, interface, Docker, and deployment to a real server. I am not the kind of developer who leaves a project "working on my laptop". My thesis portal, my schedule service and my student portal all ended up running on university infrastructure, used by real people.

Alongside web development I build **Machine Learning** and **Computer Vision** projects: real time detection on video with YOLO, image classifiers, and a geospatial analysis pipeline.

I am looking for my first full time role as a **Junior Backend / Python Developer**, and I can start immediately.

- **Core stack:** Python, Django, FastAPI, PostgreSQL, SQL, Docker, Nginx, Gunicorn, Linux, Git
- **Also work with:** Go (internal services), JavaScript, React, Vue
- **ML / CV:** PyTorch, TensorFlow, scikit-learn, OpenCV, YOLO
- **Based in:** Moscow, open to remote or hybrid

---

## Experience

**Software Developer / DevOps**, IT Department (DIT), MIIGAiK · `2026`
> Systems development and support group, production internship
- Deployed a Django portal on the university's internal infrastructure: PostgreSQL, Gunicorn behind Nginx, static and media file serving.
- Configured single sign-on with the university corporate account over OpenID Connect.
- Moved the project from dev to production: secret management, debug mode, allowed hosts, and system email.
- Loaded real journal issues into the archive and verified metadata export to XML.

**Backend / Web Developer**, university systems, MIIGAiK · `2023-2024`
> Practical work on internal services during my studies
- Built a **class schedule web service**. Wrote a large, complex SQL query that assembled the timetable from several related tables, and integrated it into the university's internal **Go (Golang)** backend services.
- Developed the **student personal account portal**: schedule, grade book, profile and university news, with a responsive interface ([miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk)).
- Worked inside an existing internal infrastructure: reading other people's code, matching conventions, and shipping changes that had to fit the rest of the system.

---

## Featured projects

**GiA: Academic journal portal**  ·  `thesis, deployed`  ·  🔒 private, demo on request
A full web portal for the journal *Izvestia Vuzov. Geodesy and Aerophotography*, with issue archive management. Designed, built and deployed by me on university infrastructure.
- Auto-generated **admin panel** for the editorial team: issues, articles, inline forms, with a business rule that only one issue can be current at a time.
- Corporate **SSO / OpenID Connect**, personal account, role based access.
- **Security**: protection against CSRF, XSS and SQL injection, plus secret management.
- **XML metadata export** for bibliographic indexing, and tests at several levels.
- `Python · Django · PostgreSQL · Docker · Nginx · Gunicorn · OIDC`

**[approval-service](https://github.com/DenisDrobyshev/approval-service): content approval backend**
- Production style REST service where content moves through a **state machine**, with a full **audit log** and a **transactional outbox** for reliable event delivery.
- **Idempotency-Key** support, per-workspace **multi-tenant isolation**, scope based header auth, and secret redaction in logs.
- `Python · FastAPI · async SQLAlchemy 2.0 · Alembic · PostgreSQL · Docker · pytest`

**[decisionrl](https://github.com/DenisDrobyshev/decisionrl): reinforcement learning for operational decisions**
- RL for operational decisions (pricing, inventory, energy, queues, supply chains). Each environment ships with its classical operations-research baseline; verified over multiple seeds, the learned policy beats the strong baseline on five tasks and matches the exact dynamic-programming optimum where one exists. Benchmarked head-to-head against Stable-Baselines3 (PPO parity on CartPole).
- Written from scratch: 31 algorithms (DQN family, PPO, SAC, TD3, TRPO, offline, model-based, multi-agent, meta-RL) on PyTorch, 20 environments (8 applied), a unified `predict / learn / save / load` API, a CLI, and Gymnasium registration.
- 385 tests, 86% coverage, typed (mypy), CI on Python 3.9 to 3.12, published on PyPI (`pip install decisionrl`), with a [documentation site](https://denisdrobyshev.github.io/decisionrl/).
- `Python · PyTorch · NumPy · Gymnasium · MkDocs · GitHub Actions`

**[Detector_app](https://github.com/DenisDrobyshev/Detector_app): real time detection on video**
- Streamlit app that finds events in the frame live: **YOLO** for detection, **InsightFace** for face recognition.
- Works with a webcam and video files, produces CSV reports and statistics.
- `Python · YOLO · InsightFace · OpenCV · Streamlit`

**[Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis): location choice from geodata**
- A pipeline that suggests where to open a fitness center: OpenStreetMap data, an **H3** hex grid, an attractiveness model in **scikit-learn**, and interactive maps.
- `Python · scikit-learn · H3 · OSMnx · geopandas`

**[classification_animals](https://github.com/DenisDrobyshev/classification_animals): image classifier**
- Compared three architectures (dense, simple CNN, VGG style). Best model reached **F1 0.88**. Served inference through FastAPI with a Streamlit interface.
- `Python · TensorFlow/Keras · CNN · FastAPI · Streamlit`

<details>
<summary><b>More projects</b></summary>

<br/>

- [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter): FastAPI service that turns Excel files into validated database tables (auth, configurable templates, web UI).
- [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store): e-commerce on React (React Router, Context API, cart, wishlist).
- [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis): UAV stability analysis (Runge-Kutta, eigenvalues, GUI).
- [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch): recognizes a function from a hand drawn graph, exports formulas to text, LaTeX and Excel.
- [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app): geodetic coordinate transformation service (7-parameter Helmert), FastAPI + Streamlit.
- [universum](https://github.com/DenisDrobyshev/universum): neural network and ML coursework from my final year.
- [CIFAR10](https://github.com/DenisDrobyshev/CIFAR10) · [veloshop](https://github.com/DenisDrobyshev/veloshop) (Vue/Nuxt) · [ToDoshka](https://github.com/DenisDrobyshev/ToDoshka) (Flutter).

</details>

---

## Tech stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vue](https://img.shields.io/badge/Vue-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)

</div>

---

## Education

**B.Sc., Applied Informatics (09.03.03)**, MIIGAiK · `2022-2026`
Moscow State University of Geodesy and Cartography, Faculty of Geoinformatics and Information Security.

---

## GitHub

<div align="center">

[![Public repos](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FDenisDrobyshev&query=%24.public_repos&label=Public%20repos&style=for-the-badge&logo=github&labelColor=1f3a5f&color=2563a8)](https://github.com/DenisDrobyshev?tab=repositories)
[![Followers](https://img.shields.io/github/followers/DenisDrobyshev?style=for-the-badge&logo=github&label=Followers&labelColor=1f3a5f&color=2563a8)](https://github.com/DenisDrobyshev)

</div>

---

<div align="center">

### Open to work. Feel free to reach out

<a href="mailto:drobishev.denis@icloud.com"><img src="https://img.shields.io/badge/Email-2563a8?style=for-the-badge&logo=maildotru&logoColor=white"/></a>
<a href="https://t.me/multiheadselfattention"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/></a>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2563a8,100:1f3a5f&height=110&section=footer"/>

</div>
