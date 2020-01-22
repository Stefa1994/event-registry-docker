from annotated_classes.Place import Place

TYPE = "ews:Event"

class Event:
    def __init__(self,er_event):
        self._type = TYPE
        self._identifier = er_event["uri"]

        if "eng" in er_event["title"]:
            self._name = er_event["title"]["eng"]
        else:
            self._name = None
        
        if "eng" in er_event["summary"]:
            self._description = er_event["summary"]["eng"]
        else:
            self._description = None
        
        self._location = Place(er_event["location"])

    def get_type(self):
        return self._type
    
    def get_identifier(self):
        return self._identifier
    
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
    
    def get_location(self):
        return self._location

    def repr(self):
        evnt_repr = {
            "@type": self.get_type(),
            "identifier": self.get_identifier(),
            "name": self.get_name(),
            "description": self.get_description(),
            "location": self.get_location().repr()
        }

        return evnt_repr