#Problem 811 Subdomain Visit Count
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = dict()
        res = []
        for domain in cpdomains:
            domain_split = domain.split(" ")
            if domain_split[1] not in dictionary:
                dictionary[domain_split[1]] = int(domain_split[0])
            else:
                dictionary[domain_split[1]] = dictionary[domain_split[1]] + int(domain_split[0])
            
            website = domain_split[1].split(".")
            
            for i in range(len(website)-1):
                if i == 0:
                    if dictionary.get(website[(len(website)-1)-i]) == None:
                        dictionary[website[(len(website)-1)-i]] = int(domain_split[0])
                    else:
                        dictionary[website[(len(website)-1)-i]] = dictionary[website[(len(website)-1)-i]] + int(domain_split[0])
                if i == 1:
                    if dictionary.get(website[1] + "." + website[2]) == None:
                        dictionary[website[1] + "." + website[2]]= int(domain_split[0])
                    else:
                        dictionary[website[1] + "." + website[2]] = dictionary[website[1] + "." + website[2]] + int(domain_split[0])

        for key in dictionary:
            res.append("{} {}".format(dictionary[key], key))
        return res