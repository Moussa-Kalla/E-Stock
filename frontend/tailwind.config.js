/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./App.js",
        "./components/**/*.{js,jsx,ts,tsx}",
        "./screens/**/*.{js,jsx,ts,tsx}",
        "./navigation/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                primary: '#1E3A8A',      // Bleu profond
                secondary: '#10B981',    // Vert émeraude
                accent: '#E5E7EB',       // Gris clair
                textPrimary: '#1F2937',  // Gris foncé
                textSecondary: '#6B7280',// Gris moyen
                sky: {
                    400: '#38bdf8',      // Bleu ciel (sky-400)
                },
            },
        },
    },
    plugins: [],
};