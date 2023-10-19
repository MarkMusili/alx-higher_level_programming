-- Select all the genres for the show Dexter
SELECT tv_genres.name AS genre
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id  = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genre ASC;
