def get_template_by_dataset(dataset_name):
    ## a prompt can be described as template_l+text_data+template_r
    ## template_l would used in pretrain
    ## template_r used for infer on downstream task
    ## pretrain and downstream task share same template_l
    if(dataset_name=='arxiv'):
        template_l = "Here is a paper published on arXiv. The abstract reads as follows: \n\n"
        template_r = ".\n\nQuestion: Based on the abstract above, this paper is published on \"___\" subject on Arxiv.\nAnswer: \""
    elif(dataset_name == 'instagram'):
        template_l = "Here are an account on Instagram, and its personal profile reads: \n\n"
        template_r = ".\n\nQuestion: Based on the profile provided , this account is a \"___\" (answer in one word) account on Instagram.\nAnswer: \""
    elif(dataset_name == 'reddit'):
        template_l = "It is a user on Reddit, and his last 3 posts are: \n\n"
        template_r = ".\n\nQuestion: Based on the given posts, the style of this user is \"___\" (answer in one word).\nAnswer: \""
    else:
        raise "template of this dataset are not registered, please modifing the prompt_config.py"
        
    return template_l,template_r
