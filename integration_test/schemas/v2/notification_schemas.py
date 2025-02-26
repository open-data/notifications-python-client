from integration_test.schemas.v2.definitions import personalisation, uuid

template = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "template schema",
    "type": "object",
    "title": "notification content",
    "properties": {
        "id": uuid,
        "version": {"type": "integer"},
        "uri": {"type": "string"}
    },
    "required": ["id", "version", "uri"]
}

get_notification_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "GET notification response schema",
    "type": "object",
    "title": "response v2/notification",
    "properties": {
        "id": uuid,
        "reference": {"type": ["string", "null"]},
        "email_address": {"type": ["string", "null"]},
        "phone_number": {"type": ["string", "null"]},
        "line_1": {"type": ["string", "null"]},
        "line_2": {"type": ["string", "null"]},
        "line_3": {"type": ["string", "null"]},
        "line_4": {"type": ["string", "null"]},
        "line_5": {"type": ["string", "null"]},
        "line_6": {"type": ["string", "null"]},
        "postcode": {"type": ["string", "null"]},
        "postage": {"enum": ["first", "second", None]},
        "type": {"enum": ["sms", "letter", "email"]},
        "status": {"type": "string"},
        "template": template,
        "body": {"type": "string"},
        "subject": {"type": ["string", "null"]},
        "created_at": {"type": "string"},
        "sent_at": {"type": ["string", "null"]},
        "completed_at": {"type": ["string", "null"]},
        "created_by_name": {"type": ["string", "null"]}
    },
    "required": [
        # technically, all keys are required since we always have all of them
        "id", "reference", "email_address", "phone_number",
        "line_1", "line_2", "line_3", "line_4", "line_5", "line_6", "postcode",
        "type", "status", "template", "body", "created_at", "sent_at", "completed_at"
    ]
}

get_notifications_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "GET list of notifications response schema",
    "type": "object",
    "properties": {
        "notifications": {
            "type": "array",
            "items": {
                "type": "object",
                "ref": get_notification_response
            }
        },
        "links": {
            "type": "object",
            "properties": {
                "current": {
                    "type": "string"
                },
                "next": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": ["current"]
        }
    },
    "additionalProperties": False,
    "required": ["notifications", "links"]
}

post_sms_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST sms notification schema",
    "type": "object",
    "title": "POST v2/notifications/sms",
    "properties": {
        "reference": {"type": "string"},
        "phone_number": {"type": "string", "format": "phone_number"},
        "template_id": uuid,
        "sms_sender_id": uuid,
        "personalisation": personalisation
    },
    "required": ["phone_number", "template_id"]
}

sms_content = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "content schema for SMS notification response schema",
    "type": "object",
    "title": "notification content",
    "properties": {
        "body": {"type": "string"},
        "from_number": {"type": ["string", "null"]}
    },
    "required": ["body"]
}

post_sms_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST sms notification response schema",
    "type": "object",
    "title": "response v2/notifications/sms",
    "properties": {
        "id": uuid,
        "reference": {"type": ["string", "null"]},
        "content": sms_content,
        "uri": {"type": "string"},
        "template": template
    },
    "required": ["id", "content", "uri", "template"]
}

post_email_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST email notification schema",
    "type": "object",
    "title": "POST v2/notifications/email",
    "properties": {
        "reference": {"type": "string"},
        "email_address": {"type": "string", "format": "email_address"},
        "template_id": uuid,
        "email_reply_to_id": uuid,
        "personalisation": personalisation
    },
    "required": ["email_address", "template_id"]
}

email_content = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Email content for POST email notification",
    "type": "object",
    "title": "notification email content",
    "properties": {
        "from_email": {"type": "string", "format": "email_address"},
        "body": {"type": "string"},
        "subject": {"type": "string"}
    },
    "required": ["body", "from_email", "subject"]
}

post_email_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST email notification response schema",
    "type": "object",
    "title": "response v2/notifications/email",
    "properties": {
        "id": uuid,
        "reference": {"type": ["string", "null"]},
        "content": email_content,
        "uri": {"type": "string"},
        "template": template
    },
    "required": ["id", "content", "uri", "template"]
}

post_letter_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST letter notification schema",
    "type": "object",
    "title": "POST v2/notifications/letter",
    "properties": {
        "reference": {"type": "string"},
        "template_id": uuid,
        "personalisation": personalisation
    },
    "required": ["letter_address", "template_id"]
}

letter_content = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Letter content for POST letter notification",
    "type": "object",
    "title": "notification letter content",
    "properties": {
        "body": {"type": ["string", "null"]},
        "subject": {"type": "string"}
    },
    "required": ["body", "subject"]
}

post_letter_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST letter notification response schema",
    "type": "object",
    "title": "response v2/notifications/letter",
    "properties": {
        "id": uuid,
        "reference": {"type": ["string", "null"]},
        "content": letter_content,
        "uri": {"type": "string"},
        "template": template
    },
    "required": ["id", "content", "uri", "template"]
}

post_precompiled_letter_response = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "POST letter notification response schema",
    "type": "object",
    "title": "response v2/notifications/letter",
    "properties": {
        "id": uuid,
        "reference": {"type": ["string", "null"]},
        "postage": {"enum": ["first", "second", None]}
    },
    "required": ["id", "reference"]
}


def create_post_sms_response_from_notification(notification, body, from_number, url_root):
    return {"id": notification.id,
            "reference": notification.client_reference,
            "content": {'body': body,
                        'from_number': from_number},
            "uri": "{}/v2/notifications/{}".format(url_root, str(notification.id)),
            "template": __create_template_from_notification(notification=notification, url_root=url_root)
            }


def create_post_email_response_from_notification(notification, content, subject, email_from, url_root):
    return {
        "id": notification.id,
        "reference": notification.client_reference,
        "content": {
            "from_email": email_from,
            "body": content,
            "subject": subject
        },
        "uri": "{}/v2/notifications/{}".format(url_root, str(notification.id)),
        "template": __create_template_from_notification(notification=notification, url_root=url_root)
    }


def __create_template_from_notification(notification, url_root):
    return {
        "id": notification.template_id,
        "version": notification.template_version,
        "uri": "{}/v2/templates/{}".format(url_root, str(notification.template_id))
    }
