# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while still providing complete control over the invoice send/receive process. The API also provides advanced features and a rich toolchain, such as invoice validation, multiple upload methods, webhooks, event logs, CORS support, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_invoice_sdk.api.update_api import UpdateApi


class TestUpdateApi(unittest.TestCase):
    """UpdateApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UpdateApi()

    def tearDown(self) -> None:
        pass

    def test_invoice_v1_update_get(self) -> None:
        """Test case for invoice_v1_update_get

        List updates
        """
        pass

    def test_invoice_v1_update_id_get(self) -> None:
        """Test case for invoice_v1_update_id_get

        Get an update by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
