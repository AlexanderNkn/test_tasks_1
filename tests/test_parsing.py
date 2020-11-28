import datetime as dt
import os
import sys

from freezegun import freeze_time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parsing import parsing_python_org_upcoming_events as upcoming  # noqa


@freeze_time("2020-05-14")
def test_parsing_date():
    html_doc = """
    <div class="shrubbery">
    <h2>Upcoming Events</h2>
    <ul>
    <li>
    <time datetime="2020-04-05T00:00:00+00:00"></time>
    <a href="/events/python-events/992/">PyDay Chile 2020</a></li>
    <li>
    <time datetime="2020-05-11T00:00:00+00:00"></time>
    <a href="/events/python-events/996/">PyCode Conference 2020</a></li>
    <li>
    <time datetime="2020-06-12T06:00:00+00:00"></time>
    <a href="/events/python-user-group/993/">Python Mauritius User</a></li>
    <li>
    <time datetime="2020-07-14T00:00:00+00:00"></time>
    <a href="/events/python-events/990/">PyCon Tanzania 2020</a></li>
    </ul>
    </div>
    """
    events = upcoming(html_doc)
    for event in events:
        date, event_name = event
        assert date in (dt.date(2020, 5, 11), dt.date(2020, 6, 12))
        assert event_name in ('PyCode Conference 2020',
                              'Python Mauritius User')
