
# CineMatch - Enhanced Movie Recommendation System

## Project Overview

CineMatch is a command-line movie recommendation system written in Python. This project improves the original application by adding new recommendation features and a personal movie watchlist.

The original movie catalog contained 20 movies. The enhanced version contains 50 movies, including additional genres such as Horror, Comedy, and Romance.

## Original Repository

https://github.com/kilobyte23/CineMatch

## Original Features

- Add a new movie with its title, genre, and rating.
- Search for movies by title or genre.
- Recommend the top N movies based on ratings.
- Delete a movie by title.

## New Improvements

### Improvement 1: Genre-Based Movie Recommendations

- Recommend the top three movies in a selected genre.
- Sort movies by rating in descending order.
- Expand the movie catalog from 20 to 50 movies.
- Add Horror, Comedy, and Romance genres.
- Support case-insensitive genre input.

Branch: `genre-recommendation`

### Improvement 2: Personal Movie Watchlist

- Add movies to a personal watchlist.
- View saved movies with their titles, genres, and ratings.
- Remove movies from the watchlist.
- Prevent duplicate movies from being added.
- Display appropriate messages for empty lists and invalid movie titles.

Branch: `personal-watchlist`

### Improvement 3: Random Movie Recommendation

- Randomly recommend a movie from the available catalog.
- Display the movie title, genre, and rating.
- Use Python's built-in random module.
- Handle an empty movie catalog.

Branch: `random-recommendation`

## Installation and Usage

Python 3 is required. No additional packages are needed.

Clone the repository:

```bash
git clone https://github.com/Yuna821112/CineMatch.git
cd CineMatch
```

Run the program:

```bash
python CineMatch.py
```

On Windows, the following command can also be used:

```bash
py CineMatch.py
```

## Program Menu

1. Add a new movie
2. Search for movies by title or genre
3. Recommend top N movies based on rating
4. Delete a movie
5. Recommend top 3 movies by genre
6. Add a movie to my watchlist
7. View my watchlist
8. Remove a movie from my watchlist
9. Random movie recommendation
10. Exit

## Testing

Manual testing was performed in Visual Studio Code.

| Test Case | Result |
| --- | --- |
| Genre-based top 3 recommendations | Passed |
| Lowercase genre input | Passed |
| Invalid genre input | Passed |
| Add movies to watchlist | Passed |
| View watchlist | Passed |
| Duplicate movie prevention | Passed |
| Invalid movie title | Passed |
| Remove movie from watchlist | Passed |
| Empty watchlist | Passed |
| Random movie recommendations | Passed |
| Invalid menu selection | Passed |
| Program exit | Passed |

Integration testing was also performed after merging the three improvements into the main branch.

## GitHub Development Process

Each improvement was developed in a separate feature branch. Changes were tested, committed, pushed to GitHub, and merged into the main branch through individual pull requests.

- Pull Request #1: Genre-Based Movie Recommendations
- Pull Request #2: Personal Movie Watchlist
- Pull Request #3: Random Movie Recommendation

## Limitations

- The application uses a command-line interface.
- Movie data and watchlists are stored in memory and reset when the program closes.
- Movie ratings are predefined and are not updated automatically.
- The application is not connected to Netflix or any external movie database.
- Random recommendations may select the same movie more than once.

## AI Assistance

ChatGPT was used to assist with developing and explaining Python code, troubleshooting errors, and setting up GitHub branches. All changes were implemented and manually tested by me.

I implemented the changes in Visual Studio Code, manually tested the features, and managed the GitHub branches, commits, pull requests, and merges.

## Author

Yuna Choi

University of Nevada, Reno

BAN 701 - GitHub Repository Improvement Project
