import os
os.environ['PATH'] = os.pathsep + '/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin'

# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Type: Proxy
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don't use any proxy
c.content.proxy = 'http://localhost:8118/'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: Index of this tab. * `{id}`:
# Internal tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page. *
# `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{audio}{index}: {perc}{current_title}'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {
    'DEFAULT': 'https://google.com/search?q={}',
    'google': 'https://google.com/search?q={}',
    'duckduckgo': 'https://duckduckgo.com/?q={}',
    'github': 'https://github.com/search?q={}',
    'npm': 'https://npmjs.com/search?q={}',
    'baidu': 'https://baidu.com/s?wd={}',
    'mijisou': 'https://mijisou.com/search?q={}'
}

# Hide the window decoration.  This setting requires a restart on
# Wayland.
# Type: Bool
# NOTE: How to maximize window after setting hide_decoration to True in OSX?
# 1. :set window.hide_decoration false
# 2. :fullscreen
# 3. :set window.hide_decoration true
# 4. Enter the system Mission Control (press Ctrl+Up)，then drag the
#    qutebrowser window back from the "fullscreen" desktop
# 5. Click or scroll to anywhere with mouse/trackpad to active this window
# 6. Done
c.window.hide_decoration = True

# Bindings for normal mode
config.bind('x', 'tab-close')
config.bind('X', 'undo')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('d', 'scroll-page 0 0.5')
config.bind('u', 'scroll-page 0 -0.5')
config.bind('j', 'scroll-page 0 0.1')
config.bind('k', 'scroll-page 0 -0.1')
config.bind('i', 'enter-mode insert ;; spawn fcitx-remote -t')
config.bind('gi', 'hint inputs --first ;; spawn fcitx-remote -t')
config.bind('p', 'open -- {clipboard}')
config.bind('P', 'open -t -- {clipboard}')
config.unbind('gl')
config.unbind('gr')
config.bind('gj', 'tab-move -')
config.bind('gk', 'tab-move +')
config.bind('<Escape>', c.bindings.default['normal']['<Escape>'] + ' ;; fake-key <Escape> ;; clear-messages ;; jseval --quiet document.getSelection().empty()')
config.bind('<Meta-Ctrl-f>', 'config-cycle window.hide_decoration false true')

# Bindings for insert mode
config.bind('<Ctrl-a>', 'fake-key <Home>', mode='insert')
config.bind('<Ctrl-e>', 'fake-key <End>', mode='insert')
config.bind('<Ctrl-d>', 'fake-key <Delete>', mode='insert')
config.bind('<Ctrl-h>', 'fake-key <Backspace>', mode='insert')
config.bind('<Ctrl-k>', 'fake-key <Ctrl-Shift-Right> ;; fake-key <Backspace>', mode='insert')
config.bind('<Ctrl-f>', 'fake-key <Right>', mode='insert')
config.bind('<Ctrl-b>', 'fake-key <Left>', mode='insert')
config.bind('<Ctrl-n>', 'fake-key <Down>', mode='insert')
config.bind('<Ctrl-p>', 'fake-key <Up>', mode='insert')
config.bind('<Escape>', 'spawn fcitx-remote -t ;; leave-mode ;; fake-key <Escape>', mode='insert')
