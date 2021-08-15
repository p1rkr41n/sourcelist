//forcesearch.py: 
    command: sudo python3 forcesearch.py [packages_name]
    output: sourceslist have this package
//sourceslist.py:
    command: sudo python3 sourceslist.py
    output: search fastest mirror server to connect and apply this
//addsourceslst.py:
    command: sudo python3 addsourceslst.py [sourceslist_link]
    output: apply needed mirror server to connect
//reversesourceslst.py:
    command: sudo python3 reversesources.py
    output: revserve old sources.list
