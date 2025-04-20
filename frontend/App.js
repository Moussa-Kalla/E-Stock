import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import AppNavigator from './navigation/AppNavigator';
import { TailwindProvider, useTailwind } from 'tailwindcss-react-native';
import { TouchableOpacity, Text } from 'react-native';

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
          400: '#38bdf8',        // Bleu ciel (sky-400)
        },
      },
    },
  },
  plugins: [],
}

export default function App() {
  return (
    <TailwindProvider>
      <NavigationContainer>
        <AppNavigator />
      </NavigationContainer>
    </TailwindProvider>
  );
}

export function MyButton({ title, onPress }) {
  const tailwind = useTailwind();
  return (
    <TouchableOpacity
      style={tailwind('bg-sky-400 px-4 py-2 rounded')}
      onPress={onPress}
    >
      <Text style={tailwind('text-white font-bold')}>{title}</Text>
    </TouchableOpacity>
  );
}
