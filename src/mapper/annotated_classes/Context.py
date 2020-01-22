# Since Context is defined as a static object, the following values are implemented
# as constants

VERSION = 1.1                   # @version
BASE = "http://ew-shopp.eu/"    # @base
SCHEMA = "http://schema.org/"   # schema
EWS = "http://ew-shopp.eu/ontology/"      # ews (EW-Shopp ontology)
EWSR = "http://ew-shopp.eu/data/rdf"        # ewsr
XSD = "http://www.w3.org/2001/XMLSchema#"   # xsd
LANG = "@language"              # language
TEXT = "@value"                 # text
IDENTIFIER = "@id"              # identifier
EVENT_ARRAY = {
    "@id": "ews:eventArray",
    "@type": "@id",
    "@container": "@set",
    "@context": {
        "@base": "/rdf/event/"
    }
}
NAME = {
    "@id": "schema:name",
    "@language": "en"
}
DESCRIPTION = {
    "@id": "schema:description",
    "@language": "en"
}
SOURCE = {
    "@id": "ews:source",
    "@language": "en"
}
CHANNEL_CODE = {
    "@id": "ews:channelCode",
    "@language": "en"
}
CHANNEL_DESCR = {
    "@id": "ews:channelDescription",
    "@language": "en"
}
START_DATE = {
    "@id": "schema:startDate",
    "@type": "xsd:dateTime"
}
END_DATE = {
    "@id": "schema:endDate",
    "@type": "xsd:dateTime"
}
CATEGORY = {
    "@id": "schema:category",
    "@type": "@id"
}
PRODUCT = {
    "@id": "ews:product",
    "@type": "@id" 
}
GTIN13 = {
    "@id": "schema:gtin13"
}
SELLER = {
    "@id": "schema:seller",
    "@type": "@id",
    "@context": {
        "@base": "/rdf/seller/"
    }
}
SKU = {
    "@id": "schema:sku"
}
CATALOG_ID = {
    "@id": "ews:catalogId"
}
MEASURE = {
    "@id": "ews:measure"
}
QUANTITY = {
    "@id": "ews:quantity",
    "@type": "xsd:integer"
}
QUANTITY_UNIT_ID = {
    "@id": "ews:quantityUnitId",
    "@type": "@id",
    "@context": {
        "@base": "/rdf/quantityUnitId/"
    }
}
INTERESTED_AUDIENCE = {
    "@id": "ews:interestedAudience",
    "@type": "xsd:integer"
}
ATTENDING_AUDIENCE = {
    "@id": "ews:attendingAudience",
    "@type": "xsd:integer"
}
PRICE_CHANGED = {
    "@id": "ews:priceChanged",
    "@type": "xsd:boolean"
}
PRICE_CHANGE = {
    "@id": "ews:priceChange",
    "@type": "xsd:float"
}
DISCOUNT = {
    "@id": "schema:discount",
    "@type": "xsd:integer"
}
LOCATION = {
    "@id": "schema:location",
    "@language": "en"
}
ADDRESS_LOCALITY = {
    "@id": "schema:addressLocality",
    "@language": "en"
}
ADDRESS_COUNTRY = {
    "@id": "schema:addressCountry",
    "@language": "en"
}
ADDRESS_REGION = {
    "@id": "schema:addressRegion",
    "@language": "en"
}
STREET_ADDRESS = {
    "@id": "schema:streetAddress",
    "@language": "en"
}
POSTAL_CODE = {
    "@id": "schema:postalCode",
    "@language": "en"
}
LATITUDE = {
    "@id": "schema:latitude",
    "@type": "xsd:double"
}
LONGITUDE = {
    "@id": "schema:longitude",
    "@type": "xsd:double"
}
ADDRESS = {
    "@id": "schema:address",
    "@type": "@id"
}

