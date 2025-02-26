  ALTER TABLE [Covid Database schema].[dbo].[CovidCountry]
  ALTER COLUMN location nvarchar (255) NOT NULL
  
  ALTER TABLE [Covid Database schema].[dbo].[CovidCountry]
  ADD PRIMARY KEY (location)

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases]
  ALTER COLUMN location nvarchar (255) NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases]
  ADD FOREIGN KEY (location) REFERENCES [Covid Database schema].[dbo].[CovidCountry] (location)

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases]
  ALTER COLUMN cases_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases]
  ADD PRIMARY KEY (cases_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases_per_millions]
  ALTER COLUMN cases_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidCases_per_millions]
  ADD FOREIGN KEY (cases_id) REFERENCES [Covid Database schema].[dbo].[CovidCases] (cases_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths]
  ALTER COLUMN location nvarchar (255) NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths]
  ADD FOREIGN KEY (location) REFERENCES [Covid Database schema].[dbo].[CovidCountry] (location)

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths]
  ALTER COLUMN deaths_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths]
  ADD PRIMARY KEY (deaths_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths_per_millions]
  ALTER COLUMN deaths_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths_per_millions]
  ADD FOREIGN KEY (deaths_id) REFERENCES [Covid Database schema].[dbo].[CovidDeaths] (deaths_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu]
  ALTER COLUMN location nvarchar (255) NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu]
  ADD FOREIGN KEY (location) REFERENCES [Covid Database schema].[dbo].[CovidCountry] (location)

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu]
  ALTER COLUMN hosp_icu_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu]
  ADD PRIMARY KEY (hosp_icu_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu_Weekly]
  ALTER COLUMN hosp_icu_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu_Weekly]
  ADD FOREIGN KEY (hosp_icu_id) REFERENCES [Covid Database schema].[dbo].[CovidHosp_Icu] (hosp_icu_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu_Weekly_per_millions]
  ALTER COLUMN hosp_icu_id float NOT NULL

  ALTER TABLE [Covid Database schema].[dbo].[CovidHosp_Icu_Weekly_per_millions]
  ADD FOREIGN KEY (hosp_icu_id) REFERENCES [Covid Database schema].[dbo].[CovidHosp_Icu] (hosp_icu_id)

  ALTER TABLE [Covid Database schema].[dbo].[CovidDeaths]
  ALTER COLUMN total_deaths float

  ALTER TABLE [Covid Database schema].[dbo].[CovidCountry]
  ALTER COLUMN population float


  --Finding 10 countrys with highest death strike
  --1st method:

  SELECT
		TOP 10 total_death_strike,
		death_strike.location
  FROM
	  (SELECT
			loc_pop_tot.location,
			(loc_pop_tot.total_deaths/loc_pop_tot.population*100) AS total_death_strike
	  FROM
		  (SELECT
				country.location,
				country.population,
				MAX(deaths.total_deaths) AS total_deaths
		  FROM [Covid Database schema].[dbo].[CovidCountry] AS country
		  LEFT JOIN [Covid Database schema].[dbo].[CovidDeaths] AS deaths
		  ON country.location = deaths.location
		  WHERE deaths.date >= '2020-01-01 00:00:00.000' AND deaths.date <= '2022-12-31 00:00:00.000'
		  GROUP BY country.location,
				   country.population) AS loc_pop_tot
	  GROUP BY loc_pop_tot.location,
				loc_pop_tot.total_deaths,
				loc_pop_tot.population) AS death_strike
  ORDER BY total_death_strike DESC

  --2nd method:
			
SELECT
		total_death_strike_with_rank.location,
		total_death_strike_with_rank.total_death_strike,
		total_death_strike_with_rank.ranked
FROM
	  (SELECT
			RANK() OVER (ORDER BY total_death_strike) AS ranked,
			death_strike.location,
			total_death_strike
	  FROM
		  (SELECT
				loc_pop_tot.location,
				(loc_pop_tot.total_deaths/loc_pop_tot.population*100) AS total_death_strike
		  FROM
			  (SELECT
					country.location,
					country.population,
					MAX(deaths.total_deaths) AS total_deaths
			  FROM [Covid Database schema].[dbo].[CovidCountry] AS country
			  LEFT JOIN [Covid Database schema].[dbo].[CovidDeaths] AS deaths
			  ON country.location = deaths.location
			  WHERE deaths.date >= '2020-01-01 00:00:00.000' AND deaths.date <= '2022-12-31 00:00:00.000'
			  GROUP BY country.location,
					   country.population) AS loc_pop_tot
		  GROUP BY loc_pop_tot.location,
					loc_pop_tot.total_deaths,
					loc_pop_tot.population) AS death_strike
		) AS total_death_strike_with_rank	
