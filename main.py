import time

from gleifpy.config import settings
from gleifpy.db import get_db_session
from gleifpy.models import ForeignCompany
from gleifpy.reader import gleif_data

if __name__ == "__main__":
    _start = time.time()

    with get_db_session() as session:
        batch = []
        batch_time_start = time.time()
        for idx, company in enumerate(gleif_data('gle.xml')):
            db_obj = ForeignCompany(**company.dict())
            batch.append(db_obj)
            # print(idx)
            if len(batch) == settings.BATCH_SIZE:
                session.bulk_save_objects(batch)
                session.commit()
                batch.clear()

                batch_time_end = time.time()
                print(f'Batch size={idx + 1} inserted. Time={batch_time_end - batch_time_start}')
                batch_time_start = time.time()

    _end = time.time()
    print(f'Full time={_end - _start}')
