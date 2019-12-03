with recommendations as (
select
  now() as created_at,
  now() as updated_at,
  word1.value as word,
  word2.value as related,
  word2.score - word1.score as score_difference,
  distance(word1.value, word2.value) as distance,
  1 / (distance(word1.value, word2.value) / 15 / (word2.score - word1.score)) as recommendation
from word word1, word word2
where word2.score - word1.score > 0
  and word2.value <> word1.value
  and word1.value between '{lower_bound}' and '{upper_bound}'
order by 3 asc, 7 desc),

ordered_recommendations as (
select
  *,
  row_number() over (partition by recommendations.word order by recommendations.recommendation desc) as rn
from recommendations)

insert into related_word
(
  select
    created_at,
    updated_at,
    word,
    related,
    score_difference,
    distance,
    recommendation
  from ordered_recommendations
  where rn <  25
) on conflict do nothing
