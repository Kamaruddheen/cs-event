import datetime
import exiftool


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def meta_data(image):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata()
    Time = metadata['File:FileModifyDate'].split('+')
    date, time = Time[0][:10], Time[0][11:]
    time = time.split(':')
    # Likewise for date too
    start = datetime.time(12, 0, 0)
    end = datetime.time(13, 0, 0)
    status = time_in_range(start, end, datetime.time(
        int(time[0]), int(time[1]), int(time[2])))
    return status
