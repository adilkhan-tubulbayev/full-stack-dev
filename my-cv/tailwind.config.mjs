/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				//my colors:
				"peach" : "#FF9B71",
				"royalblue" : "#2660A4",
				"hotpink" : "#F92A82",
				"trueblue" : "#3066BE",
				"thistle" : "#957FEF",
				"emerald" : "#62C370",
				//vars:
				'page-bg': 'var(--page-bg-color)',
        'text-primary': 'var(--text-color)',
        'btn-bg': 'var(--btn-bg-color)',
        'border': 'var(--border-color)',
				'btn-text': 'var(--btn-text)',
			}
		},
	},
	safelist: [
    {
      pattern: /bg-(peach|royalblue|hotpink|trueblue|thistle|emerald)/,
    },
  ],
	plugins: [],
}
