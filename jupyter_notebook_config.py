
c.ServerProxy.servers = {
  'xpra': {
      'command': ['xpra', 'start', ':11', '--bind-tcp=0.0.0.0:{port}', '--html=on']
  }
}

