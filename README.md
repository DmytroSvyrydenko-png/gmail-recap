# gmail-recap


## Projekta uzdevums

"The Gmail Recap 2023" projekts ir izstrādāts ar mērķi sniegt lietotājam ieskatu par viņa 2023. gada Gmail e-pasta lietošanu, izmantojot priekšmetā "Lietojumprogrammatūras automatizācijas rīki" apgūtās prasmes. Projekts pamatojas uz Spotify Wrapped ideju (ikgadējs personalizēts mūzikas klausīšanās pārskats ikvienam Spotify lietotnes lietotājam). Lietotājam ir iespēja iegūt informāciju par saņemtajiem, nosūtītajiem, sagatavotajiem, izceltajiem, nepieskatītajiem un sev pašam nosūtītiem e-vēstulem, kā arī uzzināt par datu noplūdēm, kurās varētu būt iesaistīts lietotāja e-pasta adrese.

## Izmantotās Python bibliotēkas

1. **imaplib:** Izmantots, lai saņemtu datus no Gmail, iegūtu statistiku par e-pastiem un to izmantošanas informāciju. Lietots papildresurs [ImapSearch Method](https://afterlogic.com/mailbee-net/docs/MailBee.ImapMail.Imap.Search_overload_2.html)

2. **datetime:** Izmantots, lai veiktu datuma un laika operācijas, piemēram, noteiktu sākuma un beigu datumus projekta statistikai.

3. **smtplib:** Izmantots, lai nosūtītu personalizētu Gmail Recap 2023 vēstuli ar iegūto statistiku lietotājam.

4. **selenium:** Izmantots, lai automatizētu datu iegūšanu no mājaslapas [Mozilla Monitor](https://monitor.mozilla.org/) par datu noplūdēm, kurās varētu būt iesaistīts lietotājs.

5. **time:** Izmantots, lai veiktu aiztures un pauzes skripta izpildes laikā, nodrošinot pietiekamu laiku mājaslapu resursu iegūšanai un apstrādei.

## Programmatūras izmantošanas metodes

1. **Sagatavošana:**
   - Pārliecinieties, ka jums ir uzstādīts Python interpretators jūsu ierīcē.
   - Lejupielādējiet nepieciešamās Python bibliotēkas (imaplib, smtplib, selenium)
   - Izveidojiet speciālo lietojumprogrammas paroli, lai ieiet savā Gmail e-pastā. Sīkāka instrukcija mājaslapā [Support Google](https://support.google.com/accounts/answer/185833?hl=ru)

2. **Skripta izpilde:**
   - Izpildiet faila 'email_stat.py' skriptu.
   - Sekojiet norādēm un ievadiet savu Gmail e-pasta adresi un lietojumprogrammas paroli.

3. **Rezultātu pārbaude:**
   - Pēc skripta izpildes pārbaudiet vai terminālā parādījās ziņa 'The GMAIL RECAP 2023 was sent to your inbox!' un pārbaudiet savu Gmail pastu.
   - Ja viss noritējis veiksmīgi, jūs saņemsiet personalizētu "Gmail Recap 2023" vēstuli ar statistiku par jūsu 2023. gada e-pasta lietošanu.

4. **Papildu informācija:**
    - Lai skripts darbotos pareizi, lietotājam jānodrošina pareiza Gmail e-pasta adrese un lietojumprogrammas parole.
    - Drošības apsvērumu dēļ ir svarīgi pārliecināties, ka lietotājs ir informēts un piekrīt izmantot šo programmu.
    - Skriptam ir nepieciešama piekļuve interneta resursiem, lai iegūtu datus no Mozilla Monitor un nosūtītu ziņojumu.


