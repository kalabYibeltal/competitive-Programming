class Solution(object):
    def validIPAddress(self, queryIP):
        
        if any(chr.isalpha() for chr in queryIP):
            if re.findall("[g-zG-Z]", queryIP):
                return "Neither";
            ipChunked = queryIP.split(":")
            if len(ipChunked) != 8:
                return "Neither";
            if any(not(x) or len(x) > 4 for x in ipChunked):
                return "Neither";
            return "IPv6";
        else:
            ipChunked = queryIP.split(".")
            if len(ipChunked) != 4:
                return "Neither";
            if any(not (x) or (x[0] == '0' and len(x)>1) or int(x) > 255 or int(x) < 0 for x in ipChunked):
                return "Neither";
            return "IPv4"
        return "Neither";