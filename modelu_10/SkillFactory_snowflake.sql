CREATE TABLE "nobels_laureates" (
  "id" int PRIMARY KEY,
  "year" varchar NOT NULL,
  "category" varchar NOT NULL,
  "prize" varchar NOT NULL,
  "motivation" varchar,
  "prize_share" varchar NOT NULL,
  "laureate_id" int NOT NULL,
  "laureate_type" varchar NOT NULL,
  "laureates_full_name" varchar NOT NULL,
  "laureates_birth_date" varchar NOT NULL,
  "laureates_birth_city" varchar
);

CREATE TABLE "countries_of_the_world" (
  "id" int PRIMARY KEY,
  "country_name" varchar NOT NULL,
  "continent" varchar NOT NULL,
  "currency" varchar NOT NULL,
  "iso3" varchar NOT NULL,
  "phone_code" varchar NOT NULL,
  "population" int NOT NULL,
  "area_sq_mi" int NOT NULL,
  "pop_density" float NOT NULL,
  "coastline" float NOT NULL,
  "net_migration" float NOT NULL,
  "infant_mortality" float NOT NULL,
  "gdp_usd_per_capita" int NOT NULL,
  "literacy_percent" float NOT NULL
);

CREATE TABLE "world_cities_database" (
  "id" int PRIMARY KEY,
  "country_id" int,
  "city_name" varchar NOT NULL,
  "accent_city" varchar NOT NULL,
  "region" int NOT NULL,
  "population" float,
  "latitude" float NOT NULL,
  "longitude" float NOT NULL
);

ALTER TABLE "nobels_laureates" ADD FOREIGN KEY ("laureates_birth_city") REFERENCES "world_cities_database" ("id");

ALTER TABLE "world_cities_database" ADD FOREIGN KEY ("country_id") REFERENCES "countries_of_the_world" ("id");
