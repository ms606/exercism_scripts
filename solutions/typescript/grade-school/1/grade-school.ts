export class GradeSchool {
  private roster_names: Map<number, string[]>;

  constructor() {
    this.roster_names = new Map<number, string[]>();
  }


  roster(): Record<number, string[]> {
    const result: Record<number, string[]> = {};
    const sortedGrades = Array.from(this.roster_names.keys()).sort((a, b) => a - b);

    for (const grade of sortedGrades) {
      const students = this.roster_names.get(grade) || [];
      result[grade] = [...students].sort((a, b) => a.localeCompare(b));
    }
    return result;
  }

  add(name: string, grade: number): string | boolean {
    for (const [currentGrade, students] of this.roster_names.entries()) {
      const index = students.indexOf(name);
      if (index !== -1) {
        students.splice(index, 1);
      }
    }

    if (!this.roster_names.has(grade)) {
      this.roster_names.set(grade, []);
    }

    this.roster_names.get(grade)!.push(name);
    return "OK.";
  }

  grade(grade_num: number): string[] {
    const students = this.roster_names.get(grade_num) || [];
    return [...students].sort((a, b) => a.localeCompare(b));
  }
}
