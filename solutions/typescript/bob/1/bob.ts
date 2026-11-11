export function hey(message: string): string {

  const trimmed = message.trim();
  if (trimmed === '') return 'Fine. Be that way!';
  
  const isYelling = /[a-zA-Z]/.test(trimmed) && trimmed === trimmed.toUpperCase();
  
  if (isYelling && trimmed.endsWith("?")) {
    return 'Calm down, I know what I\'m doing!';
    }
  
  if (trimmed.endsWith('?')){
    return 'Sure.';
  } else if (isYelling) {
    return 'Whoa, chill out!';
  } else {
    return "Whatever.";
  }
}