WHERE total_death_strike_with_rank.ranked >192
ORDER BY total_death_strike DESC



-- When Country cross 25% population infected
SELECT *
FROM
	(SELECT
			RANK() OVER (PARTITION BY percentage_of_population_infected.location
						 ORDER BY percentage_of_population_infected,
								  percentage_of_population_infected.date) AS rk,
			percentage_of_population_infected.date,
			percentage_of_population_infected,
			percentage_of_population_infected.location
	FROM
		(SELECT
				data_tb.date,
				data_tb.location,
				data_tb.total_cases/data_tb.population * 100 AS percentage_of_population_infected
		FROM
			(SELECT 
					covid_cases.location,
					covid_cases.total_cases,
					covid_country.population,
					LEFT(covid_cases.date, 11) AS date
			FROM [Covid Database schema].[dbo].[CovidCases] AS covid_cases
			LEFT JOIN [Covid Database schema].[dbo].[CovidCountry] AS covid_country
			ON covid_cases.location = covid_country.location
					) AS data_tb
				)AS percentage_of_population_infected
	WHERE percentage_of_population_infected >= 25 
	)AS ranked
WHERE ranked.rk = 1 


-- When Country cross 50% population infected
SELECT *
FROM
	(SELECT
			RANK() OVER (PARTITION BY percentage_of_population_infected.location
						 ORDER BY percentage_of_population_infected,
								  percentage_of_population_infected.date) AS rk,
			percentage_of_population_infected.date,
			percentage_of_population_infected,
			percentage_of_population_infected.location
	FROM
		(SELECT
				data_tb.date,
				data_tb.location,
				data_tb.total_cases/data_tb.population * 100 AS percentage_of_population_infected
		FROM
			(SELECT 
					covid_cases.location,
					covid_cases.total_cases,
					covid_country.population,
					LEFT(covid_cases.date, 11) AS date
			FROM [Covid Database schema].[dbo].[CovidCases] AS covid_cases
			LEFT JOIN [Covid Database schema].[dbo].[CovidCountry] AS covid_country
			ON covid_cases.location = covid_country.location
					) AS data_tb
				)AS percentage_of_population_infected
	WHERE percentage_of_population_infected >= 50 
	)AS ranked
WHERE ranked.rk = 1 


-- When Country cross 75% population infected
SELECT *
FROM
	(SELECT
			RANK() OVER (PARTITION BY percentage_of_population_infected.location
						 ORDER BY percentage_of_population_infected,
								  percentage_of_population_infected.date) AS rk,
			percentage_of_population_infected.date,
			percentage_of_population_infected,
			percentage_of_population_infected.location
	FROM
		(SELECT
				data_tb.date,
				data_tb.location,
				data_tb.total_cases/data_tb.population * 100 AS percentage_of_population_infected
		FROM
			(SELECT 
					covid_cases.location,
					covid_cases.total_cases,
					covid_country.population,
					LEFT(covid_cases.date, 11) AS date
			FROM [Covid Database schema].[dbo].[CovidCases] AS covid_cases
			LEFT JOIN [Covid Database schema].[dbo].[CovidCountry] AS covid_country
			ON covid_cases.location = covid_country.location
					) AS data_tb
				)AS percentage_of_population_infected
	WHERE percentage_of_population_infected >= 75
	)AS ranked
WHERE ranked.rk = 1 


-- When Country cross 100% population infected
SELECT *
FROM
	(SELECT
			RANK() OVER (PARTITION BY percentage_of_population_infected.location
						 ORDER BY percentage_of_population_infected,
								  percentage_of_population_infected.date) AS rk,
			percentage_of_population_infected.date,
			percentage_of_population_infected,
			percentage_of_population_infected.location
	FROM
		(SELECT
				data_tb.date,
				data_tb.location,
				data_tb.total_cases/data_tb.population * 100 AS percentage_of_population_infected
		FROM
			(SELECT 
					covid_cases.location,
					covid_cases.total_cases,
					covid_country.population,
					LEFT(covid_cases.date, 11) AS date
			FROM [Covid Database schema].[dbo].[CovidCases] AS covid_cases
			LEFT JOIN [Covid Database schema].[dbo].[CovidCountry] AS covid_country
			ON covid_cases.location = covid_country.location
					) AS data_tb
				)AS percentage_of_population_infected
	WHERE percentage_of_population_infected >= 100
	)AS ranked
WHERE ranked.rk = 1 




 
