
from string import ascii_lowercase


class WearGroup():

    alpha = []
    total_count = 0
    max_pair = 0

    def __init__(self):
        self.start()

    def start_pairing(self, alpha_first):
        bucket = []
        bucket.append(alpha_first)
        for x in self.alpha:
            if x not in bucket:
                bucket.append(x)
                self.total_count += 1
                # total_count+=1
        
        print(bucket)


    def start(self):
        # print(ascii_lowercase, type(ascii_lowercase))
        self.max_pair = len(ascii_lowercase)
        total_count = 0
        for c in ascii_lowercase:
        # print(c)
            self.alpha.append(c)


        print(self.alpha)


        # total_group = 0
        # group_bucket = []
        for x in self.alpha:
            
            self.start_pairing(x)
            # start pairing
            # have a, b, c then   a,b,c,ab,ac,bc  return 6 
        #     start_pairing(x)
        #     temp = []
        #     for y in alpha:
        #         if x != y:
        #             temp.append({x:y}) # add to group if not exist
        #             total_group += 1


        #     group_bucket.append(temp)

        print(self.total_count)
        # print(group_bucket, total_group)

        


x = WearGroup()
