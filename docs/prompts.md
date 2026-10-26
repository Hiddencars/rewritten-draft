# Промпты под стиль The Coffin of Andy and Leyley

Всё, что нужно, чтобы получить арт «как в игре». Проверено: стиль держится на
плоской заливке, кремовом контуре и одном акцентном цвете глаз.

## 0. Модель и LoRA

- Базовая модель: **Pony XL** (SDXL).
- LoRA: **«the coffin of andy and leyley characters and style»** (есть на SeaArt,
  также ходит по civitai-подобным каталогам).
- Вес LoRA: 0.8–1.0.
- Триггеры стиля: `by nemlei, the coffin of andy and leyley`, `framed`, `bust`.

Порядок промпта: триггеры → стиль → персонаж → поза/кадр.

## 1. База стиля (вставлять в каждый промпт)

```
by nemlei, the coffin of andy and leyley, flat color illustration, dark indie comic,
thick cream outline around the character, pure black hair and clothing fills,
pale cold skin, solid dark background, no shading, no gradients, hard cel-shaded shadows,
huge heavy-lidded eyes, stylized proportions, big head, narrow sharp chin, thin long neck
```

## 2. Женя (18)

```
18 year old boy, long shaggy messy black hair over eyes, glowing pale green irises,
tired blank stare, oversized black hoodie, hands in pockets, bust shot
```

## 3. Рина (18) — по фото, дизайн под Эшли

```
18 year old girl, long straight black hair with heavy blunt fringe covering the forehead,
glowing magenta irises, heavy upper-eyelid line, small mouth, pale skin,
black choker, off-shoulder black top with straps, white lace trim, thin shoulders,
sly smirk, bust shot
```

Вариант причёски «как у Эшли»:

```
high ponytail, black choker, bare shoulders
```

## 4. Кадры

Двое за столом:

```
two characters at a table, thick white outline around both, sepia grey-brown background,
schematic food on the table, flat cel shading
```

Комната:

```
dark apartment interior, sepia and grey-brown palette, schematic furniture,
no people, flat graphic background, rough edges
```

## 5. Негативный промпт

```
photorealistic, 3d render, glossy, gradient shading, soft airbrush, blurry,
extra fingers, deformed hands, watermark, text, signature
```

## 6. Что делать с результатом

1. Выбрать кадр, где лицо и руки не поехали (генерировать по 4–6 штук на позу).
2. Вырезать фон (любой онлайн-ремовер) — фон в игре отдельный.
3. Проверить, что кремовый контур остался по всему силуэту, а не только по волосам.
4. Положить в `game/images/` с именем `<персонаж>_<эмоция>.png`
   (`zhenya_tired.png`, `rina_smug.png`), высота ~2000 px.
5. В сценарии: `show rina smug at pos_right` — код менять не нужно.

## 7. Если стиль «не тот» — что крутить

- Мало контура → `thick cream outline`, `white outline`, `sticker outline`, поднять вес LoRA.
- Появилась живопись → убрать `painterly`, добавить `flat colors`, `no gradients`, `cel shading`.
- Глаза не того цвета → явно `glowing magenta irises` / `glowing green irises` (это главный акцент стиля).
- Пропорции «слишком нормальные» → `big head, small body, stylized proportions`.
