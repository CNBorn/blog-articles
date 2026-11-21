#!/bin/bash
# usage: verify.sh BASE_URL   e.g. http://127.0.0.1:8788  or  https://cnborn.net
# Checks every URL from the old online mirror plus the legacy nginx redirects.
BASE=${1%/}
ONLINE=~/Backups/cnborn-blog-online-20261121
fail=0; n=0
check() { # path expected_status [expected_location_suffix]
  local out code loc
  out=$(curl -s -o /dev/null -w '%{http_code} %{redirect_url}' "$BASE$1")
  code=${out%% *}; loc=${out#* }
  n=$((n+1))
  if [ "$code" != "$2" ] || { [ -n "$3" ] && [[ "$loc" != *"$3" ]]; }; then
    echo "FAIL $1 -> $code $loc (want $2 $3)"; fail=$((fail+1))
  fi
}

# legacy nginx rules
check / 302 /blog/
check /blog/atom.xml 301 /blog/feeds/all.rss.xml
check /blog/about-cnborn.html 301 /blog/pages/about/
check /blog/getting-real-chn.html 301 /docs/getting_real/index.html
check /blog/2016/08/a-year-in-toronto.html 301 /blog/2016/08/a-year-in-toronto/
check /blog/2009/11/cambodia-notes-partone-phnompenh.html 301 /blog/2009/11/cambodia-notes-partone-phnompenh/
check /blog/2016/08/duo-lun-duo-yi-nian/ 301 /blog/2016/08/a-year-in-toronto/
check /blog/index2.html 301 /blog/archives.html
check /blog/category/Event/index3.html 301 /blog/category/Event/
check /blog/lang/cn/ 301 /blog/lang/zh/
check /blog/authors.html 301 /blog/archives.html
check /blog/does-not-exist/ 404

# every non-paginated file that existed online must be 200 (except the ones redirected above)
while read -r f; do
  case "$f" in
    blog/2016/08/duo-lun-duo-yi-nian/*|blog/authors.html|blog/lang/cn/index.html) continue;;
    */index[0-9]*.html) continue;;
  esac
  p="/$f"; p=${p%index.html}
  # percent-encode non-ascii for curl
  enc=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$p")
  case "$p" in *.html) check "$enc" 308;; *) check "$enc" 200;; esac
done < <(cd "$ONLINE" && find . -type f | sed 's#^\./##' | sort)

# headers
curl -sI "$BASE/blog/theme/fonts/DXI1ORHCpsQm3Vp6mXoaTRampu5_7CjHW5spxoeN3Vs.woff2" | grep -qi '^access-control-allow-origin: \*' \
  || { echo "FAIL font CORS header"; fail=$((fail+1)); }
curl -s "$BASE/blog/2016/08/a-year-in-toronto/" | grep -q 'http://cnborn.net' \
  && { echo "FAIL hardcoded http://cnborn.net in article page"; fail=$((fail+1)); }
grep -rl 'http://cnborn.net' "${SITE_DIR:-public}" --include=*.html >/dev/null 2>&1 && echo "note: http://cnborn.net still in built html (see site/)"
echo "checked $n URLs, $fail failures"
