from django.db import models
from rdflib import Graph


class RDFStore:
    g = Graph()
    g.parse("data/data.nt", format="nt")


store = RDFStore()


class Contract:
    store.


class ContractManager:
    pass
