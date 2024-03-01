sample_list=[11,45,11,8,23,45,78,23,56]
count_dict=dict()
for i in sample_list:
    count=sample_list.count(i)
    count_dict[i]=count
print(count_dict)