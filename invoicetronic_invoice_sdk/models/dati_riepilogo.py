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

class DatiRiepilogo(BaseModel):
    """
    DatiRiepilogo
    """ # noqa: E501
    aliquota_iva: Optional[Union[StrictFloat, StrictInt]] = None
    natura: Optional[StrictStr] = None
    spese_accessorie: Optional[Union[StrictFloat, StrictInt]] = None
    arrotondamento: Optional[Union[StrictFloat, StrictInt]] = None
    imponibile_importo: Optional[Union[StrictFloat, StrictInt]] = None
    imposta: Optional[Union[StrictFloat, StrictInt]] = None
    esigibilita_iva: Optional[StrictStr] = None
    riferimento_normativo: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["aliquota_iva", "natura", "spese_accessorie", "arrotondamento", "imponibile_importo", "imposta", "esigibilita_iva", "riferimento_normativo"]

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
        """Create an instance of DatiRiepilogo from a JSON string"""
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
        # set to None if natura (nullable) is None
        # and model_fields_set contains the field
        if self.natura is None and "natura" in self.model_fields_set:
            _dict['natura'] = None

        # set to None if spese_accessorie (nullable) is None
        # and model_fields_set contains the field
        if self.spese_accessorie is None and "spese_accessorie" in self.model_fields_set:
            _dict['spese_accessorie'] = None

        # set to None if arrotondamento (nullable) is None
        # and model_fields_set contains the field
        if self.arrotondamento is None and "arrotondamento" in self.model_fields_set:
            _dict['arrotondamento'] = None

        # set to None if esigibilita_iva (nullable) is None
        # and model_fields_set contains the field
        if self.esigibilita_iva is None and "esigibilita_iva" in self.model_fields_set:
            _dict['esigibilita_iva'] = None

        # set to None if riferimento_normativo (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_normativo is None and "riferimento_normativo" in self.model_fields_set:
            _dict['riferimento_normativo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatiRiepilogo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aliquota_iva": obj.get("aliquota_iva"),
            "natura": obj.get("natura"),
            "spese_accessorie": obj.get("spese_accessorie"),
            "arrotondamento": obj.get("arrotondamento"),
            "imponibile_importo": obj.get("imponibile_importo"),
            "imposta": obj.get("imposta"),
            "esigibilita_iva": obj.get("esigibilita_iva"),
            "riferimento_normativo": obj.get("riferimento_normativo")
        })
        return _obj


