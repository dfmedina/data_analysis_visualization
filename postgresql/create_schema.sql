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
  "ex-dividend" character varying(50),
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