export function isPangram(sentence: string): boolean {
  const lower_sentence = sentence.toLowerCase();
  const letter_only = lower_sentence.replace(/[^a-z]/g,'');
  const unique_letters_only = new Set(letter_only);

  return unique_letters_only.size === 26;
}
