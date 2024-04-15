
DEF_SQLITE_SCHEMA = """CREATE TABLE IF NOT EXISTS zabytki (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  inspire_id TEXT NOT NULL,
  forma_ochrony TEXT NOT NULL,
  dokladnosc_polozenia TEXT NOT NULL,
  nazwa TEXT NOT NULL,
  chronologia TEXT,
  funkcja TEXT NOT NULL,
  wykaz_dokumentow TEXT NOT NULL,
  data_wpisu TEXT NOT NULL,
  wojewodztwo TEXT NOT NULL,
  powiat TEXT NOT NULL,
  gmina TEXT NOT NULL,
  miejscowosc TEXT NOT NULL,
  ulica TEXT ,
  nr_adresowy TEXT,
  szerokosc_geogr TEXT,
  dlugosc_geogr TEXT
);
"""

SQL_QUERY = \
    "select id, nazwa, chronologia, miejscowosc, ulica, nr_adresowy, szerokosc_geogr, dlugosc_geogr from zabytki;"

NUM_OF_MONUMENTS = 1489
