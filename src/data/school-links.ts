export interface SchoolLink {
  label: string;
  href: string;
}

export const schoolLinks: Partial<Record<string, SchoolLink[]>> = {};