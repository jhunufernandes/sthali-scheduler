from sthali_scheduler import AppSpecification, SthaliScheduler
from spec import SPEC


client = SthaliScheduler(AppSpecification(**SPEC))
app = client.app
