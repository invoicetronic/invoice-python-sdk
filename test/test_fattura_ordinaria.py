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

from invoicetronic_invoice_sdk.models.fattura_ordinaria import FatturaOrdinaria

class TestFatturaOrdinaria(unittest.TestCase):
    """FatturaOrdinaria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FatturaOrdinaria:
        """Test FatturaOrdinaria
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FatturaOrdinaria`
        """
        model = FatturaOrdinaria()
        if include_optional:
            return FatturaOrdinaria(
                sistema_emittente = '',
                fattura_elettronica_header = invoicetronic_invoice_sdk.models.fattura_elettronica_header.FatturaElettronicaHeader(
                    dati_trasmissione = invoicetronic_invoice_sdk.models.dati_trasmissione.DatiTrasmissione(
                        id_trasmittente = invoicetronic_invoice_sdk.models.id_trasmittente.IdTrasmittente(
                            id_paese = '', 
                            id_codice = '', ), 
                        progressivo_invio = '', 
                        formato_trasmissione = '', 
                        codice_destinatario = '', 
                        contatti_trasmittente = invoicetronic_invoice_sdk.models.contatti_trasmittente.ContattiTrasmittente(
                            telefono = '', 
                            email = '', ), 
                        pec_destinatario = '', ), 
                    cedente_prestatore = invoicetronic_invoice_sdk.models.cedente_prestatore.CedentePrestatore(
                        dati_anagrafici = invoicetronic_invoice_sdk.models.dati_anagrafici_cedente_prestatore.DatiAnagraficiCedentePrestatore(
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
                            albo_professionale = '', 
                            provincia_albo = '', 
                            numero_iscrizione_albo = '', 
                            data_iscrizione_albo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            regime_fiscale = '', ), 
                        sede = invoicetronic_invoice_sdk.models.sede_cedente_prestatore.SedeCedentePrestatore(
                            indirizzo = '', 
                            numero_civico = '', 
                            cap = '', 
                            comune = '', 
                            provincia = '', 
                            nazione = 'IT', ), 
                        stabile_organizzazione = invoicetronic_invoice_sdk.models.stabile_organizzazione.StabileOrganizzazione(
                            indirizzo = '', 
                            numero_civico = '', 
                            cap = '', 
                            comune = '', 
                            provincia = '', 
                            nazione = 'IT', ), 
                        iscrizione_rea = invoicetronic_invoice_sdk.models.iscrizione_rea.IscrizioneREA(
                            ufficio = '', 
                            numero_rea = '', 
                            capitale_sociale = 1.337, 
                            socio_unico = '', 
                            stato_liquidazione = '', ), 
                        contatti = invoicetronic_invoice_sdk.models.contatti.Contatti(
                            telefono = '', 
                            fax = '', 
                            email = '', ), 
                        riferimento_amministrazione = '', ), 
                    rappresentante_fiscale = invoicetronic_invoice_sdk.models.rappresentante_fiscale.RappresentanteFiscale(), 
                    cessionario_committente = invoicetronic_invoice_sdk.models.cessionario_committente.CessionarioCommittente(
                        rappresentante_fiscale = invoicetronic_invoice_sdk.models.rappresentante_fiscale_cessionario_committente.RappresentanteFiscaleCessionarioCommittente(
                            denominazione = '', 
                            nome = '', 
                            cognome = '', ), ), 
                    terzo_intermediario_o_soggetto_emittente = invoicetronic_invoice_sdk.models.terzo_intermediario_o_soggetto_emittente.TerzoIntermediarioOSoggettoEmittente(), 
                    soggetto_emittente = '', ),
                fattura_elettronica_body = [
                    invoicetronic_invoice_sdk.models.fattura_elettronica_body.FatturaElettronicaBody(
                        dati_generali = invoicetronic_invoice_sdk.models.dati_generali.DatiGenerali(
                            dati_generali_documento = invoicetronic_invoice_sdk.models.dati_generali_documento.DatiGeneraliDocumento(
                                tipo_documento = '', 
                                divisa = '', 
                                data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                numero = '', 
                                dati_ritenuta = [
                                    invoicetronic_invoice_sdk.models.dati_ritenuta.DatiRitenuta(
                                        tipo_ritenuta = '', 
                                        importo_ritenuta = 1.337, 
                                        aliquota_ritenuta = 1.337, 
                                        causale_pagamento = '', )
                                    ], 
                                dati_bollo = invoicetronic_invoice_sdk.models.dati_bollo.DatiBollo(
                                    bollo_virtuale = '', 
                                    importo_bollo = 1.337, ), 
                                dati_cassa_previdenziale = [
                                    invoicetronic_invoice_sdk.models.dati_cassa_previdenziale.DatiCassaPrevidenziale(
                                        tipo_cassa = '', 
                                        al_cassa = 1.337, 
                                        importo_contributo_cassa = 1.337, 
                                        imponibile_cassa = 1.337, 
                                        aliquota_iva = 1.337, 
                                        ritenuta = '', 
                                        natura = '', 
                                        riferimento_amministrazione = '', )
                                    ], 
                                sconto_maggiorazione = [
                                    invoicetronic_invoice_sdk.models.sconto_maggiorazione.ScontoMaggiorazione(
                                        tipo = '', 
                                        percentuale = 1.337, 
                                        importo = 1.337, )
                                    ], 
                                importo_totale_documento = 1.337, 
                                arrotondamento = 1.337, 
                                causale = [
                                    ''
                                    ], 
                                art73 = '', ), 
                            dati_ordine_acquisto = [
                                invoicetronic_invoice_sdk.models.dati_ordine_acquisto.DatiOrdineAcquisto(
                                    riferimento_numero_linea = [
                                        56
                                        ], 
                                    id_documento = '', 
                                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    num_item = '', 
                                    codice_commessa_convenzione = '', 
                                    codice_cup = '', 
                                    codice_cig = '', )
                                ], 
                            dati_contratto = [
                                invoicetronic_invoice_sdk.models.dati_contratto.DatiContratto(
                                    id_documento = '', 
                                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    num_item = '', 
                                    codice_commessa_convenzione = '', 
                                    codice_cup = '', 
                                    codice_cig = '', )
                                ], 
                            dati_convenzione = [
                                invoicetronic_invoice_sdk.models.dati_convenzione.DatiConvenzione(
                                    id_documento = '', 
                                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    num_item = '', 
                                    codice_commessa_convenzione = '', 
                                    codice_cup = '', 
                                    codice_cig = '', )
                                ], 
                            dati_ricezione = [
                                invoicetronic_invoice_sdk.models.dati_ricezione.DatiRicezione(
                                    id_documento = '', 
                                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    num_item = '', 
                                    codice_commessa_convenzione = '', 
                                    codice_cup = '', 
                                    codice_cig = '', )
                                ], 
                            dati_fatture_collegate = [
                                invoicetronic_invoice_sdk.models.dati_fatture_collegate.DatiFattureCollegate(
                                    id_documento = '', 
                                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    num_item = '', 
                                    codice_commessa_convenzione = '', 
                                    codice_cup = '', 
                                    codice_cig = '', )
                                ], 
                            dati_sal = [
                                invoicetronic_invoice_sdk.models.dati_sal.DatiSAL(
                                    riferimento_fase = 56, )
                                ], 
                            dati_ddt = [
                                invoicetronic_invoice_sdk.models.dati_ddt.DatiDDT(
                                    numero_ddt = '', 
                                    data_ddt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            dati_trasporto = invoicetronic_invoice_sdk.models.dati_trasporto.DatiTrasporto(
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
                                data_ora_consegna = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            fattura_principale = invoicetronic_invoice_sdk.models.fattura_principale.FatturaPrincipale(
                                numero_fattura_principale = '', 
                                data_fattura_principale = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                        dati_beni_servizi = invoicetronic_invoice_sdk.models.dati_beni_servizi.DatiBeniServizi(
                            dettaglio_linee = [
                                invoicetronic_invoice_sdk.models.dettaglio_linee.DettaglioLinee(
                                    numero_linea = 56, 
                                    tipo_cessione_prestazione = '', 
                                    codice_articolo = [
                                        invoicetronic_invoice_sdk.models.codice_articolo.CodiceArticolo(
                                            codice_tipo = '', 
                                            codice_valore = '', )
                                        ], 
                                    descrizione = '', 
                                    quantita = 1.337, 
                                    unita_misura = '', 
                                    data_inizio_periodo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    data_fine_periodo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    prezzo_unitario = 1.337, 
                                    prezzo_totale = 1.337, 
                                    aliquota_iva = 1.337, 
                                    ritenuta = '', 
                                    natura = '', 
                                    riferimento_amministrazione = '', 
                                    altri_dati_gestionali = [
                                        invoicetronic_invoice_sdk.models.altri_dati_gestionali.AltriDatiGestionali(
                                            tipo_dato = '', 
                                            riferimento_testo = '', 
                                            riferimento_numero = 1.337, 
                                            riferimento_data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                        ], )
                                ], 
                            dati_riepilogo = [
                                invoicetronic_invoice_sdk.models.dati_riepilogo.DatiRiepilogo(
                                    aliquota_iva = 1.337, 
                                    natura = '', 
                                    spese_accessorie = 1.337, 
                                    arrotondamento = 1.337, 
                                    imponibile_importo = 1.337, 
                                    imposta = 1.337, 
                                    esigibilita_iva = '', 
                                    riferimento_normativo = '', )
                                ], ), 
                        dati_veicoli = invoicetronic_invoice_sdk.models.dati_veicoli.DatiVeicoli(
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            totale_percorso = '', ), 
                        dati_pagamento = [
                            invoicetronic_invoice_sdk.models.dati_pagamento.DatiPagamento(
                                condizioni_pagamento = '', 
                                dettaglio_pagamento = [
                                    invoicetronic_invoice_sdk.models.dettaglio_pagamento.DettaglioPagamento(
                                        beneficiario = '', 
                                        modalita_pagamento = '', 
                                        data_riferimento_termini_pagamento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        giorni_termini_pagamento = 56, 
                                        data_scadenza_pagamento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        importo_pagamento = 1.337, 
                                        cod_ufficio_postale = '', 
                                        cognome_quietanzante = '', 
                                        nome_quietanzante = '', 
                                        cf_quietanzante = '', 
                                        titolo_quietanzante = '', 
                                        istituto_finanziario = '', 
                                        iban = '', 
                                        abi = '', 
                                        cab = '', 
                                        bic = '', 
                                        sconto_pagamento_anticipato = 1.337, 
                                        data_limite_pagamento_anticipato = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        penalita_pagamenti_ritardati = 1.337, 
                                        data_decorrenza_penale = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        codice_pagamento = '', )
                                    ], )
                            ], 
                        allegati = [
                            invoicetronic_invoice_sdk.models.allegati.Allegati(
                                nome_attachment = '', 
                                algoritmo_compressione = '', 
                                formato_attachment = '', 
                                descrizione_attachment = '', 
                                attachment = 'YQ==', )
                            ], )
                    ]
            )
        else:
            return FatturaOrdinaria(
        )
        """

    def testFatturaOrdinaria(self):
        """Test FatturaOrdinaria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
