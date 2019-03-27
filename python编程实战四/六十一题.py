audlence_ratlng_list = [("《Give up,hold on to me》收视率","1.4%"),("《The private dishes of the husbands》收视率","1.343%"),("《My father-in-lawwill do martiaiarts》收视率","0.92%"),("《North Canton still believe in love》收视率","0.862%"),("《Impossible task》 收视率","0.553%"),("《Sparrow》收视率","0.411%"),("《East of dream Avenue》收视率","0.164%"),("《The prodigal son of the new frontier town》收视率","0.259%"),("《Distant distance》收视率","0.394%"),("《Music legend》收视率","0.562%")]
for subscript in range(0,len(audlence_ratlng_list)):
    for subscript1 in range(subscript+1,len(audlence_ratlng_list)):
#        if audlence_ratlng_list[subscript][1][0:3]>audlence_ratlng_list[subscript1][1][0:3]:从小到大
        if audlence_ratlng_list[subscript][1][0:3]<audlence_ratlng_list[subscript1][1][0:3]:
            audlence_ratlng_list[subscript],audlence_ratlng_list[subscript1]=audlence_ratlng_list[subscript1],audlence_ratlng_list[subscript]
#print(audlence_ratlng_list)
for individual_rating in audlence_ratlng_list:
    print(individual_rating[0],individual_rating[1])

