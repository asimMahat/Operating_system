#getting python modules
import time
import multiprocessing

#Initial bank balance at my account

#RESOURCE
my_bank_balance = multiprocessing.Value("i",20000) #initally I have 20 thousand at my account

#PROCESS :1
#func to withdraw 10,000
def withdraw_for_pocket_money(money_in_the_bank):
    
    for i in range(10000):
        money_in_the_bank.value = money_in_the_bank.value - 1
    return money_in_the_bank

#PROCESS :2
#making a fucntion to deposit 20,000 more 
def deposit_for_fee(money_in_the_bank):
    
    for i in range(20000):
        money_in_the_bank.value = money_in_the_bank.value + 1
    return money_in_the_bank

money_deposit=multiprocessing.Process(target=deposit_for_fee, args=(my_bank_balance,))
money_withdraw=multiprocessing.Process(target=withdraw_for_pocket_money, args=(my_bank_balance,))

if __name__=="__main__":
    
    money_deposit.start()
    money_withdraw.start()
    money_deposit.join()
    money_withdraw.join()

    #printing out the remainig sum after money deopsit and money withdrawal is done
    print("Your remaining balance is : NRs", my_bank_balance.value)

    '''After two process completes the remaining sum should be 30,000 but same 
       resource 'my_bank_balance' is shared by two resources resulting race condtion.'''