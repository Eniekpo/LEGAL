/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../myapp/**/*.{html,css,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms")({
      strategy: 'base', // only generate global styles
      strategy: 'class', // only generate classes
    }),
  ],
}
