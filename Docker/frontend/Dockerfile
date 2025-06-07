FROM node:22-alpine

WORKDIR /app

RUN npm install -g pnpm

RUN corepack enable

COPY package.json pnpm-lock.yaml .env ./

RUN pnpm install --frozen-lockfile

COPY . ./


EXPOSE ${NUXT_PORT}

CMD ["pnpm", "run", "dev"]