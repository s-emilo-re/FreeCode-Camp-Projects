const { useState } = React;

export function Board() {
  const [squares, setSquares] = useState(Array(9).fill(""));
  const [xIsNext, setXIsNext] = useState(true);

  const winningLines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  function calculateWinner(board) {
    for (let line of winningLines) {
      const [a, b, c] = line;

      if (
        board[a] &&
        board[a] === board[b] &&
        board[a] === board[c]
      ) {
        return board[a];
      }
    }

    return null;
  }

  const winner = calculateWinner(squares);
  const isDraw = !winner && squares.every((square) => square !== "");

  function handleClick(index) {
    if (winner || squares[index]) return;

    const nextSquares = [...squares];
    nextSquares[index] = xIsNext ? "X" : "O";

    setSquares(nextSquares);
    setXIsNext(!xIsNext);
  }

  function resetGame() {
    setSquares(Array(9).fill(""));
    setXIsNext(true);
  }

  return (
    <div className="game">
      <h1>🎮 Tic-Tac-Toe</h1>

      <div className="board">
        <div className="board-row">
          {[0, 1, 2].map((i) => (
            <button
              key={i}
              className="square"
              onClick={() => handleClick(i)}
            >
              {squares[i]}
            </button>
          ))}
        </div>

        <div className="board-row">
          {[3, 4, 5].map((i) => (
            <button
              key={i}
              className="square"
              onClick={() => handleClick(i)}
            >
              {squares[i]}
            </button>
          ))}
        </div>

        <div className="board-row">
          {[6, 7, 8].map((i) => (
            <button
              key={i}
              className="square"
              onClick={() => handleClick(i)}
            >
              {squares[i]}
            </button>
          ))}
        </div>
      </div>

      <h2>
        {winner
          ? `Winner: ${winner}`
          : isDraw
          ? "Draw"
          : `Next Player: ${xIsNext ? "X" : "O"}`}
      </h2>

      <button id="reset" onClick={resetGame}>
        Reset Game
      </button>
    </div>
  );
}