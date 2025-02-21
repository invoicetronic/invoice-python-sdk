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

from invoicetronic_invoice_sdk.models.dati_anagrafici import DatiAnagrafici

class TestDatiAnagrafici(unittest.TestCase):
    """DatiAnagrafici unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiAnagrafici:
        """Test DatiAnagrafici
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiAnagrafici`
        """
        model = DatiAnagrafici()
        if include_optional:
            return DatiAnagrafici(
                id_fiscale_iva = invoicetronic_invoice_sdk.models.id_fiscale_iva.IdFiscaleIVA(
                    id_paese = '', 
                    id_codice = '', ),
                codice_fiscale = '',
                anagrafica = invoicetronic_invoice_sdk.models.anagrafica.Anagrafica(
                    denominazione = '', 
                    nome = '', 
                    cognome = '', 
                    titolo = '', 
                    cod_eori = '', )
            )
        else:
            return DatiAnagrafici(
        )
        """

    def testDatiAnagrafici(self):
        """Test DatiAnagrafici"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
