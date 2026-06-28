<!-- ====================== HEADER ====================== -->
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6a11cb,100:2575fc&height=200&section=header&text=Denis%20Drobyshev&fontColor=ffffff&fontSize=46&fontAlignY=34&desc=Backend%20%C2%B7%20Python%20%C2%B7%20Machine%20Learning%20Engineer&descSize=18&descAlignY=56" alt="header"/>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=900&color=2575FC&center=true&vCenter=true&width=640&lines=Python+%7C+Django+%7C+FastAPI+%7C+PyTorch;Backend+%E2%80%A2+Computer+Vision+%E2%80%A2+ML;I+ship+real+products%2C+not+just+notebooks;Open+to+work+%E2%80%94+let's+build+something" alt="typing"/>
</a>

<br/>

<a href="mailto:drobishev.denis@icloud.com"><img src="https://img.shields.io/badge/Email-drobishev.denis%40icloud.com-D44638?style=for-the-badge&logo=maildotru&logoColor=white"/></a>
<a href="https://t.me/multiheadselfattention"><img src="https://img.shields.io/badge/Telegram-%40multiheadselfattention-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/></a>
<a href="https://github.com/DenisDrobyshev"><img src="https://img.shields.io/badge/GitHub-DenisDrobyshev-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Moscow-2575FC?style=for-the-badge&logo=googlemaps&logoColor=white"/>
<img src="https://img.shields.io/badge/Open%20to%20Work-Yes-2ea44f?style=for-the-badge&logo=statuspage&logoColor=white"/>

</div>

---

## 👋 Привет, я Денис

Выпускник **МИИГАиК** по направлению **09.03.03 «Прикладная информатика»**. Backend-инженер на **Python / Django / FastAPI**, строю **ML / Computer Vision** решения, делаю фронт на **React / Vue** и мобильные приложения на **Flutter**.

Я довожу проект до **рабочего, задеплоенного продукта**: модель/логика → база → API → интерфейс → Docker → сервер. Не «ноутбук ради ноутбука» — а система, которой пользуются. Свой дипломный портал я **сам развернул в продакшн-инфраструктуре вуза** во время преддипломной практики.

- 🎯 **Ищу:** **Junior Backend / Python / ML Engineer**
- 🧩 **Стек ядра:** Python, Django, FastAPI, PostgreSQL, Docker, Nginx, Gunicorn
- 🧠 **Углубляю:** PyTorch, продакшн-инференс, проектирование API, AGI-направление
- 🌍 **Формат:** Москва / удалёнка / гибрид
- ⚡ **Кредо:** от идеи до деплоя — своими руками

---

## 💼 Опыт

**Дирекция информационных технологий (ДИТ) МИИГАиК** — *Разработчик / DevOps (преддипломная производственная практика)* · 2026
> Группа разработки и сопровождения автоматизированных систем и сервисов
- Самостоятельно развернул Django-портал в внутренней инфраструктуре вуза: **PostgreSQL**, сервер приложений **Gunicorn**, обратный прокси **Nginx**, раздача статики и медиа.
- Настроил **единый вход (SSO) через OpenID Connect** с корпоративной учётной записью МИИГАиК.
- Перенёс проект в продакшн-конфигурацию (секреты, режим отладки, разрешённые хосты), настроил системные письма, наполнил электронный архив реальными выпусками, проверил выгрузку метаданных в **XML**.

---

## 🚀 Избранные проекты

> Это не туториалы — это рабочие системы с моделями, API, базой и деплоем.

### 📰 GiA — Информационный портал научного журнала · *диплом + внедрение*  `🔒 приватный, демо по запросу`
Полноценный веб-портал журнала **«Известия вузов. Геодезия и аэрофотосъёмка»** с управлением архивами выпусков — спроектирован, разработан и **развёрнут в инфраструктуре вуза**.
- **Django** + **PostgreSQL** + **Docker / docker-compose**, деплой через **Nginx + Gunicorn**
- Автогенерируемая **админ-панель** для редакции: выпуски, статьи, inline-формы, группы полей; бизнес-инвариант «не более одного текущего выпуска»
- **SSO / OpenID Connect**, личный кабинет, ролевая модель доступа
- **Информационная безопасность**: защита от CSRF / XSS / SQL-инъекций, управление секретами
- **Выгрузка метаданных в XML** для библиографического индексирования
- Полноценное **тестирование** (модульное, интеграционное, функциональное, нефункциональное) по пирамиде тестов
- `Python · Django · PostgreSQL · Docker · Nginx · Gunicorn · OIDC`

