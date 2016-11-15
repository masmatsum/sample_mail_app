
CREATE TABLE users (
  id bigserial PRIMARY KEY,
  name text,
  pref_cd int,
  site text,
  created_dt timestamp
);

CREATE TABLE companies (
  id bigserial PRIMARY KEY,
  name text,
  created_dt timestamp
);

CREATE TABLE jobs (
  id bigserial PRIMARY KEY,
  company_id bigint REFERENCES companies(id),
  title text,
  content text,
  created_dt timestamp
);

CREATE TABLE entries (
  id bigserial PRIMARY KEY,
  user_id bigint REFERENCES users(id),
  job_id bigint REFERENCES jobs(id),
  entry_dt timestamp,
  is_anonymous bool
);

CREATE TABLE prefs (
  id int PRIMARY KEY,
  name text
--  large_area text,
);

