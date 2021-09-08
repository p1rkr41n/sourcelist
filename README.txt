//forcesearch.py: 
    command: sudo python3 forcesearch.py [package_name]
    output: sourceslist have this package
    demo: sudo python3 forcesearch.py man-db
//sourceslist.py:
    command: sudo python3 sourceslist.py
    output: search fastest mirror server to connect and apply this
    demo:= command
//addsourceslst.py:
    command: sudo python3 addsourceslst.py [sourceslist_link]
    output: apply needed mirror server to connect
    demo: sudo python3 addsourceslst.py http.kali.org/kali
//reversesourceslst.py:
    command: sudo python3 reversesources.py
    output: revserve old sources.list
    demo: = command
//install_insrc.py
    command: sudo python3 install_insrc.py [package_name] [sourceslist_link]
    output: install package_name ourcelist_link
    demo: sudo python3 install_insrc.py man-db http.kali.org/kali
//search_fastest_package/fast_search.py
    command: sudo python3 fast_search.py [package_name]
    output: sourceslist have this package sort by time
    demo : sudo python3 fast_search.py man-db
