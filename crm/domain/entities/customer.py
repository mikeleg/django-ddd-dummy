from dataclasses import dataclass
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    name = str
    surname = str
    phone = str
    email = str
    date_created = datetime
    date_modified = datetime

    def convert_from_model(self, customer_model):
        self.name = customer_model.name
        self.surname = customer_model.surname
        self.phone = customer_model.phone
        self.email = customer_model.email
        self.date_created = customer_model.date_created
        self.date_modified = customer_model.date_modified

        return self
