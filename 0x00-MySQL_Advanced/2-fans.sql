-- THE SUM OF FANS OR ALL BANDS THAT ARE IN A SPESIFIC COUNTRY
SELECT  origin, SUM(fans) as nb_fans FROM metal_bands   
  GROUP BY origin
  ORDER BY nb_fans DESC;
