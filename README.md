# Denis Drobyshev

Fullstack developer — Python, Django, FastAPI, React.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) · [Telegram](https://t.me/multiheadselfattention) · [Portfolio](https://denisdrobyshev.github.io/portfolio/) · [Habr Career](https://career.habr.com/denisdrobyshev) · [DrobyshevDev](https://github.com/DrobyshevDev)

**English** · [Русский](README.ru.md)

## About

I write backends in Python: Django and FastAPI, PostgreSQL underneath, Docker and Nginx in front. I take a project the whole way — schema, server logic, API, interface, deployment. A service that runs only on my laptop is not finished, and three of mine run on MIIGAiK infrastructure: the journal portal from my thesis, the class schedule service and the student personal account.

Alongside that I release open source: five projects under tagged releases, three of them on PyPI. Machine learning and computer vision run on the same stack — real-time detection on video, image classifiers, a geospatial pipeline over OpenStreetMap.

- **Core:** Python · Django · FastAPI · PostgreSQL · SQL · Docker · Nginx · Gunicorn · Linux · Git
- **Also:** Go · JavaScript · React · Vue · Java
- **ML / CV:** PyTorch · TensorFlow · scikit-learn · OpenCV · YOLO

## Open source

Libraries and tooling for machine learning, LLM agents and operational decisions, kept in the [DrobyshevDev](https://github.com/DrobyshevDev) organisation and documented at [drobyshevdev.github.io](https://drobyshevdev.github.io/). The libraries are typed, tested in CI and published under tagged releases.

| Project | What it is | |
|---|---|---|
| [**decisionrl**](https://github.com/DrobyshevDev/decisionrl) | Reinforcement learning for operational decisions: pricing, inventory, energy, queues, supply chains. Every applied environment ships with its classical operations-research baseline, so a policy is measured against the standard method rather than asserted to be good. | [PyPI](https://pypi.org/project/decisionrl/) · [docs](https://drobyshevdev.github.io/decisionrl/) |
| [**stadion**](https://github.com/DrobyshevDev/stadion) | A proving ground for operational decisions: agents are scored against the tuned classical method and the exact optimum, with a confidence interval. | [PyPI](https://pypi.org/project/stadion-rl/) |
| [**mlango**](https://github.com/DrobyshevDev/mlango) | A framework for ML, analytics and LLM agents, built on Django's philosophy: you declare datasets, models and evaluations, the framework runs, versions and records them. | [PyPI](https://pypi.org/project/mlango/) · [docs](https://drobyshevdev.github.io/mlango/) |
| [**glia**](https://github.com/DrobyshevDev/glia) | A glass-box library for building LLM agents: modern techniques as opt-in primitives, no hidden control flow, zero-dependency core. | [docs](https://drobyshevdev.github.io/glia/) |
| [**praxis**](https://github.com/DrobyshevDev/praxis) | A legal assistant for Russian law whose citations are verified rather than asserted: hybrid retrieval with reranking, an NLI citation verifier, GraphRAG over cross-references. | [release](https://github.com/DrobyshevDev/praxis/releases/latest) |
| [**lemma**](https://github.com/DrobyshevDev/lemma) | A free course: a road map through ML, DL and RL, from zero to reading and reproducing research. 27 modules, in Russian. | [site](https://drobyshevdev.github.io/lemma/) |

<!-- RELEASES:START -->
Latest releases: [**stadion**](https://github.com/DrobyshevDev/stadion/releases/tag/v0.1.0) v0.1.0 (9 Aug 2026) · [**praxis**](https://github.com/DrobyshevDev/praxis/releases/tag/v0.1.0) v0.1.0 (31 Jul 2026) · [**mlango**](https://github.com/DrobyshevDev/mlango/releases/tag/v0.2.0) v0.2.0 (31 Jul 2026) · [**glia**](https://github.com/DrobyshevDev/glia/releases/tag/v0.8.2) v0.8.2 (24 Jul 2026) · [**decisionrl**](https://github.com/DrobyshevDev/decisionrl/releases/tag/v0.4.0) v0.4.0 (18 Jul 2026)
<!-- RELEASES:END -->

## GitHub activity

<p align="center">
  <img alt="GitHub metrics — commits, pull requests, contributions, languages" src="./github-metrics.svg" />
</p>

<p align="center">
  <img alt="Contribution streak" src="https://streak-stats.demolab.com/?user=DenisDrobyshev&theme=tokyonight&hide_border=true&v=3" />
</p>

> Commits, pull requests and contributions are counted across all public repositories, including pull requests to repositories I don't own. The stats image is generated in CI and committed to this repository, so it never depends on a live third-party service.

## Experience

**Software developer / DevOps — MIIGAiK, IT department (DIT)** · `2026`<br>
Systems development and support group; production internship.

- Deployed a Django portal on the university's internal infrastructure: PostgreSQL, Gunicorn behind Nginx, static and media serving.
- Set up single sign-on with the corporate university account over OpenID Connect.
- Moved the project from development to production: secret management, debug mode, allowed hosts, system mail.
- Loaded the real journal archive and verified metadata export to XML.

**IT support technician — MIIGAiK, Informatisation Office** · `Dec 2024 – Jan 2026`<br>
IT support service, 1 year 2 months.

- Administered Windows and Linux workstations and servers in an Active Directory domain.
- Wrote PowerShell and Bash automation for routine support work.
- Kept the hardware running and set workplaces up: diagnostics, repair, software and driver configuration.

**Backend / web developer — MIIGAiK internal systems** · `2023–2024`<br>
Work on university services during my studies.

- Class schedule service: a large SQL query that assembles the timetable from several related tables, integrated into the university's internal Go services.
- Student personal account: schedule, grade book, profile and university news, with a responsive interface ([miigaik-lk](https://github.com/DenisDrobyshev/miigaik-lk)).
- The infrastructure already existed — the work was reading other people's code, matching their conventions, and shipping changes that had to fit the rest of the system.

## Projects

**GiA — academic journal portal** · `thesis, deployed` · private repository, demo on request<br>
A portal for *Izvestia Vuzov. Geodesy and Aerophotography*: issue archive, editorial admin, reader accounts. Designed, built and deployed on university infrastructure.

- Admin panel generated for the editorial team: issues, articles, inline forms, with the rule that exactly one issue can be current.
- Corporate SSO over OpenID Connect, personal accounts, role-based access.
- Protection against CSRF, XSS and SQL injection; secrets kept out of the repository.
- XML metadata export for bibliographic indexing, and tests at several levels.
- `Python · Django · PostgreSQL · Docker · Nginx · Gunicorn · OIDC`

**[approval-service](https://github.com/DenisDrobyshev/approval-service) — content approval backend**

- Content moves through a state machine: every transition lands in an audit log, and events leave the service through a transactional outbox.
- Idempotency-Key support, per-workspace multi-tenant isolation, scope-based header auth, secrets redacted in logs.
- `Python · FastAPI · async SQLAlchemy 2.0 · Alembic · PostgreSQL · Docker · pytest`

**[decisionrl](https://github.com/DrobyshevDev/decisionrl) — reinforcement learning for operational decisions**

- Each applied environment ships with the classical operations-research baseline it has to beat. Over five seeds the learned policy beats the strong baseline on five tasks and matches the exact dynamic-programming optimum where one exists; PPO reaches parity with Stable-Baselines3 on CartPole.
- Written from scratch: 31 algorithms (DQN family, PPO, SAC, TD3, TRPO, offline, model-based, multi-agent, meta-RL) on PyTorch, 22 environments of which 9 are applied, 12 gradient-free optimizers, one `predict / learn / save / load` interface, a CLI and Gymnasium registration.
- 400 tests, 86% coverage, typed and checked with mypy, CI on Python 3.9–3.12, published on PyPI.
- `Python · PyTorch · NumPy · Gymnasium · MkDocs · GitHub Actions`

**[Detector_app](https://github.com/DenisDrobyshev/Detector_app) — real-time detection on video**

- Finds events in the frame live: YOLO for detection, InsightFace for face recognition. Works with a webcam or a video file and produces CSV reports.
- `Python · YOLO · InsightFace · OpenCV · Streamlit`

**[Geomarketing_analysis](https://github.com/DenisDrobyshev/Geomarketing_analysis) — choosing a location from geodata**

- Where to open a fitness centre: OpenStreetMap data, an H3 hex grid, an attractiveness model in scikit-learn, interactive maps.
- `Python · scikit-learn · H3 · OSMnx · GeoPandas`

**[classification_animals](https://github.com/DenisDrobyshev/classification_animals) — image classifier**

- Three architectures compared — dense, plain CNN, VGG-style. Best F1 0.88. Inference served through FastAPI behind a Streamlit interface.
- `Python · TensorFlow/Keras · FastAPI · Streamlit`

<details>
<summary><b>More projects</b></summary>

<br/>

- [excel-to-db-converter](https://github.com/DenisDrobyshev/excel-to-db-converter): FastAPI service that turns Excel files into validated database tables — auth, configurable templates, web UI.
- [chinese-premium-store](https://github.com/DenisDrobyshev/chinese-premium-store): storefront on React — catalogue with filters, cart, wishlist, React Router and Context API.
- [StableDroneSystemAnalysis](https://github.com/DenisDrobyshev/StableDroneSystemAnalysis): stability analysis of UAV dynamics — Euler and Runge-Kutta integration, eigenvalues, GUI.
- [FunctionSketch](https://github.com/DenisDrobyshev/FunctionSketch): recognises a function from a hand-drawn graph and exports the formula to text, LaTeX and Excel.
- [StreamlitFastAPI_app](https://github.com/DenisDrobyshev/StreamlitFastAPI_app): geodetic coordinate transformation between reference systems, 7-parameter Helmert, FastAPI + Streamlit.
- [marginpilot](https://github.com/DenisDrobyshev/marginpilot): per-customer LLM cost metering and real-time budgets between an application and the model providers. Go, in progress.
- [sellerhelper](https://github.com/DenisDrobyshev/sellerhelper): stage-gated assistant for marketplace sellers, working from live marketplace data. In progress.
- [ScrollStop](https://github.com/DenisDrobyshev/ScrollStop): a three-week method for quitting short-form video, with the research behind it. EN/RU.

</details>

## Education

**B.Sc. in Applied Informatics (09.03.03)** · `2022–2026`<br>
MIIGAiK — Moscow State University of Geodesy and Cartography, Department of Geoinformatics and Information Security.

## Contact

Open to backend and fullstack roles — Moscow, remote or hybrid.

[drobishev.denis@icloud.com](mailto:drobishev.denis@icloud.com) · [Telegram](https://t.me/multiheadselfattention)
