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

**[Математическое моделирование](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/matematicheskoe-modelirovanie)**

- [Лекции](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/matematicheskoe-modelirovanie/lectures)
    - **01.** [Классическая модель парной линейной регрессии](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/01-parnaya-linejnaya-regressiya.md) — 2026-09-01
    - **02.** [Метод наименьших квадратов и теорема Гаусса—Маркова](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/02-mnk-teorema-gaussa-markova.md) — 2026-09-01

**[other](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/other)**

- **01.** [Технология обучения в Университете Синергия](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/other/01-tehnologiya-obucheniya-sinergiya.md) — 2026-09-02

**[Проектная деятельность](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/proektnaya-deyatelnost)**

- [Лекции](https://github.com/aimnoux/synergy-mag/tree/main/semester-1/proektnaya-deyatelnost/lectures)
    - **01.** [Информатизация бизнеса и проектный офис](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/01-informatizaciya-biznesa-proektnyj-ofis.md) — 2026-09-07
    - **02.** [Проектный офис на ступенях зрелости I–III](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/02-proektnyj-ofis-stupeni-zrelosti-1-3.md) — 2026-09-07
    - **03.** [Ступень IV — стратегическое управление портфелем проектов](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/proektnaya-deyatelnost/lectures/03-strategicheskoe-upravlenie-portfelem-proektov.md) — 2026-09-07

<!-- INDEX:END -->
