const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    matomoSiteId: '3',
    matomoUrlBase: 'https://stats.pimaker.org/',
    showPloneLogin: false,
    serverConfig: {
      ...config.settings.serverConfig,
      extractScripts: {
        ...config.settings.serverConfig.extractScripts,
        errorPages: true,
      },
    },
  };
  return config;
};

export default applyConfig;
