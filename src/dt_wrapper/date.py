from datetime import date
from datetime import datetime
import re


class DateException(Exception):
    pass


class Date(datetime):

    def to_string(self,format):
        return self.strftime(format)
    
    def str2date(self, string_format):
        format_type = None
        date_with_month_name_and_space = re.compile(r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec){1}\s\d{2}\s\d{4}\s\d{2}:\d{2}:\d{2})")
        date_with_month_name_and_slash = re.compile(r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec){1}/\d{2}/\d{4})")
        month_only = re.compile(r"January|Febuary|March|April|May|June|July|August|September|October|November|December")
        full_month_date_with_space_and_comma = re.compile(r"((January|Febuary|March|April|May|June|July|August|September|October|November|December){1}\s\d{2},\s\d{4})")
        date_with_dash = re.compile(r"\d{4}-\d{2}-\d{2}")
        if date_with_dash.findall(string_format):
            format_type = "%Y-%m-%d"
        
        if date_with_month_name_and_space.findall(string_format):
            format_type = "%b %d %Y %H:%M:%S"
        
        if date_with_month_name_and_slash.findall(string_format):
            format_type = "%b/%d/%Y"

        if month_only.findall(string_format):
            format_type = "%B"
        
        if full_month_date_with_space_and_comma.findall(string_format):
            format_type = "%B %d, %Y"

        if format_type == None:
            raise DateException("string is not formated correctly: ")

        return self.strptime(string_format, format_type)






if __name__ == "__main__":
    date = Date.now()
    print(date.to_string("%Y-%m-%d"))
    print(date.str2date("2019-08-02"))
    print(date.str2date("Jan 31 2020 08:32:12"))
    print(date.str2date("Jan/31/2020"))
    print(date.str2date("January"))
    print(date.str2date("January 31, 2019"))