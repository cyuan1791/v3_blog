# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Dev Commands

```bash
npm run dev       # Start Vite dev server
npm run build     # Type-check (vue-tsc) then build with Vite
npm run preview   # Preview production build
```

No test runner or linter is configured. TypeScript strict mode with `noUnusedLocals` and `noUnusedParameters` enforced via tsconfig.

## Architecture

Vue 3 + TypeScript + Vite SPA blog application styled with Bootstrap 4. No state management library (Vuex/Pinia); data is passed in via the host page.

### Data Flow

The app is designed to be embedded in a larger platform. Blog post data is passed through the global `window.asoneData` property as a base64-encoded JSON string. Components decode it with `JSON.parse(atob(...))`. The Vite config uses a `_PagePath_` placeholder as the base path, replaced at deploy time by the host system.

### Routing

Vue Router in history mode with two routes:
- `/` — Home (post listing)
- `/post/:id` — PostView (single post, where `:id` is a slugified title)

Slugification rule: `title.replace(/\s+/g, '-').replace(/[^a-zA-Z0-9-_]/g, '')`. This is duplicated in `BlogPost.vue` (link generation) and `PostView.vue` (post lookup) — keep them in sync.

### Source Layout

- `src/views/` — Page-level route components (Home.vue, PostView.vue)
- `src/components/` — Reusable components (BlogPost.vue)
- `src/data/posts.json` — Static fallback post data
- `src/router.ts` — Route definitions
- `src/main.ts` — App bootstrap

### Conventions

- Composition API with `<script setup lang="ts">`
- PascalCase component names, camelCase for functions/variables
- `window` object access uses `as any` casts to bypass type checking
