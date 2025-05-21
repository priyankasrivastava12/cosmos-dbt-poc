-- models/fct/fct_listings_and_reviews.sql

WITH
  listings AS (
    SELECT
      *
    FROM
      {{ ref('dim_listings_cleansed') }}
  ),
  reviews AS (
    SELECT
      *
    FROM
      {{ ref('fct_reviews') }}
  )
SELECT
  l.listing_id,
  l.listing_name,
  l.room_type,
  l.minimum_nights,
  l.price,
  l.host_id,
  r.review_date,
  r.reviewer_name,
  r.review_text,
  r.review_sentiment
FROM
  listings l
INNER JOIN
  reviews r
ON
  l.listing_id = r.listing_id