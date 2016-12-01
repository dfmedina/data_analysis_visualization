-- Create database for the project
CREATE DATABASE dav;

-- Create user
CREATE USER dba PASSWORD 'root';
-- Grant permissions
GRANT ALL ON DATABASE dav TO dba;

-- Create schema for the project
CREATE SCHEMA dav;

-- Table: dav.data_landing

-- DROP TABLE dav.data_landing;

CREATE TABLE dav.data_landing
   (
    id bigserial NOT NULL,
    ticker character varying(50) NOT NULL,
    date character varying(50),
    open character varying(50),
    high character varying(50),
    low character varying(50),
    close character varying(50),
    volume character varying(50),
    ex_dividend character varying(50),
    split_ratio character varying(50),
    adj_open character varying(50),
    adj_high character varying(50),
    adj_low character varying(50),
    adj_close character varying(50),
    adj_volume character varying(50),
    CONSTRAINT data_landing_pkey PRIMARY KEY (id)
    )
WITH (
       OIDS=FALSE
      );
ALTER TABLE dav.data_landing
OWNER TO dba;

--DROP TABLE dav.company_landing;

CREATE TABLE dav.company_landing
(
  symbol character varying(100) NOT NULL,
  name character varying(100) NOT NULL,
  last_sale character varying(100),
  market_cap character varying(100),
  country character varying(100),
  ipo_year character varying(100),
  sector character varying(100),
  industry character varying(100),
  CONSTRAINT company_landing_pkey PRIMARY KEY (symbol)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dav.company_landing
  OWNER TO dba;