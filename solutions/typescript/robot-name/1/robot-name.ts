export class Robot {
  // Global set to keep track of all names currently in use across all robots
  private static usedNames = new Set<string>();
  
  private _name: string | null = null;

  constructor() {
    // Starts with no name when coming off the factory floor
  }

  // Generates a random name formatted as two uppercase letters and three digits
  private random_name_generator(): string {
    const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const char1 = LETTERS[Math.floor(Math.random() * 26)];
    const char2 = LETTERS[Math.floor(Math.random() * 26)];
    
    // Generates a 3-digit number padded with leading zeros if necessary
    const num = Math.floor(Math.random() * 1000).toString().padStart(3, '0');
    
    return `${char1}${char2}${num}`;
  }

  // Ensures a unique name is generated and registered
  private generate_unique_name(): string {
    let name: string;
    
    do {
      name = this.random_name_generator();
    } while (Robot.usedNames.has(name));
    
    // Register the name in the tracking set to prevent future collisions
    Robot.usedNames.add(name);
    return name;
  }

  // The first time you turn on a robot or ask for its name, a name is generated
  public get name(): string {
    if (!this._name) {
      this._name = this.generate_unique_name();
    }
    return this._name;
  }

  // Resets the robot to factory settings, wiping its name
  public resetName(): void {
    this._name = null;
  }

  // Optional: Clears all tracked names (useful for resetting test suites)
  public static releaseNames(): void {
    Robot.usedNames.clear();
  }
}