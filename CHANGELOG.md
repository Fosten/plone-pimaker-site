# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- You should *NOT* be adding new change log entries to this file.
     You should create a file in the news directory instead.
     For helpful instructions, please see:
     https://6.docs.plone.org/volto/developer-guidelines/contributing.html#create-a-pull-request
-->

<!-- towncrier release notes start -->

## [Unreleased]

- Bump Volto from 19.0.0-alpha.9 to 19.0.0-alpha.24 [fosten]
- Patch volto-form-block to fix the anonymous export in fieldSchema.js [fosten]
- Bump Plone from 6.1.4 to 6.2.0a1 [fosten]

## [2.2.0] (2026-02-12)

- Release 2.2.0 [fosten]
- Bump Plone from 6.1.1 to 6.1.4 [fosten]
- Bump node from 22 to 24 [fosten]
- Add `.mxdev_cache` to .gitignore in backend addons [fosten]
- Update pre-commit version and README.md [fosten]
- Add footer links to CHANGELOG.md [fosten]
- Remove duplicate gzip middleware declarations [fosten]
- Add volto-authomatic, pas.plugins.oidc, pas.plugins.keycloakgroups [fosten]
- Change volto-rss-provider to @plone-collective/volto-rss-provider [fosten]
- Bump Volto from 18.10.1 to 19.0.0-alpha.9 [fosten]

## [2.1.0] (2025-03-30)

- Update CHANGELOG.md [fosten]
- Bump Plone from 6.1.0 to 6.1.1 [fosten]
- Bump Volto from 18.0.0 to 18.10.1 [fosten]
- Update check-python-versions from 0.21.3 to 0.22.1 [fosten]
- Set python_requires to >=3.10 [fosten]
- Switch from z3c.autoinclude.plugin to plone.autoinclude.plugin [fosten]
- Bump Plone from 6.0.13 to 6.1.0 [fosten]
- corepack signature verfication workaround [fosten]
- Add volto-byline [fosten]
- Change traefik.docker to traefik.swarm [fosten]

## [2.0.0] (2024-11-02)

- Rename traefik entrypoints [fosten]
- Bump Volto from 18.0.0-alpha.42 to 18.0.0 [fosten]
- Remove old browserlayer in new install profile [fosten]
- Add kitconcept.seo and enable for Image type [fosten]
- Update .eslintrc.js and storybook/main.js [fosten]
- Add config.resolve.fallback querystring to querystring-es3 [fosten]
- Add mrs.developer to Dockerfile [fosten]
- Add volto-rss-provider and rss_provider [fosten]
- Bump node from 18 to 22 [fosten]
- Refactor using cookieplone [fosten]
- Add towncrier to CHANGELOG.md [fosten]

## [1.2.0] (2024-10-14)

- Update CHANGELOG.md [fosten]
- Remove ports [fosten]
- Add hashed pw var [fosten]
- Add volto-banner and eea.banner [fosten]
- Add collective.listmonk [fosten]
- Add volto-columns-block [fosten]
- Use en-us language variant [fosten]
- FromAsCasing match [fosten]
- Add collective.honeypot [fosten]
- Bump Plone from 6.0.11.1 to 6.0.13 [fosten]
- Remove py38 and py39, add py312 [fosten]
- Bump Volto from 18.0.0-alpha.32 to 18.0.0-alpha.42 [fosten]

## [1.1.0] (2024-05-24)

- Change gocept.pytestlayer to zope.pytestlayer [fosten]
- Add collective.volto.formsupport, volto-form-block, volto-subblocks [fosten]
- Bump Volto from 17.15.5 to 18.0.0-alpha.32 [fosten]
- Bump Plone from 6.0.10.1 to 6.0.11.1 [fosten]
- Remove capital letter @Fosten to @fosten [fosten]
- Add Typescript [fosten]
- Bump Volto from 17.0.0-alpha.23 to 17.15.5 [fosten]
- Add dependabot for automatic updates to Github Actions [fosten]

## [1.0.0] (2023-09-27)

- Add homeassistant env_vars [fosten]
- Update GHA workflow files [fosten]
- Add testing stack [fosten]
- Add release stack [fosten]
- Add kitconcept/docker-stack-deploy GHA [fosten]

## [0.2.0] (2023-08-18)

- Enable JS on 404 [fosten]
- Add matomoSiteId, matomoUrlBase [fosten]
- Override favicon [fosten]
- Bump node from 16 to 18 [fosten]
- Bump Volto from 16.21.3 to 17.0.0-alpha.23 [fosten]
- Bump Plone from 6.0.6 to 6.0.10.1 [fosten]
- Add volto-pimaker-theme and volto-home-assistant via mrs.developer [fosten]

## [0.1.0] (2023-07-19)

- Initial commit [fosten]

[Unreleased]: https://github.com/Fosten/plone-pimaker-site/compare/2.1.0...main
[2.2.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/2.2.0
[2.1.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/2.1.0
[2.0.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/2.0.0
[1.2.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/1.2.0
[1.1.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/1.1.0
[1.0.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/1.0.0
[0.2.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/0.2.0
[0.1.0]: https://github.com/Fosten/plone-pimaker-site/releases/tag/0.1.0
[fosten]: https://github.com/Fosten
