
from datetime import timedelta
import csv
import json
import source_google_calendar.constants as K
from googleapiclient.discovery import build

def load_json(filepath):
    with open(filepath, "r") as jfile:
        return json.load(jfile)


def write_json(filepath, data):
    with open(filepath, "w") as jfile:
        json.dump(data, jfile)


def replace_month(now, current_month, target_month):
    return now.replace(f"-{current_month}-", f"-{target_month}-")


def replace_year(now, current_year, target_year):
    return now.replace(f"{current_year}-", f"{target_year}-")


def get_past_future_month(now, periods=1):
    """Function used to get preceding and proceding timestamps
    that are exactly n months behind and ahead of the timestamp
    specified in the argument 'now'
    """
    # number of month times 30 days
    days = periods * 30
    delta = timedelta(days=days)

    return (now - delta).isoformat() + "Z", (now + delta).isoformat() + "Z"


def write_csv(filepath, data, delimiter=","):

    with open(filepath, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


def record_attendee_data(
    event,
    event_data
):

    """takes event data and generates triples using the collected data and adds
    an event entry to the event_data object
    """
    


    event_data[event[K.ID_KEY]] = event





def record_data(
    event,
    event_data,

):
    # adds event to triples list and  to event_data dictionary


    record_attendee_data(
        event,
        event_data
    )


def record_check(
    event,
    event_data,
    company,
    email
):

    """checks to see if target company is a substring of the passed
    email address, if so then data is recorded data indices  described in record_data()
    and record_attendee_data()
    """



    if company in email:
        record_data(
            event,
            event_data

        )





def extract_event_data(event, event_data, target_companies):

    # get event organizer, attendee and summary if they exist
    organizer = event.get("organizer")
    attendees = event.get("attendees")

    # runs the following code if an organizer exists
    if organizer:
        organizer_email = organizer.get('email')
        # only want calendar events where multiple people attended
        if attendees:

            # iterates  through list of attendees
            for attendee in attendees:
                # iterates through company list
                attendee_email = attendee.get('email')
                for company in target_companies:

                    # checks if a databook employee is the organizer
                    if K.DATABOOK_KEY in organizer:
                        record_check(
                            event,
                            event_data,
                            company,
                            attendee_email
                        )

                    # get events where db employee was an attendee of a meeting
                    else:
                        record_check(
                            event,
                            event_data,
                            company,
                            organizer_email
                        )


def get_events(service, subject, lower_bound, upper_bound, pageToken=None):
    events_result = (
        service.events()
        .list(
            calendarId=subject,  # account in question
            timeMin=lower_bound,  # lower temporal search bound
            timeMax=upper_bound,  # higher temporal search bound
            maxResults=None,
            pageToken=pageToken  # max results to surface
            # singleEvents=False,  # expand recurring events to instances of single events? True = yes
            # orderBy="startTime",  # How to order events?
        )
        .execute()
    )

    # gets actual event data
    events = events_result.get(K.ITEMS_KEY, [])

    pageToken = events_result.get(K.NEXT_PAGE_TOKEN_KEY)

    return events, pageToken


def extract_calendar(
    subject,
    credentials,
    event_data,
    target_companies,
    lower_bound,
    upper_bound
):
    subject = f"{subject}{K.EMAIL_DOMAIN}"

    # gets specific credentials for a given account
    delegated_credentials = credentials.with_subject(subject)

    # builds the calendar client
    service = build("calendar", "v3", credentials=delegated_credentials)

    # gets a list of events\ ids from the account's calendar based on passed arguments
    events, pageToken = get_events(service, subject, lower_bound, upper_bound)

    # iterates through list of event data
    for event in events:
        extract_event_data(
            event, event_data, target_companies
        )
    print(pageToken)
    while pageToken:
        events, pageToken = get_events(
            service, subject, lower_bound, upper_bound, pageToken=pageToken
        )
        print(pageToken)

        # iterates through list of event data
        for event in events:
            extract_event_data(
                event, event_data, target_companies
            )