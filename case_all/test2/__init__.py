import pymysql
pymysql.version_info = (1, 4, 0, "final", 0)  # mysql指定本地版本
pymysql.install_as_MySQLdb()