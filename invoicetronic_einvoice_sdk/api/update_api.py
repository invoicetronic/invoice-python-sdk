# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1] (Interchange Service). The API is designed by Invoicetronic to be simple and easy to use, abstracting away the Interchange Service's complexity while still providing complete control over the invoice send/receive process. The API also provides advanced features and a rich toolchain, such as invoice validation, multiple upload methods, webhooks, event logs, CORS support, client SDKs for commonly used languages, and CLI tools.  For more information, see:  - [Invoicetronic website][2] - [Invoice API reference][3]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/ [3]: https://api.invoicetronic.com/invoice/v1/docs 

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from invoicetronic_einvoice_sdk.models.update import Update

from invoicetronic_einvoice_sdk.api_client import ApiClient, RequestSerialized
from invoicetronic_einvoice_sdk.api_response import ApiResponse
from invoicetronic_einvoice_sdk.rest import RESTResponseType


class UpdateApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def invoice_v1_update_get(
        self,
        company_id: Annotated[Optional[StrictInt], Field(description="Company id.")] = None,
        identifier: Annotated[Optional[StrictStr], Field(description="SDI identifier.")] = None,
        unread: Annotated[Optional[StrictBool], Field(description="Only unread items.")] = None,
        send_id: Annotated[Optional[StrictInt], Field(description="Send item's id.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="SDI state")] = None,
        last_update_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        last_update_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 format (2024-11-29T12:34:56Z)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Update]:
        """List updates

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param company_id: Company id.
        :type company_id: int
        :param identifier: SDI identifier.
        :type identifier: str
        :param unread: Only unread items.
        :type unread: bool
        :param send_id: Send item's id.
        :type send_id: int
        :param state: SDI state
        :type state: str
        :param last_update_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_from: datetime
        :param last_update_to: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_to: datetime
        :param date_sent_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type date_sent_from: datetime
        :param date_sent_to: UTC ISO 8601 format (2024-11-29T12:34:56Z)
        :type date_sent_to: datetime
        :param page: Page number.
        :type page: int
        :param page_size: Items per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_get_serialize(
            company_id=company_id,
            identifier=identifier,
            unread=unread,
            send_id=send_id,
            state=state,
            last_update_from=last_update_from,
            last_update_to=last_update_to,
            date_sent_from=date_sent_from,
            date_sent_to=date_sent_to,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Update]",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def invoice_v1_update_get_with_http_info(
        self,
        company_id: Annotated[Optional[StrictInt], Field(description="Company id.")] = None,
        identifier: Annotated[Optional[StrictStr], Field(description="SDI identifier.")] = None,
        unread: Annotated[Optional[StrictBool], Field(description="Only unread items.")] = None,
        send_id: Annotated[Optional[StrictInt], Field(description="Send item's id.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="SDI state")] = None,
        last_update_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        last_update_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 format (2024-11-29T12:34:56Z)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Update]]:
        """List updates

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param company_id: Company id.
        :type company_id: int
        :param identifier: SDI identifier.
        :type identifier: str
        :param unread: Only unread items.
        :type unread: bool
        :param send_id: Send item's id.
        :type send_id: int
        :param state: SDI state
        :type state: str
        :param last_update_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_from: datetime
        :param last_update_to: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_to: datetime
        :param date_sent_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type date_sent_from: datetime
        :param date_sent_to: UTC ISO 8601 format (2024-11-29T12:34:56Z)
        :type date_sent_to: datetime
        :param page: Page number.
        :type page: int
        :param page_size: Items per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_get_serialize(
            company_id=company_id,
            identifier=identifier,
            unread=unread,
            send_id=send_id,
            state=state,
            last_update_from=last_update_from,
            last_update_to=last_update_to,
            date_sent_from=date_sent_from,
            date_sent_to=date_sent_to,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Update]",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def invoice_v1_update_get_without_preload_content(
        self,
        company_id: Annotated[Optional[StrictInt], Field(description="Company id.")] = None,
        identifier: Annotated[Optional[StrictStr], Field(description="SDI identifier.")] = None,
        unread: Annotated[Optional[StrictBool], Field(description="Only unread items.")] = None,
        send_id: Annotated[Optional[StrictInt], Field(description="Send item's id.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="SDI state")] = None,
        last_update_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        last_update_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_from: Annotated[Optional[datetime], Field(description="UTC ISO 8601 (2024-11-29T12:34:56Z)")] = None,
        date_sent_to: Annotated[Optional[datetime], Field(description="UTC ISO 8601 format (2024-11-29T12:34:56Z)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List updates

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param company_id: Company id.
        :type company_id: int
        :param identifier: SDI identifier.
        :type identifier: str
        :param unread: Only unread items.
        :type unread: bool
        :param send_id: Send item's id.
        :type send_id: int
        :param state: SDI state
        :type state: str
        :param last_update_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_from: datetime
        :param last_update_to: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type last_update_to: datetime
        :param date_sent_from: UTC ISO 8601 (2024-11-29T12:34:56Z)
        :type date_sent_from: datetime
        :param date_sent_to: UTC ISO 8601 format (2024-11-29T12:34:56Z)
        :type date_sent_to: datetime
        :param page: Page number.
        :type page: int
        :param page_size: Items per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_get_serialize(
            company_id=company_id,
            identifier=identifier,
            unread=unread,
            send_id=send_id,
            state=state,
            last_update_from=last_update_from,
            last_update_to=last_update_to,
            date_sent_from=date_sent_from,
            date_sent_to=date_sent_to,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Update]",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _invoice_v1_update_get_serialize(
        self,
        company_id,
        identifier,
        unread,
        send_id,
        state,
        last_update_from,
        last_update_to,
        date_sent_from,
        date_sent_to,
        page,
        page_size,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if company_id is not None:
            
            _query_params.append(('company_id', company_id))
            
        if identifier is not None:
            
            _query_params.append(('identifier', identifier))
            
        if unread is not None:
            
            _query_params.append(('unread', unread))
            
        if send_id is not None:
            
            _query_params.append(('send_id', send_id))
            
        if state is not None:
            
            _query_params.append(('state', state))
            
        if last_update_from is not None:
            if isinstance(last_update_from, datetime):
                _query_params.append(
                    (
                        'last_update_from',
                        last_update_from.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('last_update_from', last_update_from))
            
        if last_update_to is not None:
            if isinstance(last_update_to, datetime):
                _query_params.append(
                    (
                        'last_update_to',
                        last_update_to.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('last_update_to', last_update_to))
            
        if date_sent_from is not None:
            if isinstance(date_sent_from, datetime):
                _query_params.append(
                    (
                        'date_sent_from',
                        date_sent_from.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date_sent_from', date_sent_from))
            
        if date_sent_to is not None:
            if isinstance(date_sent_to, datetime):
                _query_params.append(
                    (
                        'date_sent_to',
                        date_sent_to.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date_sent_to', date_sent_to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('page_size', page_size))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/invoice/v1/update',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def invoice_v1_update_id_get(
        self,
        id: Annotated[StrictInt, Field(description="Item id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Update:
        """Get an update by id

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param id: Item id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Update",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def invoice_v1_update_id_get_with_http_info(
        self,
        id: Annotated[StrictInt, Field(description="Item id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Update]:
        """Get an update by id

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param id: Item id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Update",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def invoice_v1_update_id_get_without_preload_content(
        self,
        id: Annotated[StrictInt, Field(description="Item id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get an update by id

        Updates are notifications that are sent by the SDI about the status of sent invoices.

        :param id: Item id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._invoice_v1_update_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Update",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _invoice_v1_update_id_get_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/invoice/v1/update/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


