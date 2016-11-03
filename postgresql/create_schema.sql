-- Create database for the project
CREATE DATABASE dav;

-- Create schema for the project
CREATE SCHEMA dav;

-- Create user
CREATE USER dba PASSWORD 'root';
-- Grant permissions
GRANT ALL ON DATABASE dav TO dba;
GRANT ALL ON ALL TABLES IN SCHEMA dav TO dba;

-- Table: dav.data_landing

-- DROP TABLE dav.data_landing;

CREATE TABLE dav.data_landing
(
  id bigserial NOT NULL,
  ticker character varying(20) NOT NULL,
  date character varying(20) NOT NULL,
  open character varying(20) NOT NULL,
  high character varying(20) NOT NULL,
  low character varying(20) NOT NULL,
  close character varying(20) NOT NULL,
  volume character varying(20) NOT NULL,
  "ex-dividend" character varying(20) NOT NULL,
  split_ratio character varying(20),
  adj_open character varying(20),
  adj_high character varying(20),
  adj_low character varying(20),
  adj_close character varying(20),
  adj_volume character varying(20),
  CONSTRAINT data_landing_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dav.data_landing
  OWNER TO dba;