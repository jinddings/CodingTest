function solution(maps) {
  var answer = 0;

  let row_len = maps.length;
  let col_len = maps[0].length;
  let visited = Array.from(new Array(row_len), () =>
    new Array(col_len).fill(false)
  );
  let dist = Array.from(new Array(row_len), () => new Array(col_len).fill(1));
  let dr = [0, 1, 0, -1];
  let dc = [1, 0, -1, 0];

  function isValid(r, c) {
    return r >= 0 && r < maps.length && c >= 0 && c < maps[0].length;
  }

  function bfs(r, c) {
    visited[r][c] = true;
    let queue = [[r, c]];
    while (queue.length) {
      const [cur_r, cur_c] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const next_r = cur_r + dr[i];
        const next_c = cur_c + dc[i];
        if (isValid(next_r, next_c)) {
          if (!visited[next_r][next_c] && maps[next_r][next_c] == 1) {
            queue.push([next_r, next_c]);
            visited[next_r][next_c] = true;
            dist[next_r][next_c] = dist[cur_r][cur_c] + 1;
          }
        }
      }
    }
    return -1;
  }

  answer = bfs(0, 0);
  return dist[maps.length - 1][maps[0].length - 1] === 1
    ? -1
    : dist[maps.length - 1][maps[0].length - 1];
}
