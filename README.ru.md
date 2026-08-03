# Денис Дробышев

Бэкенд-разработчик — Python, Django, FastAPI. Москва, открыт к предложениям.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) · [Telegram](https://t.me/multiheadselfattention) · [Портфолио](https://denisdrobyshev.github.io/portfolio/) · [Хабр Карьера](https://career.habr.com/denisdrobyshev) · [DrobyshevDev](https://github.com/DrobyshevDev)

[English](README.md) · **Русский**

## О себе

Пишу бэкенды на Python: Django и FastAPI, снизу PostgreSQL, спереди Docker и Nginx. Веду проект целиком — схема, серверная логика, API, интерфейс, деплой. Сервис, который работает только на моём ноутбуке, не закончен, и **три моих работают на инфраструктуре МИИГАиК**: портал журнала из дипломной работы, сервис расписания и личный кабинет студента.

Рядом с вебом — машинное обучение и компьютерное зрение: детекция на видео в реальном времени, классификаторы изображений, геоаналитический пайплайн по данным OpenStreetMap.

- **Основное:** Python · Django · FastAPI · PostgreSQL · SQL · Docker · Nginx · Gunicorn · Linux · Git
- **Также:** Go · JavaScript · React · Vue
- **ML / CV:** PyTorch · TensorFlow · scikit-learn · OpenCV · YOLO

## Открытый код

Библиотеки и инструменты для машинного обучения, LLM-агентов и операционных решений лежат в организации [DrobyshevDev](https://github.com/DrobyshevDev), документация — на [drobyshevdev.github.io](https://drobyshevdev.github.io/). Библиотеки типизированы, покрыты тестами в CI и выпускаются тегированными релизами.

| Проект | Что это | |
|---|---|---|
| [**decisionrl**](https://github.com/DrobyshevDev/decisionrl) | Обучение с подкреплением для операционных решений: ценообразование, запасы, энергетика, очереди, цепочки поставок. Каждая прикладная среда идёт со своим классическим baseline из исследования операций, поэтому политику измеряют, а не объявляют хорошей. | [PyPI](https://pypi.org/project/decisionrl/) · [документация](https://drobyshevdev.github.io/decisionrl/) |
| [**mlango**](https://github.com/DrobyshevDev/mlango) | Фреймворк для ML, аналитики и LLM-агентов, построенный на философии Django: вы объявляете датасеты, модели и оценки, фреймворк их запускает, версионирует и записывает. | [PyPI](https://pypi.org/project/mlango/) · [документация](https://drobyshevdev.github.io/mlango/) |
| [**glia**](https://github.com/DrobyshevDev/glia) | Прозрачная библиотека для сборки LLM-агентов: современные техники как опциональные примитивы, никакого скрытого потока управления, ядро без зависимостей. | [документация](https://drobyshevdev.github.io/glia/) |
| [**praxis**](https://github.com/DrobyshevDev/praxis) | Юридический ассистент по праву РФ, у которого цитаты проверяются, а не утверждаются: гибридный поиск с реранкингом, NLI-верификатор цитат, GraphRAG по перекрёстным ссылкам. | [релиз](https://github.com/DrobyshevDev/praxis/releases/latest) |
| [**lemma**](https://github.com/DrobyshevDev/lemma) | Бесплатный курс: дорожная карта в ML, DL и RL — с нуля и до умения читать и воспроизводить исследования. 27 модулей. | [сайт](https://drobyshevdev.github.io/lemma/) |

<!-- RELEASES:START -->
Последние релизы: [**praxis**](https://github.com/DrobyshevDev/praxis/releases/tag/v0.1.0) v0.1.0 (31 июля 2026) · [**mlango**](https://github.com/DrobyshevDev/mlango/releases/tag/v0.2.0) v0.2.0 (31 июля 2026) · [**glia**](https://github.com/DrobyshevDev/glia/releases/tag/v0.8.2) v0.8.2 (24 июля 2026) · [**decisionrl**](https://github.com/DrobyshevDev/decisionrl/releases/tag/v0.4.0) v0.4.0 (18 июля 2026)
<!-- RELEASES:END -->

## Опыт

**Разработчик / DevOps — МИИГАиК, департамент информационных технологий (ДИТ)** · `2026`<br>
Производственная практика, группа разработки и сопровождения систем.

- Развернул Django-портал на внутренней инфраструктуре университета: PostgreSQL, Gunicorn за Nginx, раздача статики и медиа.
- Настроил единый вход через корпоративную учётную запись университета по OpenID Connect.
- Перевёл проект из разработки в продакшен: управление секретами, режим отладки, разрешённые хосты, системная почта.
- Загрузил реальный архив выпусков журнала и проверил экспорт метаданных в XML.

**Бэкенд / веб-разработчик — внутренние системы МИИГАиК** · `2023–2024`<br>
Работа над университетскими сервисами во время учёбы.

- Сервис расписания занятий: большой SQL-запрос, который собирает расписание из нескольких связанных таблиц, встроен во внутренние Go-сервисы университета.
- Личный кабинет студента: расписание, зачётная книжка, профиль и новости университета, адаптивный интерфейс ([miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk)).
- Инфраструктура уже существовала — работа состояла в чтении чужого кода, следовании чужим соглашениям и внесении изменений, которые должны были встать в остальную систему.

## Проекты

**GiA — портал научного журнала** · `дипломная работа, развёрнут` · приватный репозиторий, демо по запросу<br>
Портал журнала «Известия вузов. Геодезия и аэрофотосъёмка»: архив выпусков, редакторская админка, личные кабинеты читателей. Спроектирован, собран и развёрнут на университетской инфраструктуре.

- Админка для редакции: выпуски, статьи, инлайн-формы, с правилом, что текущим может быть ровно один выпуск.
- Корпоративный SSO по OpenID Connect, личные кабинеты, доступ по ролям.
- Защита от CSRF, XSS и SQL-инъекций; секреты вне репозитория.
- Экспорт метаданных в XML для библиографического индексирования и тесты на нескольких уровнях.
- `Python · Django · PostgreSQL · Docker · Nginx · Gunicorn · OIDC`

**[approval-service](https://github.com/DenisDrobyshev/approval-service) — бэкенд согласования контента** · `тестовое задание`

- Контент двигается по конечному автомату: каждый переход попадает в журнал аудита, а события уходят из сервиса через транзакционный outbox.
- Поддержка Idempotency-Key, изоляция арендаторов по воркспейсам, авторизация по заголовку со скоупами, вырезание секретов из логов.
- `Python · FastAPI · async SQLAlchemy 2.0 · Alembic · PostgreSQL · Docker · pytest`

**[decisionrl](https://github.com/DrobyshevDev/decisionrl) — обучение с подкреплением для операционных решений**

- Каждая прикладная среда идёт с классическим baseline, который надо побить. На пяти сидах обученная политика обходит сильный baseline на пяти задачах и совпадает с точным оптимумом динамического программирования там, где он существует; PPO выходит на паритет со Stable-Baselines3 на CartPole.
- Написано с нуля: 31 алгоритм (семейство DQN, PPO, SAC, TD3, TRPO, offline, model-based, мультиагентные, meta-RL) на PyTorch, 22 среды, из них 9 прикладных, 12 безградиентных оптимизаторов, единый интерфейс `predict / learn / save / load`, CLI и регистрация в Gymnasium.
- 400 тестов, покрытие 86%, типизировано и проверено mypy, CI на Python 3.9–3.12, опубликовано на PyPI.
- `Python · PyTorch · NumPy · Gymnasium · MkDocs · GitHub Actions`

**[Detector_app](https://github.com/DenisDrobyshev/Detector_app) — детекция на видео в реальном времени**

- Находит события в кадре на лету: YOLO для детекции, InsightFace для распознавания лиц. Работает с веб-камерой и с видеофайлом, отдаёт отчёты в CSV.
- `Python · YOLO · InsightFace · OpenCV · Streamlit`

**[Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis) — выбор локации по геоданным**

- Где открыть фитнес-центр: данные OpenStreetMap, гексагональная сетка H3, модель привлекательности на scikit-learn, интерактивные карты.
- `Python · scikit-learn · H3 · OSMnx · GeoPandas`

**[classification_animals](https://github.com/DenisDrobyshev/classification_animals) — классификатор изображений**

- Сравнил три архитектуры — полносвязная, простая CNN, в стиле VGG. Лучший результат F1 0.88. Инференс отдаётся через FastAPI за интерфейсом на Streamlit.
- `Python · TensorFlow/Keras · FastAPI · Streamlit`

<details>
<summary><b>Остальные проекты</b></summary>

<br/>

- [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter): сервис на FastAPI, превращающий файлы Excel в валидированные таблицы базы — авторизация, настраиваемые шаблоны, веб-интерфейс.
- [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store): витрина магазина на React — каталог с фильтрами, корзина, избранное, React Router и Context API.
- [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis): анализ устойчивости динамики БПЛА — интегрирование методами Эйлера и Рунге-Кутты, собственные числа, GUI.
- [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch): распознаёт функцию по нарисованному от руки графику и выгружает формулу в текст, LaTeX и Excel.
- [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app): пересчёт геодезических координат между референц-системами, 7-параметрическая формула Гельмерта, FastAPI + Streamlit.
- [marginpilot](https://github.com/DenisDrobyshev/marginpilot): учёт стоимости LLM по каждому клиенту и бюджеты в реальном времени между приложением и провайдерами моделей. Go, в работе.
- [sellerhelper](https://github.com/DenisDrobyshev/sellerhelper): пошаговый ассистент для продавцов маркетплейсов, работающий на живых данных площадок. В работе.
- [ScrollStop](https://github.com/DenisDrobyshev/ScrollStop): трёхнедельный метод отказа от коротких видео вместе с исследованиями, на которых он стоит. EN/RU.
- [universum](https://github.com/DenisDrobyshev/universum) · [CIFAR10](https://github.com/DenisDrobyshev/CIFAR10): практические работы по нейросетям и ML за выпускной курс.

Ранние учебные работы — игры, задачи на Java, первые приложения на React и Flutter — заархивированы, а не удалены: история остаётся читаемой и не конкурирует за внимание с текущей работой.

</details>

## Образование

**Бакалавр, прикладная информатика (09.03.03)** · `2022–2026`<br>
МИИГАиК — Московский государственный университет геодезии и картографии, факультет геоинформатики и информационной безопасности.

## Контакты

Ищу первую полноценную работу джуниор-бэкенд / Python-разработчиком: Москва, удалённо или гибрид, готов выйти сразу.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) · [Telegram](https://t.me/multiheadselfattention)
