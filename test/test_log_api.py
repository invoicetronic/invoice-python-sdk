# coding: utf-8

"""
    Italian eInvoice API v1

    The [Italian eInvoice API][2] is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. The API also provides advanced features as encryption at rest, invoice validation, multiple upload formats, webhooks, event logging, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_invoice_sdk.api.log_api import LogApi


class TestLogApi(unittest.TestCase):
    """LogApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LogApi()

    def tearDown(self) -> None:
        pass

    def test_log_get(self) -> None:
        """Test case for log_get

        List events
        """
        pass

    def test_log_id_get(self) -> None:
        """Test case for log_id_get

        Get an event by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
