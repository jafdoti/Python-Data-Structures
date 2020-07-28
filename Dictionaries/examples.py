# Dictionary Structure
contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}

# Value Lookup
# In order to find a phone number in the contact list, 
# you simply index into the dictionary with the name you want to look up:
def lookup(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    if name in contacts:
        return contacts[name]
    else:
        return ""
    
def lookup2(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    return contacts.get(name, "")

# Iteration
def print_contacts(contacts):
    """
    Print the names of the contacts in our contacts list.
    """
    for name in contacts:
        print(name)
        

print_contacts(contacts)

def print_contact_list(contacts):
    """
    Print the names and phone numbers of the contacts in
    our contacts list.
    """
    for name, number in contacts.items():
        print(name, ":", number)
        
print_contact_list(contacts)  

def print_ordered(contacts):
    """
    Print the names and phone numbers of the contacts
    in our contacts list in alphabetical order.
    """
    keys = contacts.keys()
    names = sorted(keys)
    for name in names:
        print(name, ":", contacts[name])
        
print_ordered(contacts)    


# Updates
def add_contact(contacts, name, number):
    """
    Add a new contact (name, number) to the contacts list.
    """
    if name in contacts:
        print(name, "is already in contacts list!")
    else:
        contacts[name] = number

        
def update_contact(contacts, name, newnumber):
    """
    Update an existing contact's number in the contacts list.
    """
    if name in contacts:
        contacts[name] = newnumber
    else:
        print(name, "is not in contacts list!")


def add_or_update_contact(contacts, name, number):
    """
    Add contact or update it if it is already in the contacts list.
    """
    contacts[name] = number