### 🎥 [Detector_app](https://github.com/DenisDrobyshev/Detector_app) — Мониторинг по видеопотоку
Веб-приложение на **Streamlit** для детекции событий на занятиях в реальном времени.
- **YOLO (Ultralytics)** — детекция нарушений на кадре; **InsightFace** — распознавание лиц и привязка к человеку
- Работа с веб-камерой и видео (MP4/AVI/MOV/MKV), CSV-отчёты и статистика
- `Python · Computer Vision · YOLO · InsightFace · Streamlit`

### 🗺️ [Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis) — Геомаркетинговая ML-аналитика
Пайплайн: **где открыть фитнес-центр** при максимуме потенциала и минимуме конкуренции.
- Открытые геоданные через **OpenStreetMap / OSMnx**, гексагональная сетка **H3**
- Модель привлекательности локаций (**scikit-learn**) + интерактивные карты **Leafmap**
- `Python · Geospatial ML · H3 · scikit-learn · OSM`

### 🐾 [classification_animals](https://github.com/DenisDrobyshev/classification_animals) — Классификатор изображений
Сравнение архитектур (Dense / SimpleCNN / VGG-like) с деплоем.
- Лучшая модель **VGGCNN — F1 0.88** (Dense 0.70 → SimpleCNN 0.87 → VGGCNN 0.88)
- Деплой: **Streamlit** UI + **FastAPI** инференс-API
- `Python · TensorFlow/Keras · CNN · Streamlit · FastAPI`

### 🗃️ [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter) — Excel → база данных
Бэкенд на **FastAPI**: превращение Excel-файлов в структурированные таблицы БД.
- Авторизация, настраиваемые шаблоны таблиц, валидация данных по типам и правилам
- Веб-интерфейс просмотра/редактирования записей
- `Python · FastAPI · Uvicorn · HTML/JS`

<details>
<summary><b>➕ Ещё проекты</b></summary>

<br/>

- 🐉 [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store) — e-commerce на **React** (React Router, Context API, корзина, избранное).
- 🛩️ [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis) — анализ устойчивости БПЛА (Рунге-Кутта, собственные числа, GUI).
- 📊 [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch) — распознавание функции по нарисованному графику, экспорт в текст/LaTeX/Excel.
- ⚙️ [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app) — связка Streamlit + FastAPI.
- 🎓 [miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk) — личный кабинет студента МИИГАиК (HTML/CSS/JS).
- 🧠 [universum](https://github.com/DenisDrobyshev/universum) — практические работы по нейросетям и ML за выпускной семестр.
- 🖼️ [CIFAR10](https://github.com/DenisDrobyshev/CIFAR10) · 🚲 [veloshop](https://github.com/DenisDrobyshev/veloshop) (Vue/Nuxt) · ✅ [ToDoshka](https://github.com/DenisDrobyshev/ToDoshka) (Flutter).

</details>

---

## 🛠️ Стек

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vue](https://img.shields.io/badge/Vue-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

</div>

---

## 📈 GitHub статистика

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=DenisDrobyshev&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&theme=tokyonight" alt="stats"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=DenisDrobyshev&layout=compact&langs_count=8&hide_border=true&theme=tokyonight" alt="top langs"/>

<br/>

<img src="https://github-readme-streak-stats.demolab.com?user=DenisDrobyshev&hide_border=true&theme=tokyonight" alt="streak"/>

<br/>

<img src="https://github-profile-trophy.vercel.app/?username=DenisDrobyshev&theme=tokyonight&no-frame=true&column=7&margin-w=8" alt="trophies"/>

</div>

---

<div align="center">

### 💬 Готов выйти на проект и приносить пользу с первого дня

<a href="mailto:drobishev.denis@icloud.com"><img src="https://img.shields.io/badge/Email-D44638?style=for-the-badge&logo=maildotru&logoColor=white"/></a>
<a href="https://t.me/multiheadselfattention"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/></a>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2575fc,100:6a11cb&height=110&section=footer"/>

</div>
