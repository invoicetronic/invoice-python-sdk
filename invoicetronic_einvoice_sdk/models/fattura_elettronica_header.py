# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1] (Interchange Service). The API is designed by Invoicetronic to be simple and easy to use, abstracting away the Interchange Service's complexity while still providing complete control over the invoice send/receive process. The API also provides advanced features and a rich toolchain, such as invoice validation, multiple upload methods, webhooks, event logs, CORS support, client SDKs for commonly used languages, and CLI tools.  For more information, see:  - [Invoicetronic website][2] - [Invoice API reference][3]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/ [3]: https://api.invoicetronic.com/invoice/v1/docs 

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from invoicetronic_einvoice_sdk.models.cedente_prestatore import CedentePrestatore
from invoicetronic_einvoice_sdk.models.cessionario_committente import CessionarioCommittente
from invoicetronic_einvoice_sdk.models.dati_trasmissione import DatiTrasmissione
from invoicetronic_einvoice_sdk.models.rappresentante_fiscale import RappresentanteFiscale
from invoicetronic_einvoice_sdk.models.terzo_intermediario_o_soggetto_emittente import TerzoIntermediarioOSoggettoEmittente
from typing import Optional, Set
from typing_extensions import Self

class FatturaElettronicaHeader(BaseModel):
    """
    FatturaElettronicaHeader
    """ # noqa: E501
    dati_trasmissione: Optional[DatiTrasmissione] = None
    cedente_prestatore: Optional[CedentePrestatore] = None
    rappresentante_fiscale: Optional[RappresentanteFiscale] = Field(default=None, alias="RappresentanteFiscale")
    cessionario_committente: Optional[CessionarioCommittente] = None
    terzo_intermediario_o_soggetto_emittente: Optional[TerzoIntermediarioOSoggettoEmittente] = None
    soggetto_emittente: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dati_trasmissione", "cedente_prestatore", "RappresentanteFiscale", "cessionario_committente", "terzo_intermediario_o_soggetto_emittente", "soggetto_emittente"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FatturaElettronicaHeader from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dati_trasmissione
        if self.dati_trasmissione:
            _dict['dati_trasmissione'] = self.dati_trasmissione.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cedente_prestatore
        if self.cedente_prestatore:
            _dict['cedente_prestatore'] = self.cedente_prestatore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rappresentante_fiscale
        if self.rappresentante_fiscale:
            _dict['RappresentanteFiscale'] = self.rappresentante_fiscale.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cessionario_committente
        if self.cessionario_committente:
            _dict['cessionario_committente'] = self.cessionario_committente.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terzo_intermediario_o_soggetto_emittente
        if self.terzo_intermediario_o_soggetto_emittente:
            _dict['terzo_intermediario_o_soggetto_emittente'] = self.terzo_intermediario_o_soggetto_emittente.to_dict()
        # set to None if soggetto_emittente (nullable) is None
        # and model_fields_set contains the field
        if self.soggetto_emittente is None and "soggetto_emittente" in self.model_fields_set:
            _dict['soggetto_emittente'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FatturaElettronicaHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dati_trasmissione": DatiTrasmissione.from_dict(obj["dati_trasmissione"]) if obj.get("dati_trasmissione") is not None else None,
            "cedente_prestatore": CedentePrestatore.from_dict(obj["cedente_prestatore"]) if obj.get("cedente_prestatore") is not None else None,
            "RappresentanteFiscale": RappresentanteFiscale.from_dict(obj["RappresentanteFiscale"]) if obj.get("RappresentanteFiscale") is not None else None,
            "cessionario_committente": CessionarioCommittente.from_dict(obj["cessionario_committente"]) if obj.get("cessionario_committente") is not None else None,
            "terzo_intermediario_o_soggetto_emittente": TerzoIntermediarioOSoggettoEmittente.from_dict(obj["terzo_intermediario_o_soggetto_emittente"]) if obj.get("terzo_intermediario_o_soggetto_emittente") is not None else None,
            "soggetto_emittente": obj.get("soggetto_emittente")
        })
        return _obj


