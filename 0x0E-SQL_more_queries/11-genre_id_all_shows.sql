-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_show_genre.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genre  ON tv_shows.id = tv_show_genre.show_id
ORDER BY title ASC, genre_id ASC;
