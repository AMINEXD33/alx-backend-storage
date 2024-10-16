-- get all bands with Glam rock as a style
-- ranked by their longevity

SELECT 
  band_name, IFNULL(split, 2020) - IFNULL(formed, 0) as lifespan 
FROM 
  metal_bands;