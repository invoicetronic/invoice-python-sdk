# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while still providing complete control over the invoice send/receive process. The API also provides advanced features and a rich toolchain, such as invoice validation, multiple upload methods, webhooks, event logs, CORS support, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Company(BaseModel):
    """
    A company model.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier. Leave it at 0 for new records as it will be set automatically.")
    created: Optional[datetime] = Field(default=None, description="Creation date. It is set automatically.")
    version: Optional[StrictInt] = Field(default=None, description="Row version, for optimistic concurrency. It is set automatically.")
    user_id: Optional[StrictInt] = Field(default=None, description="User id.")
    vat: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Vat number. Must include the country code.")
    fiscal_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Fiscal code. In most cases it's the same as the vat number.")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name")
    counter: Optional[StrictInt] = Field(default=None, description="Holds the last unique value used to generate a XML filename. This is automatically updated by the system   when a raw XML file is uploaded. Normally, you do not need or want to change this value.")
    __properties: ClassVar[List[str]] = ["id", "created", "version", "user_id", "vat", "fiscal_code", "name", "counter"]

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
        """Create an instance of Company from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Company from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "version": obj.get("version"),
            "user_id": obj.get("user_id"),
            "vat": obj.get("vat"),
            "fiscal_code": obj.get("fiscal_code"),
            "name": obj.get("name"),
            "counter": obj.get("counter")
        })
        return _obj


