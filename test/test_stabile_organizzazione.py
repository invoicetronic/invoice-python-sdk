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

from invoicetronic_invoice_sdk.models.stabile_organizzazione import StabileOrganizzazione

class TestStabileOrganizzazione(unittest.TestCase):
    """StabileOrganizzazione unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StabileOrganizzazione:
        """Test StabileOrganizzazione
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StabileOrganizzazione`
        """
        model = StabileOrganizzazione()
        if include_optional:
            return StabileOrganizzazione(
                indirizzo = '',
                numero_civico = '',
                cap = '',
                comune = '',
                provincia = '',
                nazione = 'IT'
            )
        else:
            return StabileOrganizzazione(
        )
        """

    def testStabileOrganizzazione(self):
        """Test StabileOrganizzazione"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
