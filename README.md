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
    └── <предмет>/
        ├── lectures/
        ├── seminars/
        └── labs/
```

- Один конспект — один `.md`-файл с YAML-фронтматтером (`title`, `subject`, `type`, `date`).
- Имена папок и файлов — латиница, kebab-case. Русские названия живут во фронтматтере.
- Файлы занятий именуются `NN-slug.md` (`01`, `02`, …) — по порядку прохождения курса.
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
    - [Классическая модель парной линейной регрессии](https://github.com/aimnoux/synergy-mag/blob/main/semester-1/matematicheskoe-modelirovanie/lectures/01-parnaya-linejnaya-regressiya.md) — 2026-09-01

<!-- INDEX:END -->
