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
from invoicetronic_invoice_sdk.models.dati_bollo import DatiBollo
from invoicetronic_invoice_sdk.models.dati_cassa_previdenziale import DatiCassaPrevidenziale
from invoicetronic_invoice_sdk.models.dati_ritenuta import DatiRitenuta
from invoicetronic_invoice_sdk.models.sconto_maggiorazione import ScontoMaggiorazione
from typing import Optional, Set
from typing_extensions import Self

class DatiGeneraliDocumento(BaseModel):
    """
    DatiGeneraliDocumento
    """ # noqa: E501
    tipo_documento: Optional[StrictStr] = None
    divisa: Optional[StrictStr] = None
    data: Optional[datetime] = None
    numero: Optional[StrictStr] = None
    dati_ritenuta: Optional[List[DatiRitenuta]] = None
    dati_bollo: Optional[DatiBollo] = None
    dati_cassa_previdenziale: Optional[List[DatiCassaPrevidenziale]] = None
    sconto_maggiorazione: Optional[List[ScontoMaggiorazione]] = None
    importo_totale_documento: Optional[Union[StrictFloat, StrictInt]] = None
    arrotondamento: Optional[Union[StrictFloat, StrictInt]] = None
    causale: Optional[List[StrictStr]] = None
    art73: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["tipo_documento", "divisa", "data", "numero", "dati_ritenuta", "dati_bollo", "dati_cassa_previdenziale", "sconto_maggiorazione", "importo_totale_documento", "arrotondamento", "causale", "art73"]

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
        """Create an instance of DatiGeneraliDocumento from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dati_ritenuta (list)
        _items = []
        if self.dati_ritenuta:
            for _item_dati_ritenuta in self.dati_ritenuta:
                if _item_dati_ritenuta:
                    _items.append(_item_dati_ritenuta.to_dict())
            _dict['dati_ritenuta'] = _items
        # override the default output from pydantic by calling `to_dict()` of dati_bollo
        if self.dati_bollo:
            _dict['dati_bollo'] = self.dati_bollo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dati_cassa_previdenziale (list)
        _items = []
        if self.dati_cassa_previdenziale:
            for _item_dati_cassa_previdenziale in self.dati_cassa_previdenziale:
                if _item_dati_cassa_previdenziale:
                    _items.append(_item_dati_cassa_previdenziale.to_dict())
            _dict['dati_cassa_previdenziale'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sconto_maggiorazione (list)
        _items = []
        if self.sconto_maggiorazione:
            for _item_sconto_maggiorazione in self.sconto_maggiorazione:
                if _item_sconto_maggiorazione:
                    _items.append(_item_sconto_maggiorazione.to_dict())
            _dict['sconto_maggiorazione'] = _items
        # set to None if tipo_documento (nullable) is None
        # and model_fields_set contains the field
        if self.tipo_documento is None and "tipo_documento" in self.model_fields_set:
            _dict['tipo_documento'] = None

        # set to None if divisa (nullable) is None
        # and model_fields_set contains the field
        if self.divisa is None and "divisa" in self.model_fields_set:
            _dict['divisa'] = None

        # set to None if numero (nullable) is None
        # and model_fields_set contains the field
        if self.numero is None and "numero" in self.model_fields_set:
            _dict['numero'] = None

        # set to None if dati_ritenuta (nullable) is None
        # and model_fields_set contains the field
        if self.dati_ritenuta is None and "dati_ritenuta" in self.model_fields_set:
            _dict['dati_ritenuta'] = None

        # set to None if dati_cassa_previdenziale (nullable) is None
        # and model_fields_set contains the field
        if self.dati_cassa_previdenziale is None and "dati_cassa_previdenziale" in self.model_fields_set:
            _dict['dati_cassa_previdenziale'] = None

        # set to None if sconto_maggiorazione (nullable) is None
        # and model_fields_set contains the field
        if self.sconto_maggiorazione is None and "sconto_maggiorazione" in self.model_fields_set:
            _dict['sconto_maggiorazione'] = None

        # set to None if importo_totale_documento (nullable) is None
        # and model_fields_set contains the field
        if self.importo_totale_documento is None and "importo_totale_documento" in self.model_fields_set:
            _dict['importo_totale_documento'] = None

        # set to None if arrotondamento (nullable) is None
        # and model_fields_set contains the field
        if self.arrotondamento is None and "arrotondamento" in self.model_fields_set:
            _dict['arrotondamento'] = None

        # set to None if causale (nullable) is None
        # and model_fields_set contains the field
        if self.causale is None and "causale" in self.model_fields_set:
            _dict['causale'] = None

        # set to None if art73 (nullable) is None
        # and model_fields_set contains the field
        if self.art73 is None and "art73" in self.model_fields_set:
            _dict['art73'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatiGeneraliDocumento from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tipo_documento": obj.get("tipo_documento"),
            "divisa": obj.get("divisa"),
            "data": obj.get("data"),
            "numero": obj.get("numero"),
            "dati_ritenuta": [DatiRitenuta.from_dict(_item) for _item in obj["dati_ritenuta"]] if obj.get("dati_ritenuta") is not None else None,
            "dati_bollo": DatiBollo.from_dict(obj["dati_bollo"]) if obj.get("dati_bollo") is not None else None,
            "dati_cassa_previdenziale": [DatiCassaPrevidenziale.from_dict(_item) for _item in obj["dati_cassa_previdenziale"]] if obj.get("dati_cassa_previdenziale") is not None else None,
            "sconto_maggiorazione": [ScontoMaggiorazione.from_dict(_item) for _item in obj["sconto_maggiorazione"]] if obj.get("sconto_maggiorazione") is not None else None,
            "importo_totale_documento": obj.get("importo_totale_documento"),
            "arrotondamento": obj.get("arrotondamento"),
            "causale": obj.get("causale"),
            "art73": obj.get("art73")
        })
        return _obj


