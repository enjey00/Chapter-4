class ContactList(list):
    def __init__(self, *all_):
        self.all_ = all_

    def search_by_name(self, name):
        for a in self.all_:
            if a in name:
                print(a)

all_contacts = ContactList('Zhenishbek', 'Altynbek', 'Orozobek')
all_contacts.search_by_name('Orozobek')


