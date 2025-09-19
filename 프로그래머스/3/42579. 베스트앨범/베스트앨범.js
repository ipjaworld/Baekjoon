function solution(genres, plays) {
    // 1. 장르별 총 재생수와 노래 목록 세기
    const genrePlayCount = {};
    const songsByGenre = {};

    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i];

        // 총 재생수
        genrePlayCount[genre] = (genrePlayCount[genre] || 0) + play;

        // 노래 목록
        if (!songsByGenre[genre]) songsByGenre[genre] = [];
        songsByGenre[genre].push({ index: i, play });
    }

    // 2. 장르 정렬 (총 재생수 기준)
    const sortedGenres = Object.keys(genrePlayCount)
        .sort((a, b) => genrePlayCount[b] - genrePlayCount[a]);

    // 3. 장르별 노래 정렬 및 선택
    const result = [];
    for (let genre of sortedGenres) {
        const sortedSongs = songsByGenre[genre].sort((a, b) => {
            if (b.play === a.play) return a.index - b.index;
            return b.play - a.play;
        });

        // 최대 2곡만 선택
        result.push(sortedSongs[0].index);
        if (sortedSongs[1]) result.push(sortedSongs[1].index);
    }

    return result;
}