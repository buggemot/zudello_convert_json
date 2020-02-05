#parameter, regex for parameter, regex for value
rule_for_group_parameter = [
    ('array'), # Array of items of the same type
    ('​collection'), #An object
    ]
rule_for_single_parameter = [
    ('uuid', None, '[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}'), #UUID
    ('​email', '(?:e ?\-? ?(?:mail)?)', '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}'), # Allows only a valid email address to be filled in
    ('​url', None, '[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'), #URL address
    ('text', 'string', '[\w\d ]+'),
    ('date', 'date', '(?:(?:date)|[\d\-\:]+)'), #Date or date with time
    ('​uinteger', None, '\b(?:(?:\d{1,3}(?:,\d{1,4})?)+'), #Positive whole number
    ('​integer', None, '([^\d]{,2}?(?:\d{1,3}(?:,\d{1,4})?)+'), #Whole number
    ('​boolean', None, None), # true or false value
    ('​buffer', None, None), # Binary buffer
    ('​cert'), #Certifcate in PEM format
    ('​color'), #Hexadecimal color input
    ('file'), #File selection
    ('filename'), #File name
    ('filter'), #An advanced parameter used for filtering
    ('folder'), #Folder selection
    ('hidden'), #Parameter of this type is hidden from the user
    ('json'), #Allows only a json valid against JSON Schema
    ('number'), #A number
    ('path'), #A path to a file or a folder
    ('pkey'), #Private key in PEM format
    ('port'), #A whole number in range from 1 to 65535
    ('select'), #A selection from predefined values
    ('time'), #Time in hh:mm or hh:mm:ss or hh:mm:ss.nnn format
    ('timestamp'), #Unix timestamp
    ('​timezone'), #Time zone name (e.g. Europe/Prague)
]
