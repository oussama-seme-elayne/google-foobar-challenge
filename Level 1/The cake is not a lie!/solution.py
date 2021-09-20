def sample(leng, split_list):
    for i in range(0, leng-1):

        if(split_list[i] == split_list[i+1]):
            if(i == leng-2):
                return leng
            else:
                continue
        else:
            return 1


def solution(s):
    gem_str = s
    sample_num = 1
    str_length = len(gem_str)  
    for divider_value in range(1, str_length):
        split_list = []
        if(str_length % divider_value == 0):
            for x in range(0, str_length, divider_value):
                split_list.append(gem_str[x:x+divider_value])
            split_list_length = len(split_list)

            sample_num = sample(split_list_length, split_list)
            if(sample_num != 1):
                return sample_num
    return sample_num