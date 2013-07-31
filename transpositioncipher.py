#common_bigrams = ['E_', 'D_', 'ES', 'RE','_A', 'TI', 'AT', 'IO','ON', 'AN', 'ND', '_I','IN', 'EN', 'N_', 'ME','_T', 'TH', 'AL', 'ER','S_', 'NT', 'HE', '_O']
#common_trigrams = ['_TH','ION','ND_','AND','_AN','THE','TIO','IN_','ENT','HE_','___','MEN','AL_','ATI','OF_','_OF','ON_','ING','_CO','ES_','NG_','TO_','PRO','_TO']

##############
#
# Transposition decryptor
#
# By Scott Schultz
#
# Given a transposited string, and a starting permutation block length, will generate a dictionary of decending block lengths
# then prompt for which block contains an identifiable anagramed word.
# The script will then ask for an order to use and return the decrypted string.
#
##############
class DetermainBlocks:
    period_length = 2
    block_dict = {}
    def __init__(self,arg_counter=5):
        block_list = []
        counter = 0
        while (counter<len(encrypted_string)):
            block_list.append([encrypted_string[counter:counter+arg_counter]])
            counter = counter+arg_counter
        print ">>Block length %d:" %(arg_counter)
        last_block_length = len(block_list[len(block_list)-1:][0][0])
        if last_block_length < arg_counter:
            block_list[len(block_list)-1:][0][0] = block_list[len(block_list)-1:][0][0]+("_"*(arg_counter-last_block_length))
        print block_list
        print

        self.block_dict[arg_counter] = block_list
        if arg_counter > 2:
            DetermainBlocks(arg_counter-1)
        else:
            print ">> Block dictionary created"
            print
            self.getPermuteActionInput()
            
    def getPermuteActionInput(self):
        permute_action = input("Can you see any words in any of those lists? If you can, tell me which block, if not, enter 0:")
        if permute_action > 0:
            self.displayBlockList(permute_action)
        else:
            print
            period_count = input("Enter a new period length. (If you enter nothing I'll assume 5): ")
            DetermainBlocks(period_count)

    def displayBlockList(self,permute_action):
        print
        print ">> Displaying block list %d:" %(permute_action)
        print self.block_dict[permute_action]
        print
        position_list = []
        list_length = permute_action
        while (list_length >= 1):
            position_list.append(input("What position should be in the first space? (so if the block is [_EHT], then the letter T (position 4) should be in position 1)")-1)
            list_length = list_length-1
        print
        print ">> Trying new block order:"+str(position_list)
        self.permuteBlock(permute_action,position_list)
                
    def permuteBlock(self,block_length,block_order):
        decrypted_string = ''
        for block in self.block_dict[block_length]:
            block = list(block[0])
            block = [ block[i] for i in block_order ]
            block = "".join(block)
            decrypted_string = decrypted_string+block
        print "Does this look right?"
        print decrypted_string
        correct_decrypt = raw_input("Y/N: ")
        if correct_decrypt == 'N' or correct_decrypt == 'n':
            period_count = input("Enter a new period length. (If you enter nothing I'll assume 5): ")
            DetermainBlocks(period_count)
        else:
            quit()

##################################
            
encrypted_string = raw_input("Please enter a transposited string: ").strip().upper()
period_count = input("Whats the highest period length to check? (If you enter nothing I'll assume 5): ")
DetermainBlocks(period_count)
print       

