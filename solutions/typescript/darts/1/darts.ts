export function score(x: number, y: number): unknown {
  const radius = Math.hypot(x,y)
  let points = null;
  
  if (radius <= 1) {
    points = 10
  } else if (radius <= 5) {
    points = 5
  } else if (radius <= 10) {
    points = 1
  } else {
    points = 0
  }
  return points
}

