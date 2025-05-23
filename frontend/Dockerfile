# syntax=docker/dockerfile:1
ARG VOLTO_VERSION
FROM plone/frontend-builder:${VOLTO_VERSION} as builder

COPY --chown=node packages/volto-pimaker-site /app/packages/volto-pimaker-site
COPY --chown=node volto.config.js /app/
COPY --chown=node package.json /app/package.json.temp
COPY --chown=node mrs.developer.json /app/
COPY --chown=node pnpm-workspace.yaml /app/

RUN --mount=type=cache,id=pnpm,target=/app/.pnpm-store,uid=1000 <<EOT
     python3 -c "import json; data = json.load(open('package.json.temp')); deps = data['dependencies']; data['dependencies'].update(deps); json.dump(data, open('package.json', 'w'), indent=2)"
     rm package.json.temp
     pnpm dlx mrs-developer missdev --no-config --fetch-https
     pnpm install && pnpm build:deps
     pnpm build
     pnpm install --prod
EOT

FROM plone/frontend-prod-config:${VOLTO_VERSION}

LABEL maintainer="Brian Davis <info@pimaker.org>" \
      org.label-schema.name="plone-pimaker-site-frontend" \
      org.label-schema.description="Plone PiMaker Site frontend image." \
      org.label-schema.vendor="Brian Davis"

COPY --from=builder /app/ /app/
