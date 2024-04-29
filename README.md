# HSS

* HSS is responsive and single page design theme for [Pelican](http://getpelican.com), it is my hack of a Giulio Fidente's [gfidente/pelican-svbhack](https://github.com/gfidente/pelican-svbhack) theme.
* HSS is "H"ack to "S"ingle-page-layout of "S"VBHACK.

:warning: This theme requires Pelican 4.0.0 or newer.

## Screenshot&Demo

You can see the [my site](https://memo.laughk.org).

index                     | content
--------------------------|---------------------------
![image](screenshot1.png) | ![image](screenshot2.png)

## INSTALL

Clone the [repository](https://github.com/laughk/pelican-hss), edit your `pelicanconf.py` and modify the `THEME` variable to make it point to the downloaded theme location.

## PELICANCONF.PY

- `GOOGLE_ANALYTICS` to use Google Analytics, set this var to your ID ("UA-..." or "G-...") code
- The following values are intended for use Google Adsens(only responsive).

  - `GOOGLE_ADSENSE_CLIENT`: `ca-pub-XXXXXXXXX` at `data-ad-client`.
  - `GOOGLE_ADSENSE_SLOT`: value at `data-ad-slot`

  ex.
  ```python
  GOOGLE_ADSENSE_CLIENT = 'ca-pub-xxxxxxxxxxxxxxxx'
  GOOGLE_ADSENSE_SLOT   = 'xxxxxxxxx'
  ```

- `USER_LOGO_URL` to replace the logo placeholder, put your logo in content/images/your_logo.png and make this var point to `SITEURL + '/static/images/your_logo.png'`
- `DISQUS_SITENAME` set this to your Disqus sitename to enable disqus comments in articles
- `TAGLINE` some text rendered right below the logo
- `INTERNET_DEFENSE_LEAGUE` set this to `True` if you want to enable the [Internet Defense League](http://internetdefenseleague.org) code
- `SHOW_SOCIAL_SHARE_BUTTON` to use social share button. set this var to `True`.
- `SOCIAL_SHARE_BUTTONS` to choice social media for  

  from the following.
    - `twitter`: [twitter](https://about.twitter.com/ja/resources/buttons)
    - `x_twitter` : Same as `twitter` except icon and domain.
    - `facebook`: [facebook share link](https://developers.facebook.com/docs/sharing/web)
    - `pocket`: [pocket button](https://getpocket.com/publisher/button)
    - `hatebu`: [hatena bookmark](http://b.hatena.ne.jp/guide/bbutton)
    - `bsky`: [Bluesky Social(bsky.app)][https://bsky.app/]

  ex.
  ```python
  SHOW_SOCIAL_SHARE_BUTTON = True
  SOCIAL_SHARE_BUTTONS = (
      'twitter', 'x_twitter', 'facebook', 'hatebu', 'pocket', 'bsky',
  )
  ```
- `CUSTOM_CSS_URL` (Default: `None`)

  if you want to customize to stylesheet, you add css file by your hosting and seting url to this value.

  ex.

  make `custom.css` to `/path/to/your-pelican-project/content/extra/custom.css`  
  and add to `pelicanconf.py`

  ```python
  # set custom.css url.
  CUSTOM_CSS_URL = '/static/custom.css'

  # add `extra` to STATIC_PATHS.
  STATIC_PATHS = [ 'extra', 'images', ]

  # set url of custom.css to EXTRA_PATH_METADATA.
  EXTRA_PATH_METADATA = {

      -- -- snip -- --

      'extra/custom.css': {'path': 'static/custom.css'},
  }
  ```

  or you can use your hosting url path.  
  so use your hosting url, there is no need to set `STATIC_PATHS` , `EXTRA_PATH_METADATA`.

  ```python
  # set custom.css url.
  CUSTOM_CSS_URL = 'https://your-hosting.example.com/path/to/custom.css'
  ```
- `HSS_TWITTER_CARD` to enable twitter card for your site. set this var to `True`.
  - `HSS_TWITTER_CARD_TWITTER_ID` twitter_id for TWITTER_CARD, if you want. (optional)
- `HSS_DEFAULT_OGP_IMAGE_URL` for default ogp image of your site by URL.


## How to set an ogp image by articles

if you want to set an ogp image by articles, set below parameters as file metadata.

- `ogp_image_url` (URL): set an url path that you want to use as an ogp image.  
- `twitter_card_large` (bool, default: false): set "true" if you want to ogp image as "summary_large_image".

ex.
```markdown
Title: My super title
Date: 2022-02-05 10:20

 ... snip ....

ogp_image_url: https://example.com/path/to/your_ogp_image.png
twitter_card_large: true
```

## MODIFICATIONS

- A different Pygmentize theme can be used by editing `./Makefile` and running `make pygments`.

## AUTHOR

* [HSS](https://github.com/laughk/pelican-hss) is authored by Kei Iwasaki.
* [pelican-svbhack](https://github.com/gfidente/pelican-svbhack) is authored by Giulio Fidente.


## LICENSE

Released under MIT License, full details in `LICENSE` file.
