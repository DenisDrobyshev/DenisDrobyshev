# Denis Drobyshev

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) | [Telegram](https://t.me/multiheadselfattention) | [Portfolio](https://denisdrobyshev.github.io/portfolio/) | [Habr Career](https://career.habr.com/denisdrobyshev) | [DrobyshevDev](https://github.com/DrobyshevDev)

**English** | [Русский](README.ru.md)

## About

I write backends in Python: Django and FastAPI, PostgreSQL, Docker, Nginx. I usually take a project from the database schema and server logic to the interface and deployment. Three of my services run on MIIGAiK university infrastructure: an academic journal portal (my thesis), a class schedule service and the student personal account.

I also work on machine learning: object detection on video, image classification, geospatial analysis on OpenStreetMap data. My open-source libraries live in the DrobyshevDev organisation, and four of them are on PyPI.

Main stack: Python, Django, FastAPI, PostgreSQL, SQL, Docker, Nginx, Gunicorn, Linux, Git.
I have also worked with Go, JavaScript, React, Vue and Java.
Machine learning: PyTorch, TensorFlow, scikit-learn, OpenCV, YOLO.

## Open source

The libraries are in the [DrobyshevDev](https://github.com/DrobyshevDev) organisation, with documentation at [drobyshevdev.github.io](https://drobyshevdev.github.io/).

| Project | What it is | Links |
|---|---|---|
| [decisionrl](https://github.com/DrobyshevDev/decisionrl) | Reinforcement learning for operational problems: pricing, inventory, energy, queues, supply chains. Each problem comes with a classical operations-research method that the trained policy is compared against. | [PyPI](https://pypi.org/project/decisionrl/), [docs](https://drobyshevdev.github.io/decisionrl/) |
| [stadion](https://github.com/DrobyshevDev/stadion) | A benchmark for agents on operational problems. An agent's result is compared with a tuned classical method and with the exact optimum, together with a confidence interval. | [PyPI](https://pypi.org/project/stadion-rl/) |
| [mlango](https://github.com/DrobyshevDev/mlango) | A framework for ML projects modelled on Django. Datasets, models and evaluations are declared in code, and the framework runs, versions and records them. | [PyPI](https://pypi.org/project/mlango/), [docs](https://drobyshevdev.github.io/mlango/) |
| [glia](https://github.com/DrobyshevDev/glia) | A small library for LLM agents. Every model call and tool call can be logged and replayed, and the core has no dependencies. | [PyPI](https://pypi.org/project/glia-agents/), [docs](https://drobyshevdev.github.io/glia/) |
| [praxis](https://github.com/DrobyshevDev/praxis) | A legal assistant for Russian law. Hybrid search over the codes, reranking, and an NLI model that checks every citation. | [release](https://github.com/DrobyshevDev/praxis/releases/latest) |
| [lemma](https://github.com/DrobyshevDev/lemma) | A free course on ML, DL and RL: 27 modules with notebooks, in Russian. | [site](https://drobyshevdev.github.io/lemma/) |

<!-- RELEASES:START -->
Latest releases: [mlango](https://github.com/DrobyshevDev/mlango/releases/tag/v0.3.0) v0.3.0 (22 Aug 2026), [stadion](https://github.com/DrobyshevDev/stadion/releases/tag/v0.1.0) v0.1.0 (9 Aug 2026), [praxis](https://github.com/DrobyshevDev/praxis/releases/tag/v0.1.0) v0.1.0 (31 Jul 2026), [glia](https://github.com/DrobyshevDev/glia/releases/tag/v0.8.2) v0.8.2 (24 Jul 2026), [decisionrl](https://github.com/DrobyshevDev/decisionrl/releases/tag/v0.4.0) v0.4.0 (18 Jul 2026).
<!-- RELEASES:END -->

## Activity

<img alt="GitHub statistics" src="./github-metrics.svg" />

## Experience

**Software developer / DevOps**, MIIGAiK IT department, 2026  
Systems development and support group, production internship.

- Deployed a Django portal on the university's internal infrastructure: PostgreSQL, Gunicorn behind Nginx, static and media files.
- Set up sign-in with the university's corporate account over OpenID Connect.
- Prepared the project for production: moved secrets out of the code, turned off debug mode, configured allowed hosts and system mail.
- Loaded the journal's archive of issues and checked the XML metadata export.

**IT support technician**, MIIGAiK Informatisation Office, Dec 2024 to Mar 2026

- Administered Windows and Linux workstations and servers in an Active Directory domain with SCCM.
- Wrote PowerShell and Bash scripts for repetitive support tasks.
- Repaired and configured computers, installed software and drivers, set up workplaces.

**Backend / web developer**, MIIGAiK internal systems, 2023 to 2024

- Class schedule service: wrote an SQL query that assembles the timetable from several related tables. The university's internal Go services use it.
- Student personal account: schedule, grade book, profile and university news, responsive layout ([miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk)).

## Projects

**GiA, academic journal portal** (thesis, deployed at the university; private repository, demo on request)  
A portal for the journal *Izvestia Vuzov. Geodesy and Aerophotography*: issue archive, admin panel for the editors, reader accounts.

- Admin panel for the editors: issues, articles, inline forms. Only one issue can be current at a time.
- Sign-in through the corporate SSO over OpenID Connect, personal accounts, role-based access.
- Protection against CSRF, XSS and SQL injection, secrets kept outside the repository.
- XML metadata export for bibliographic databases, tests at several levels.

Stack: Python, Django, PostgreSQL, Docker, Nginx, Gunicorn, OpenID Connect.

**[approval-service](https://github.com/DenisDrobyshev/approval-service)**, backend for content approval

- Content goes through a state machine. Every transition is written to an audit log, and events leave the service through a transactional outbox.
- Idempotency-Key support, data isolation per workspace, header auth with scopes, secrets removed from logs.

Stack: Python, FastAPI, async SQLAlchemy 2.0, Alembic, PostgreSQL, Docker, pytest.

**[decisionrl](https://github.com/DrobyshevDev/decisionrl)**, reinforcement learning for operational problems

- Each applied environment comes with a classical operations-research method that the trained policy is compared against. The policy beats it on five tasks and matches the optimal solution on two more.
- Written from scratch: 32 algorithms on PyTorch (DQN and its variants, PPO, SAC, TD3, TRPO, offline, model-based, multi-agent, meta-RL), 24 environments of which 9 are applied, 12 gradient-free optimisers, one predict / learn / save / load interface and a CLI.
- Typed and checked with mypy, CI on Python 3.9 to 3.12, published on PyPI.

Stack: Python, PyTorch, NumPy, Gymnasium, MkDocs, GitHub Actions.

**[Detector_app](https://github.com/DenisDrobyshev/Detector_app)**, real-time detection on video

- Finds events in the frame as they happen: YOLO for detection, InsightFace for face recognition. Works with a webcam or a video file and saves reports to CSV.

Stack: Python, YOLO, InsightFace, OpenCV, Streamlit.

**[Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis)**, choosing a location from geodata (final project of my retraining programme)

- Finds places to open a fitness centre: OpenStreetMap data, an H3 hexagonal grid, an attractiveness model in scikit-learn, interactive maps.

Stack: Python, scikit-learn, H3, OSMnx, GeoPandas.

**[classification_animals](https://github.com/DenisDrobyshev/classification_animals)**, image classifier

- Compared three architectures: a dense network, a plain CNN and a VGG-style network. The best one reached F1 0.88. The model is served through FastAPI with a Streamlit interface.

Stack: Python, TensorFlow/Keras, FastAPI, Streamlit.

<details>
<summary><b>More projects</b></summary>

<br/>

- [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter): a FastAPI service that turns Excel files into validated database tables. Auth, configurable templates, web interface.
- [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store): a shop front on React. Catalogue with filters, cart, wishlist, React Router and Context API.
- [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis): stability analysis of UAV dynamics. Euler and Runge-Kutta methods, eigenvalues, a desktop interface.
- [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch): recognises a function from a hand-drawn graph and exports the formula to text, LaTeX and Excel.
- [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app): converts geodetic coordinates between reference systems with the 7-parameter Helmert formula. FastAPI and Streamlit.
- [marginpilot](https://github.com/DenisDrobyshev/marginpilot): tracks the cost of LLM requests per customer and enforces budgets in real time. Go, in progress.
- [sellerhelper](https://github.com/DenisDrobyshev/sellerhelper): a step-by-step assistant for marketplace sellers that works on live marketplace data. In progress.
- [ScrollStop](https://github.com/DenisDrobyshev/ScrollStop): a three-week plan for quitting short-form video and the research it is based on. In English and Russian.

</details>

## Education

**B.Sc. in Applied Informatics (09.03.03)**, 2022 to 2026  
MIIGAiK (Moscow State University of Geodesy and Cartography), Department of Geoinformatics and Information Security.

**Professional retraining "Big Data Specialist"**, 2024 to 2025  
MIIGAiK Digital Department, programme "Development of geoinformation solutions using artificial intelligence methods".

## Contact

Open to backend and fullstack roles in Moscow, remote or hybrid.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) | [Telegram](https://t.me/multiheadselfattention)
