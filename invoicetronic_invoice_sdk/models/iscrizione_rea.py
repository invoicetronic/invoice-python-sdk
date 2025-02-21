# coding: utf-8

"""
    Italian eInvoice API v1

    The [Italian eInvoice API][2] is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. The API also provides advanced features as encryption at rest, invoice validation, multiple upload formats, webhooks, event logging, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class IscrizioneREA(BaseModel):
    """
    IscrizioneREA
    """ # noqa: E501
    ufficio: Optional[StrictStr] = None
    numero_rea: Optional[StrictStr] = None
    capitale_sociale: Optional[Union[StrictFloat, StrictInt]] = None
    socio_unico: Optional[StrictStr] = None
    stato_liquidazione: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["ufficio", "numero_rea", "capitale_sociale", "socio_unico", "stato_liquidazione"]

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
        """Create an instance of IscrizioneREA from a JSON string"""
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
        # set to None if ufficio (nullable) is None
        # and model_fields_set contains the field
        if self.ufficio is None and "ufficio" in self.model_fields_set:
            _dict['ufficio'] = None

        # set to None if numero_rea (nullable) is None
        # and model_fields_set contains the field
        if self.numero_rea is None and "numero_rea" in self.model_fields_set:
            _dict['numero_rea'] = None

        # set to None if capitale_sociale (nullable) is None
        # and model_fields_set contains the field
        if self.capitale_sociale is None and "capitale_sociale" in self.model_fields_set:
            _dict['capitale_sociale'] = None

        # set to None if socio_unico (nullable) is None
        # and model_fields_set contains the field
        if self.socio_unico is None and "socio_unico" in self.model_fields_set:
            _dict['socio_unico'] = None

        # set to None if stato_liquidazione (nullable) is None
        # and model_fields_set contains the field
        if self.stato_liquidazione is None and "stato_liquidazione" in self.model_fields_set:
            _dict['stato_liquidazione'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IscrizioneREA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ufficio": obj.get("ufficio"),
            "numero_rea": obj.get("numero_rea"),
            "capitale_sociale": obj.get("capitale_sociale"),
            "socio_unico": obj.get("socio_unico"),
            "stato_liquidazione": obj.get("stato_liquidazione")
        })
        return _obj


