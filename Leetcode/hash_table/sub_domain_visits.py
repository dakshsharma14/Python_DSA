from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Dictionary to store the counts for each subdomain
        domain_counts = {}

        for cpdomain in cpdomains:
            # Split the count and the domain
            count, domain = cpdomain.split()
            count = int(count)

            # Split the domain into its parts
            subdomains = domain.split('.')

            # Generate all subdomains and accumulate their counts
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_counts[subdomain] = domain_counts.get(subdomain, 0) + count

        result = [f"{count} {domain}" for domain, count in domain_counts.items()]
        return result