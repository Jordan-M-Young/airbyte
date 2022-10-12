ATTENDS_KEY = "attends"

BODY_KEY = "body"

CALENDAR_EVENT_JSON_KEY = "calendar_event_data.json"
CONTAINS_KEY = "contains"

DATA_KEY = "data"
DATABOOK_KEY = "databook"
DATE_KEY = "date"

GMAIL_THREAD_JSON_KEY = "gmail_thread_data.json"
GMAIL_MESSAGE_JSON_KEY = "gmail_message_data.json"

EMAIL_KEY = "email"
EMAIL_DOMAIN = "@trydatabook.com"

FROM_KEY = "from"

HAS_PARTICIPANT_KEY = "has_participant"
HEADERS_KEY = "headers"

ID_KEY = "id"
IN_RESPONSE_TO_KEY = "in_response_to"
ITEMS_KEY = "items"

MEETS_WITH_KEY = "plans_meeting_with"
MEETING_KEY = "meeting"
MESSAGE_KEY = "message"
MESSAGES_KEY = "messages"

NAME_KEY = "name"
NEXT_PAGE_TOKEN_KEY = "nextPageToken"
NEWER_THAN_KEY = "newer_than:"
NUMBER_TIME_UNITS = "1"
OR_OPERATOR = " OR "

EMAIL_EXTRACT_REGEXES = [r"<[^>]*>", r"[\w.+-]+@[\w-]+\.[\w.-]+"]

GMAIL_OBJECT_ACCESS_PATHS = []

PARTS_KEY = "parts"
PAYLOAD_KEY = "payload"
PERSON_KEY = "person"

PEOPLE_INDEX_JSON_KEY = "people_index.json"

RECEIVED_BY_KEY = "received_by"

SUBJECT_KEY = "subject"
SUMMARY_KEY = "summary"

TEXT_KEY = "text"
THREAD_KEY = "thread"
THREADS_KEY = "threads"
TIME_UNIT = "m"
TO_KEY = "to"

VALUE_KEY = "value"

WRITES_TO_KEY = "writes_to"
WRITTEN_BY_KEY = "written_by"


GMAIL_OBJECT_ACCESS_PATHS = [
    f"{PARTS_KEY}.{0}.{BODY_KEY}.{DATA_KEY}",
    f"{PARTS_KEY}.{0}.{PARTS_KEY}.{0}.{BODY_KEY}.{DATA_KEY}",
    f"{PARTS_KEY}.{0}.{PARTS_KEY}.{0}.{PARTS_KEY}.{0}.{BODY_KEY}.{DATA_KEY}",
    f"{BODY_KEY}.{DATA_KEY}",
]