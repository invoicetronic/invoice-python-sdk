# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1] (Interchange Service). The API is designed by Invoicetronic to be simple and easy to use, abstracting away the Interchange Service's complexity while still providing complete control over the invoice send/receive process. The API also provides advanced features and a rich toolchain, such as invoice validation, multiple upload methods, webhooks, event logs, CORS support, client SDKs for commonly used languages, and CLI tools.  For more information, see:  - [Invoicetronic website][2] - [Invoice API reference][3]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/ [3]: https://api.invoicetronic.com/invoice/v1/docs 

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_invoice_sdk.api.receive_api import ReceiveApi


class TestReceiveApi(unittest.TestCase):
    """ReceiveApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReceiveApi()

    def tearDown(self) -> None:
        pass

    def test_invoice_v1_receive_get(self) -> None:
        """Test case for invoice_v1_receive_get

        List incoming invoices
        """
        pass

    def test_invoice_v1_receive_id_delete(self) -> None:
        """Test case for invoice_v1_receive_id_delete

        Delete an incoming invoice by id
        """
        pass

    def test_invoice_v1_receive_id_get(self) -> None:
        """Test case for invoice_v1_receive_id_get

        Get an incoming invoice by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
