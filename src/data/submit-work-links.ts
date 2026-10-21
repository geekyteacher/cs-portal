export interface SubmitWorkLink {
  label: string;
  href: string;
}

export const submitWorkLinks: Partial<Record<string, SubmitWorkLink[]>> = {
  year5: [
    {
      label: 'Maple Class',
      href: 'https://cishool-my.sharepoint.com/:f:/g/personal/simon_farren_cischool_edu_pl/IgC0DY4fmsAbRL9_ZbYsxFMAAbs73Jlp8XCj7HebJ87_NL0',
    },
    {
      label: 'Willow Class',
      href: 'https://cishool-my.sharepoint.com/:f:/g/personal/simon_farren_cischool_edu_pl/IgAYH_Z_faTjT7IMY_Rmr00WAVNJ7JpogsWV2pUSg-YQL2o',
    },
    {
      label: 'Balmoral (WIPS)',
      href: 'https://cishool-my.sharepoint.com/:f:/g/personal/simon_farren_cischool_edu_pl/IgC04XjyMGyrRZyTt8Tg_hFNAfefPU0m-K7udyrIQGjwg7I',
    },
  ],
};
