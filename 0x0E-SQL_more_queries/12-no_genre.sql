-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
from tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title ASC, genre_id ASC;

