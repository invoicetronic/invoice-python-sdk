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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AltriDatiGestionali(BaseModel):
    """
    AltriDatiGestionali
    """ # noqa: E501
    tipo_dato: Optional[StrictStr] = None
    riferimento_testo: Optional[StrictStr] = None
    riferimento_numero: Optional[Union[StrictFloat, StrictInt]] = None
    riferimento_data: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["tipo_dato", "riferimento_testo", "riferimento_numero", "riferimento_data"]

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
        """Create an instance of AltriDatiGestionali from a JSON string"""
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
        # set to None if tipo_dato (nullable) is None
        # and model_fields_set contains the field
        if self.tipo_dato is None and "tipo_dato" in self.model_fields_set:
            _dict['tipo_dato'] = None

        # set to None if riferimento_testo (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_testo is None and "riferimento_testo" in self.model_fields_set:
            _dict['riferimento_testo'] = None

        # set to None if riferimento_numero (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_numero is None and "riferimento_numero" in self.model_fields_set:
            _dict['riferimento_numero'] = None

        # set to None if riferimento_data (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_data is None and "riferimento_data" in self.model_fields_set:
            _dict['riferimento_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AltriDatiGestionali from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tipo_dato": obj.get("tipo_dato"),
            "riferimento_testo": obj.get("riferimento_testo"),
            "riferimento_numero": obj.get("riferimento_numero"),
            "riferimento_data": obj.get("riferimento_data")
        })
        return _obj


