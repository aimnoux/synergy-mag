# Конспекты

<!-- CURRENT-SEMESTER: 1 -->

Учебные конспекты магистратуры «Менеджмент проектов в области искусственного интеллекта»
(Университет «Синергия», направление «Прикладная информатика»).

## Как устроен репозиторий

```text
.
├── README.md                  ← этот файл: маркер текущего семестра + оглавление
├── scripts/build_index.py     ← пересборка оглавления
├── _inbox/                    ← сюда кладём сырые транскрипты и презентации (не коммитятся)
└── semester-1/
    ├── <предмет>/
    │   ├── lectures/
    │   ├── seminars/
    │   └── labs/
    └── other/                 ← всё вне сетки дисциплин, файлы лежат плоско
```

- Один конспект — один `.md`-файл с YAML-фронтматтером (`title`, `subject`, `type`, `date`).
- Имена папок и файлов — латиница, kebab-case. Русские названия живут во фронтматтере.
- Файлы занятий именуются `NN-slug.md`. Нумерация своя внутри каждой группы «семестр / предмет / тип»: начинается с `01`, всегда двузначная, без пропусков (`lectures/01-…` и `seminars/01-…` рядом — это норма).
- Внеучебные материалы (установочные встречи, инструктажи) складываются в `semester-N/other/` без подпапки типа; `subject` и `type` у них — `other`.
- Текущий семестр задаётся маркером `<!-- CURRENT-SEMESTER: N -->` выше. Меняем его вручную в начале нового семестра.

## Рабочий процесс

1. Транскрипт лекции (и презентацию, если есть) кладём в `_inbox/`.
2. Просим Claude сделать конспект — он появится в `semester-N/<предмет>/<тип>/NN-slug.md`.
3. Оглавление пересобирается:

   ```bash
   python scripts/build_index.py
   ```

4. Коммитим конспект вместе с обновлённым `README.md`.

## Оглавление

<!-- INDEX:START -->

### [Семестр 1](https://github.com/aimnoux/synergy-mag/tree/main/semester-1) (текущий)

**[Информационный менеджмент](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/informacionnyj-menedzhment)**

- [Лекции](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/informacionnyj-menedzhment/lectures)
    - **01.** [Менеджмент бизнес-информации](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/informacionnyj-menedzhment/lectures/01-menedzhment-biznes-informacii.md) — 2026-09-12
    - **02.** [Стратегическое целевое управление ИТ и структура ИТ-стратегии](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/informacionnyj-menedzhment/lectures/02-strategicheskoe-celevoe-upravlenie-it.md) — 2026-09-12
    - **03.** [Способы приобретения и факторы качества ИС](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/informacionnyj-menedzhment/lectures/03-sposoby-priobreteniya-kachestvo-is.md) — 2026-09-26
    - **04.** [Эксплуатация ИС: ITIL, SLA, риски и ИТ-аудит](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/informacionnyj-menedzhment/lectures/04-ekspluataciya-is-sla-riski-it-audit.md) — 2026-09-26

**[Математическое моделирование](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/matematicheskoe-modelirovanie)**

- [Лекции](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/matematicheskoe-modelirovanie/lectures)
    - **01.** [Классическая модель парной линейной регрессии](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/01-parnaya-linejnaya-regressiya.md) — 2026-09-01
    - **02.** [Метод наименьших квадратов и теорема Гаусса—Маркова](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/02-mnk-teorema-gaussa-markova.md) — 2026-09-01
    - **03.** [Мультиколлинеарность: природа, признаки и диагностика](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/03-multikollinearnost-diagnostika.md) — 2026-09-08
    - **04.** [Фиктивные переменные и отбор регрессоров](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/04-fiktivnye-peremennye-i-otbor-regressorov.md) — 2026-09-08
    - **05.** [Цепи Маркова с дискретным временем](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/05-cepi-markova-diskretnoe-vremya.md) — 2026-09-15
    - **06.** [Эргодичность, PageRank и уравнения Колмогорова](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/06-ergodichnost-pagerank-uravneniya-kolmogorova.md) — 2026-09-15
    - **07.** [Практикум 1. Регрессия цены квартиры на площадь — задание](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/07-praktikum-1-regressiya-ceny-kvartiry-zadanie.md) — 2026-09-22
    - **08.** [Практикум 1. Вопросы по заданию и сдаче](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/08-praktikum-1-voprosy-po-zadaniyu-i-sdache.md) — 2026-09-22

**[other](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/other)**

- **01.** [Технология обучения в Университете Синергия](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/other/01-tehnologiya-obucheniya-sinergiya.md) — 2026-09-02

**[Проектная деятельность](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/proektnaya-deyatelnost)**

- [Лабораторные](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/proektnaya-deyatelnost/labs)
    - **01.** [Лабораторный практикум 1: организация работы и теоретическая часть](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/01-organizaciya-raboty-i-teoreticheskaya-chast.md) — 2026-09-10
    - **02.** [Критерии успеха проекта и магический треугольник](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/02-kriterii-uspeha-i-magicheskij-treugolnik.md) — 2026-09-10
    - **03.** [Кейс «ТехноПрогресс»: цель ИТ-стратегии и категории мероприятий](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/03-kejs-tehnoprogress-it-strategiya.md) — 2026-09-17
    - **04.** [Кейс «ТехноПрогресс»: проектирование проектного офиса](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/04-proektirovanie-proektnogo-ofisa-tehnoprogress.md) — 2026-09-17
    - **05.** [Кейс «ТехноПрогресс»: балансировка портфеля и сдача ЛП1](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/05-kejs-tehnoprogress-balansirovka-portfelya.md) — 2026-09-24
    - **06.** [Кейс «ТехноПрогресс»: управление проектом внедрения ERP](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/labs/06-kejs-tehnoprogress-upravlenie-proektom-erp.md) — 2026-09-24
- [Лекции](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/proektnaya-deyatelnost/lectures)
    - **01.** [Информатизация бизнеса и проектный офис](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/01-informatizaciya-biznesa-proektnyj-ofis.md) — 2026-09-03
    - **02.** [Проектный офис на ступенях зрелости I–III](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/02-proektnyj-ofis-stupeni-zrelosti-1-3.md) — 2026-09-03
    - **03.** [Ступень IV — стратегическое управление портфелем проектов](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/03-strategicheskoe-upravlenie-portfelem-proektov.md) — 2026-09-04
    - **04.** [ITSM, ITIL 4 и основы управления ИТ-проектами](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/04-itsm-itil-osnovy-upravleniya-it-proektami.md) — 2026-09-04
    - **05.** [ИТ-проекты: этапы, стейкхолдеры, команда и коммуникации](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/05-it-proekty-stejkholdery-komanda-kommunikacii.md) — 2026-09-11
    - **06.** [Базовый план проекта и управление рисками](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/06-bazovyj-plan-upravlenie-riskami.md) — 2026-09-11

<!-- INDEX:END -->
