-- Display tv_shows based on their genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE EXISTS (
    SELECT 1
    FROM tv_show_genres AS tsg
    WHERE tsg.show_id = tv_shows.id
)
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
