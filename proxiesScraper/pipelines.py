# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ProxiesscraperPipeline:

    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS PROXIES(
                id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                ip text NOT NULL,
                source text NOT NULL
                );
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        self.cur.execute("SELECT ip FROM PROXIES WHERE ip = '%s'" % item['ip'])
        result = self.cur.fetchone()
        if result:
            return item
        else:
            self.cur.execute(f"""
                INSERT INTO PROXIES (ip, source)
                VALUES ('{item['ip']}', '{item['source']}')""")
            self.conn.commit()
            return item
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