class Context:
    def __init__(self):
        self._version = VERSION
        self._base = BASE
        self._schema = SCHEMA
        self._ews = EWS
        self._ewsr = EWSR
        self._lang = LANG
        self._text = TEXT
        self._identifier = IDENTIFIER
        self._eventArray = EVENT_ARRAY
        self._name = NAME
        self._description = DESCRIPTION
        self._source = SOURCE
        self._channelCode = CHANNEL_CODE
        self._channelDescr = CHANNEL_DESCR
        self._startDate = START_DATE
        self._endDate = END_DATE
        self._category = CATEGORY
        self._product = PRODUCT
        self._gtin13 = GTIN13  
        self._seller = SELLER
        self._sku = SKU
        self._catalogId = CATALOG_ID
        self._measure = MEASURE
        self._quantity = QUANTITY
        self._quantityUnitId = QUANTITY_UNIT_ID
        self._interestedAudience = INTERESTED_AUDIENCE
        self._attendingAudience = ATTENDING_AUDIENCE
        self._priceChanged = PRICE_CHANGED
        self._priceChange = PRICE_CHANGE
        self._discount = DISCOUNT
        self._location = LOCATION
        self._addressLocality = ADDRESS_LOCALITY
        self._addressCountry = ADDRESS_COUNTRY
        self._addressRegion = ADDRESS_REGION
        self._streetAddress = STREET_ADDRESS
        self._postalCode = POSTAL_CODE
        self._latitude = LATITUDE
        self._longitude = LONGITUDE
        self._address = ADDRESS

    def get_version(self):
        return self._version
    
    def get_base(self):
        return self._base
    
    def get_schema(self):
        return self._schema
    
    def get_ews(self):
        return self._ews
    
    def get_ewsr(self):
        return self._ewsr
    
    def get_lang(self):
        return self._lang
    
    def get_text(self):
        return self._text
    
    def get_identifier(self):
        return self._identifier
    
    def get_eventArray(self):
        return self._eventArray
    
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
    
    def get_source(self):
        return self._source
    
    def get_channelCode(self):
        return self._channelCode
    
    def get_channelDescr(self):
        return self._channelDescr
    
    def get_startDate(self):
        return self._startDate
    
    def get_endDate(self):
        return self._endDate
    
    def get_category(self):
        return self._category
    
    def get_product(self):
        return self._product
    
    def get_gtin13(self):
        return self._gtin13
    
    def get_seller(self):
        return self._seller
    
    def get_sku(self):
        return self._sku
    
    def get_catalogId(self):
        return self._catalogId
    
    def get_measure(self):
        return self._measure
    
    def get_quantity(self):
        return self._quantity
    
    def get_quantityUnitId(self):
        return self._quantityUnitId
    
    def get_interestedAudience(self):
        return self._interestedAudience
    
    def get_attendingAudience(self):
        return self._attendingAudience
    
    def get_priceChanged(self):
        return self._priceChanged
    
    def get_priceChange(self):
        return self._priceChange
    
    def get_discount(self):
        return self._discount
    
    def get_location(self):
        return self._location
    
    def get_addressLocality(self):
        return self._addressLocality
    
    def get_addressCountry(self):
        return self._addressCountry
    
    def get_addressRegion(self):
        return self._addressRegion
    
    def get_streetAddress(self):
        return self._streetAddress
    
    def get_postalCode(self):
        return self._postalCode
    
    def get_latitude(self):
        return self._latitude
    
    def get_longitude(self):
        return self._longitude
    
    def get_address(self):
        return self._address
    
    def repr(self):
        cntxt_repr = {
            "@version": self.get_version(),
            "@base": self.get_base(),
            "schema": self.get_schema(),
            "ews": self.get_ews(),
            "ewsr": self.get_ewsr(),
            "lang": self.get_lang(),
            "text": self.get_text(),
            "identifier": self.get_identifier(),
            "eventArray": self.get_eventArray(),
            "name": self.get_name(),
            "description": self.get_description(),
            "source": self.get_source(),
            "channelCode": self.get_channelCode(),
            "channelDescription": self.get_channelDescr(),
            "startDate": self.get_startDate(),
            "endDate": self.get_endDate(),
            "category": self.get_category(),
            "product": self.get_product(),
            "gtin13": self.get_gtin13(),
            "seller": self.get_seller(),
            "sku": self.get_sku(),
            "catalogId": self.get_catalogId(),
            "measure": self.get_measure(),
            "quantity": self.get_quantity(),
            "quantityUnitId": self.get_quantityUnitId(),
            "interestedAudience": self.get_interestedAudience(),
            "attendingAudience": self.get_attendingAudience(),
            "priceChanged": self.get_priceChanged(),
            "discount": self.get_discount(),
            "location": self.get_location(),
            "addressLocality": self.get_addressLocality(),
            "addressCountry": self.get_addressCountry(),
            "addressRegion": self.get_addressRegion(),
            "streetAddress": self.get_streetAddress(),
            "postalCode": self.get_postalCode(),
            "latitude": self.get_latitude(),
            "longitude": self.get_longitude(),
            "address": self.get_address()
        }

        return cntxt_repr