import os
import psutil
from psutil._common import bytes2human

def output_info() -> None:
    """Вывод основной информации

    device: Имя партиции диска
    mountpoint: Точка монтирования — это каталог или файл, c помощью которого
                обеспечивается доступ к новой файловой системе, каталогу или файлу
    fstype: Тип файловой системы
    opts: Различные доступные опции. Зависит от платформы
    """
    templ = "%-17s %8s %8s %8s %5s%%  %13s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=True):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # пропускаем приводы cd-rom, в которых нет диска;
                # они могут вызвать ошибку графического интерфейса
                # Windows для неготового раздела или просто зависнуть
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))

