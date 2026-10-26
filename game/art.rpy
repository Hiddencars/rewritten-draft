# ===========================================================
#  Спрайты: автоподстановка.
#  Положи PNG в game/images/ с нужным именем — игра подхватит
#  его сама. Нет файла — показывается цветная заглушка.
#
#  Имена файлов:
#    rina_idle.png    rina_sweet.png  rina_smug.png
#    rina_cold.png    rina_hurt.png   rina_rage.png
#    zhenya_idle.png  zhenya_tired.png zhenya_smirk.png
#    zhenya_annoyed.png zhenya_hurt.png
#
#  Требования: PNG с прозрачностью, высота ~2000 px,
#  персонаж по бедро или в полный рост, кремовый контур по силуэту.
# ===========================================================

init -1 python:
    import os

    def sprite(path, fallback):
        if os.path.exists(os.path.join(config.gamedir, path)):
            return path
        return fallback

    def _ph(color):
        return Transform(Solid(color), xysize=(520, 860))

    PH_RINA = "#2b2030"
    PH_ZHENYA = "#1b2028"

# --- Рина
image rina idle    = sprite("images/rina_idle.png",    _ph(PH_RINA))
image rina sweet   = sprite("images/rina_sweet.png",   _ph(PH_RINA))
image rina smug    = sprite("images/rina_smug.png",    _ph(PH_RINA))
image rina cold    = sprite("images/rina_cold.png",    _ph(PH_RINA))
image rina hurt    = sprite("images/rina_hurt.png",    _ph(PH_RINA))
image rina rage    = sprite("images/rina_rage.png",    _ph(PH_RINA))

# --- Женя
image zhenya idle    = sprite("images/zhenya_idle.png",    _ph(PH_ZHENYA))
image zhenya tired   = sprite("images/zhenya_tired.png",   _ph(PH_ZHENYA))
image zhenya smirk   = sprite("images/zhenya_smirk.png",   _ph(PH_ZHENYA))
image zhenya annoyed = sprite("images/zhenya_annoyed.png", _ph(PH_ZHENYA))
image zhenya hurt    = sprite("images/zhenya_hurt.png",    _ph(PH_ZHENYA))

# --- позиции: спрайт нормализуется по высоте, пропорции сохраняются
transform pos_left:
    xalign 0.18
    yalign 1.0
    zoom 1.0

transform pos_right:
    xalign 0.82
    yalign 1.0
    zoom 1.0
