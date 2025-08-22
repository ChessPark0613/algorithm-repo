# solution.py

class RESULT:
    def __init__(self):
        self.cnt = -1
        self.IDs = [0] * 5  # 최대 5개

class UserSolution:
    def __init__(self):
        self.movies = None
        self.movie_genre = None
        self.user_score = None

    def init(self, N: int) -> None:
        self.movies = {}
        self.movie_genre = {}
        self.user_score = {}
        return

    def add(self, mID: int, mGenre: int, mTotal: int) -> int:
        if mID in self.movies:
            return 0

        self.movies[mID] = {"genre": mGenre, "total": mTotal}

        if mGenre not in self.movie_genre:
            self.movie_genre[mGenre] = set()
        self.movie_genre[mGenre].add(mID)

        return 1

    def erase(self, mID: int) -> int:
        if mID not in self.movies:
            return 0

        self.movies.remove(mID)
        return 1

    def watch(self, uID: int, mID: int, mRating: int) -> int:
        # TODO: 시청/평점 반영 로직 작성
        return -1

    def suggest(self, uID: int) -> RESULT:
        # TODO: 추천 로직 작성
        res = RESULT()
        res.cnt = -1
        # 필요 시 res.IDs[0..cnt-1] 채우기
        return res
