#parameter, regex for key, regex for value
rule_for_group_parameter = [
    ("array"), # Array of items of the same type
    ("​collection"), #An object
    ]
rule_for_single_parameter = [
    ("uuid", "id", "[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}"), #UUID
    ("date", "(date|time)", "(?i)(?:.*date\(\d{13}\+\d{4}\).*)|(?:\d{2,4}[^\d]\d{1,2}[^\d]\d{2,4}(?:t)?(?:\d{2,4}[^\d]\d{1,2}[^\d]\d{2,4})?(?:[^\d]?\d{1,2}[^\d])?)"), #Date or date with time
    ("email", "mail", "[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"), # Allows only a valid email address to be filled in
    ("number", None, "[-\s]*(?:(?:\d{1,3}(?:,\d{1,3})?)+(?:\.\d+))"), #A number
    ("uinteger", None, "(?<!-|\d)(?:(?:\d{1,3}(?:,\d{1,3})?)+)"), #Positive whole number
    ("url", None, "\b(?:http://)?(?:www\.)[a-z0-9][-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"), #URL address
    ("integer", None, "[-\s]*(?:(?:\d{1,3}(?:,\d{1,3})?)+)"), #Whole number
    ("boolean", None, "(?:false|true)"), # true or false value
    ("text", "string", "((\S+ ?)+)"),
    ("buffer", None, None), # Binary buffer
    ("cert", None, None), #Certifcate in PEM format
    ("color", None, None), #Hexadecimal color input
    ("file", None, None), #File selection
    ("filename", None, None), #File name
    ("filter", None, None), #An advanced parameter used for filtering
    ("folder", None, None), #Folder selection
    ("hidden", None, None), #Parameter of this type is hidden from the user
    ("json", None, None), #Allows only a json valid against JSON Schema
    ("path", None, None), #A path to a file or a folder
    ("pkey", None, None), #Private key in PEM format
    ("port", None, None), #A whole number in range from 1 to 65535
    ("select", None, None), #A selection from predefined values
    ("time", None, None), #Time in hh:mm or hh:mm:ss or hh:mm:ss.nnn format
    ("timestamp", None, None), #Unix timestamp
    ("timezone", None, None), #Time zone name (e.g. Europe/Prague)
]
