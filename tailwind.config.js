module.exports = {
  mode: 'jit',
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': ['Inter', 'sans-serif'],
    },
    extend: {
      opacity: ['disabled'],
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
