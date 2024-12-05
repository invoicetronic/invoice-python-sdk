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

from invoicetronic_invoice_sdk.models.dati_trasporto import DatiTrasporto

class TestDatiTrasporto(unittest.TestCase):
    """DatiTrasporto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasporto:
        """Test DatiTrasporto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasporto`
        """
        model = DatiTrasporto()
        if include_optional:
            return DatiTrasporto(
                dati_anagrafici_vettore = invoicetronic_invoice_sdk.models.dati_anagrafici_vettore.DatiAnagraficiVettore(
                    id_fiscale_iva = invoicetronic_invoice_sdk.models.id_fiscale_iva.IdFiscaleIVA(
                        id_paese = '', 
                        id_codice = '', ), 
                    codice_fiscale = '', 
                    anagrafica = invoicetronic_invoice_sdk.models.anagrafica.Anagrafica(
                        denominazione = '', 
                        nome = '', 
                        cognome = '', 
                        titolo = '', 
                        cod_eori = '', ), 
                    numero_licenza_guida = '', ),
                mezzo_trasporto = '',
                causale_trasporto = '',
                numero_colli = 56,
                descrizione = '',
                unita_misura_peso = '',
                peso_lordo = 1.337,
                peso_netto = 1.337,
                data_ora_ritiro = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tipo_resa = '',
                indirizzo_resa = invoicetronic_invoice_sdk.models.indirizzo_resa.IndirizzoResa(
                    indirizzo = '', 
                    numero_civico = '', 
                    cap = '', 
                    comune = '', 
                    provincia = '', 
                    nazione = 'IT', ),
                data_ora_consegna = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DatiTrasporto(
        )
        """

    def testDatiTrasporto(self):
        """Test DatiTrasporto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
