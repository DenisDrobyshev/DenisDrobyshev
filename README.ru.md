# Денис Дробышев

Фулстек-разработчик: Python, Django, FastAPI, React.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) | [Telegram](https://t.me/multiheadselfattention) | [Портфолио](https://denisdrobyshev.github.io/portfolio/) | [Хабр Карьера](https://career.habr.com/denisdrobyshev) | [DrobyshevDev](https://github.com/DrobyshevDev)

[English](README.md) | **Русский**

## О себе

Пишу бэкенд на Python: Django и FastAPI, PostgreSQL, Docker, Nginx. Обычно веду проект целиком, от схемы базы данных и серверной логики до интерфейса и развёртывания. Три моих сервиса работают в инфраструктуре МИИГАиК: портал научного журнала (дипломная работа), сервис расписания и личный кабинет студента.

Ещё занимаюсь машинным обучением: детекция объектов на видео, классификация изображений, геоаналитика по данным OpenStreetMap. Открытые библиотеки выпускаю в организации DrobyshevDev, четыре из них опубликованы на PyPI.

Основной стек: Python, Django, FastAPI, PostgreSQL, SQL, Docker, Nginx, Gunicorn, Linux, Git.
Также работал с Go, JavaScript, React, Vue и Java.
Машинное обучение: PyTorch, TensorFlow, scikit-learn, OpenCV, YOLO.

## Открытый код

Библиотеки лежат в организации [DrobyshevDev](https://github.com/DrobyshevDev), документация на [drobyshevdev.github.io](https://drobyshevdev.github.io/).

| Проект | Что это | Ссылки |
|---|---|---|
| [decisionrl](https://github.com/DrobyshevDev/decisionrl) | Обучение с подкреплением для операционных задач: ценообразование, запасы, энергетика, очереди, цепочки поставок. Для каждой задачи есть классический метод из исследования операций, с которым сравнивается обученная политика. | [PyPI](https://pypi.org/project/decisionrl/), [документация](https://drobyshevdev.github.io/decisionrl/) |
| [stadion](https://github.com/DrobyshevDev/stadion) | Среда для оценки агентов в операционных задачах. Результат агента сравнивается с настроенным классическим методом и с точным оптимумом, считается доверительный интервал. | [PyPI](https://pypi.org/project/stadion-rl/) |
| [mlango](https://github.com/DrobyshevDev/mlango) | Фреймворк для ML-проектов по образцу Django. Датасеты, модели и оценки описываются в коде, фреймворк их запускает, версионирует и сохраняет результаты. | [PyPI](https://pypi.org/project/mlango/), [документация](https://drobyshevdev.github.io/mlango/) |
| [glia](https://github.com/DrobyshevDev/glia) | Небольшая библиотека для LLM-агентов. Каждый вызов модели и инструмента можно записать и воспроизвести, у ядра нет зависимостей. | [PyPI](https://pypi.org/project/glia-agents/), [документация](https://drobyshevdev.github.io/glia/) |
| [praxis](https://github.com/DrobyshevDev/praxis) | Юридический ассистент по праву РФ. Гибридный поиск по кодексам, переранжирование результатов и проверка каждой цитаты NLI-моделью. | [релиз](https://github.com/DrobyshevDev/praxis/releases/latest) |
| [lemma](https://github.com/DrobyshevDev/lemma) | Бесплатный курс по ML, DL и RL: 27 модулей с ноутбуками, на русском. | [сайт](https://drobyshevdev.github.io/lemma/) |

<!-- RELEASES:START -->
Последние релизы: [mlango](https://github.com/DrobyshevDev/mlango/releases/tag/v0.3.0) v0.3.0 (22 августа 2026), [stadion](https://github.com/DrobyshevDev/stadion/releases/tag/v0.1.0) v0.1.0 (9 августа 2026), [praxis](https://github.com/DrobyshevDev/praxis/releases/tag/v0.1.0) v0.1.0 (31 июля 2026), [glia](https://github.com/DrobyshevDev/glia/releases/tag/v0.8.2) v0.8.2 (24 июля 2026), [decisionrl](https://github.com/DrobyshevDev/decisionrl/releases/tag/v0.4.0) v0.4.0 (18 июля 2026).
<!-- RELEASES:END -->

## Активность

<img alt="Статистика GitHub" src="./github-metrics.svg" />

## Опыт

**Разработчик / DevOps**, дирекция информационных технологий МИИГАиК, 2026  
Группа разработки и сопровождения систем, производственная практика.

- Развернул портал на Django во внутренней инфраструктуре университета: PostgreSQL, Gunicorn за Nginx, раздача статики и медиафайлов.
- Настроил вход через корпоративную учётную запись университета по OpenID Connect.
- Подготовил проект к эксплуатации: вынес секреты из кода, отключил режим отладки, настроил разрешённые хосты и системную почту.
- Загрузил архив выпусков журнала и проверил выгрузку метаданных в XML.

**Техник технической поддержки**, управление информатизации МИИГАиК, дек. 2024 – янв. 2026

- Администрировал рабочие станции и серверы на Windows и Linux в домене Active Directory через SCCM.
- Писал скрипты на PowerShell и Bash для повторяющихся задач поддержки.
- Ремонтировал и настраивал компьютеры, устанавливал программы и драйверы, готовил рабочие места.

**Бэкенд / веб-разработчик**, внутренние системы МИИГАиК, 2023–2024

- Сервис расписания: написал SQL-запрос, который собирает расписание из нескольких связанных таблиц. Его используют внутренние сервисы университета на Go.
- Личный кабинет студента: расписание, зачётная книжка, профиль и новости университета, адаптивная вёрстка ([miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk)).

## Проекты

**GiA, портал научного журнала** (дипломная работа, развёрнут в университете; репозиторий закрытый, демо по запросу)  
Портал журнала «Известия вузов. Геодезия и аэрофотосъёмка»: архив выпусков, админка для редакции, личные кабинеты читателей.

- Админка для редакции: выпуски, статьи, вложенные формы. Текущим может быть только один выпуск.
- Вход через корпоративный SSO по OpenID Connect, личные кабинеты, доступ по ролям.
- Защита от CSRF, XSS и SQL-инъекций, секреты хранятся вне репозитория.
- Выгрузка метаданных в XML для библиографических баз, тесты на нескольких уровнях.

Стек: Python, Django, PostgreSQL, Docker, Nginx, Gunicorn, OpenID Connect.

**[approval-service](https://github.com/DenisDrobyshev/approval-service)**, бэкенд согласования контента

- Контент проходит через конечный автомат. Каждый переход записывается в журнал аудита, события уходят из сервиса через transactional outbox.
- Поддержка Idempotency-Key, изоляция данных по рабочим пространствам, авторизация по заголовку со скоупами, секреты вырезаются из логов.

Стек: Python, FastAPI, async SQLAlchemy 2.0, Alembic, PostgreSQL, Docker, pytest.

**[decisionrl](https://github.com/DrobyshevDev/decisionrl)**, обучение с подкреплением для операционных задач

- К каждой прикладной среде прилагается классический метод из исследования операций, с которым сравнивается обученная политика. На пяти задачах политика его обходит, ещё на двух совпадает с оптимальным решением.
- Написано с нуля: 32 алгоритма на PyTorch (DQN и его варианты, PPO, SAC, TD3, TRPO, offline, model-based, мультиагентные, meta-RL), 24 среды, из них 9 прикладных, 12 безградиентных оптимизаторов, единый интерфейс predict / learn / save / load и CLI.
- Код типизирован и проверяется mypy, CI на Python 3.9–3.12, пакет опубликован на PyPI.

Стек: Python, PyTorch, NumPy, Gymnasium, MkDocs, GitHub Actions.

**[Detector_app](https://github.com/DenisDrobyshev/Detector_app)**, детекция на видео в реальном времени

- Находит события в кадре на лету: YOLO для детекции, InsightFace для распознавания лиц. Работает с веб-камерой и видеофайлами, сохраняет отчёты в CSV.

Стек: Python, YOLO, InsightFace, OpenCV, Streamlit.

**[Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis)**, выбор места по геоданным (итоговый проект переподготовки)

- Подбирает место для фитнес-центра: данные OpenStreetMap, гексагональная сетка H3, модель привлекательности на scikit-learn, интерактивные карты.

Стек: Python, scikit-learn, H3, OSMnx, GeoPandas.

**[classification_animals](https://github.com/DenisDrobyshev/classification_animals)**, классификатор изображений

- Сравнил три архитектуры: полносвязную сеть, простую CNN и сеть в стиле VGG. Лучший результат F1 0.88. Модель отдаётся через FastAPI, интерфейс на Streamlit.

Стек: Python, TensorFlow/Keras, FastAPI, Streamlit.

<details>
<summary><b>Остальные проекты</b></summary>

<br/>

- [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter): сервис на FastAPI, который превращает файлы Excel в проверенные таблицы базы данных. Авторизация, настраиваемые шаблоны, веб-интерфейс.
- [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store): витрина магазина на React. Каталог с фильтрами, корзина, избранное, React Router и Context API.
- [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis): анализ устойчивости динамики БПЛА. Методы Эйлера и Рунге-Кутты, собственные числа, графический интерфейс.
- [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch): распознаёт функцию по графику, нарисованному от руки, и выгружает формулу в текст, LaTeX и Excel.
- [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app): пересчёт геодезических координат между системами координат по 7-параметрической формуле Гельмерта. FastAPI и Streamlit.
- [marginpilot](https://github.com/DenisDrobyshev/marginpilot): учёт стоимости запросов к LLM по каждому клиенту и бюджеты в реальном времени. Go, в работе.
- [sellerhelper](https://github.com/DenisDrobyshev/sellerhelper): пошаговый помощник для продавцов маркетплейсов на живых данных площадок. В работе.
- [ScrollStop](https://github.com/DenisDrobyshev/ScrollStop): трёхнедельный план отказа от коротких видео и исследования, на которые он опирается. На русском и английском.

</details>

## Образование

**Бакалавриат, прикладная информатика (09.03.03)**, 2022–2026  
МИИГАиК, факультет геоинформатики и информационной безопасности.

**Профессиональная переподготовка «Специалист по большим данным»**, 2024–2025  
Цифровая кафедра МИИГАиК, программа «Разработка геоинформационных решений с использованием методов искусственного интеллекта».

## Контакты

Открыт к предложениям по бэкенду и фулстеку, Москва, удалённо или гибрид.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) | [Telegram](https://t.me/multiheadselfattention)
