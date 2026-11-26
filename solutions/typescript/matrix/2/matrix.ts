export class Matrix {
  private readonly matrixRows: number[][];

  constructor(matrixStr: string) {
    // 1. Split the string into individual rows by newlines
    // 2. Trim whitespace and split each row by any amount of spaces
    // 3. Convert each string token into a number.
    this.matrixRows = matrixStr
      .split('\n')
      .map(row => row.trim().split(/\s+/).map(Number));
  }

  // Getter to return the rows
  get rows(): number[][] {
    return this.matrixRows;
  }

  // Getter to dynamically transpose rows into columns
  get columns(): number[][] {
    if (this.matrixRows.length === 0) return [];

    const numCols = this.matrixRows[0].length;
    const cols: number[][] = [];

    for (let i = 0; i < numCols; i++) {
      cols.push(this.matrixRows.map(row => row[i]));
    }

    return cols;
  }
}
