#========================================================================
# Python library imports
#========================================================================
import math
import pandas as pd
import operator as op
from functools import reduce


#========================================================================
# Function to compute the combinatorics of given n & r
#========================================================================
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  
  
  
#========================================================================
# Generic function to calculate binomial function
#========================================================================
def binomial(n, p, x, k=2):
  probability_for_p = ncr((k-1)*n,x) * math.pow(p,x) * math.pow((1-p),((k-1)*n)-x)
  return probability_for_p


def single_sampling_plan(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2):
  '''
  Input: User specified values - AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2
  Function: Computes the probability for both p1 & p2 for each pair of (n,c)
                  using the single sampling plan formula, derives alpha & beta values 
                  from the computed probabilities, tests if the derived values are 
                  within user specified range (low and high) and returns all that
                  satisfy this criteria as admissible plan(s)
  Output: Admissible plan(s) as a dataframe
  '''
  single_plans_df = pd.DataFrame()
  for c in range(0, 15):
    for n in range(5, 501):
      probability_for_p1 = 0
      probability_for_p2 = 0
      for x in range(c+1):
        probability_for_p1 = probability_for_p1 + binomial(n=n, p=p1, x=x) 
        probability_for_p2 = probability_for_p2 + binomial(n=n, p=p2, x=x) 
      tempalpha = 1 - probability_for_p1
      tempbeta = probability_for_p2
      if ((tempbeta <= BetaHigh) and (BetaLow <= tempbeta) and 
          (tempalpha <= AlphaHigh) and (AlphaLow <= tempalpha)):
        tempalphaplusbeta = tempalpha + tempbeta
        single_plans_df = single_plans_df.append({"n":n, "c":c, "Alpha":tempalpha,
                                                  "Beta":tempbeta, 
                                                  "Alpha+Beta":tempalphaplusbeta}, 
                                                   ignore_index=True)
        break
  return single_plans_df


#========================================================================
# Function definition for ChSP-1
#========================================================================
def chsp_1(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2):
  '''
  Input: User specified values - AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2
  Function: Computes the probability for both p1 & p2 for each pair of (n,i)
            using the ChSP-1 formula, derives alpha & beta values 
            from the computed probabilities, tests if the derived values are 
            within user specified range (low and high) and returns all that
            satisfy this criteria as admissible plan(s)
  Output: Admissible plan(s) as a dataframe
  '''
  
  chsp_1_df = pd.DataFrame()
  probability_for_p1 = 0
  probability_for_p2 = 0
  c1 = 0
  c2 = 1
  for n in range(5, 501):
    for i in range(0, 21):
      probability_one_for_p1 = 0
      probability_two_for_p1 = 0
      probability_one_for_p2 = 0
      probability_two_for_p2 = 0
      for x1 in range(c1+1):
        probability_one_for_p1 = probability_one_for_p1 + binomial(n=n, p=p1, x=x1)
        probability_one_for_p2 = probability_one_for_p2 + binomial(n=n, p=p2, x=x1)
      for x2 in range(c1+1, c2+1):
        probability_two_for_p1 = probability_two_for_p1 + binomial(n=n, p=p1, x=x2)
        probability_two_for_p2 = probability_two_for_p2 + binomial(n=n, p=p2, x=x2)
      probability_for_p1 = probability_one_for_p1 + (probability_two_for_p1 * math.pow(probability_one_for_p1, i))
      probability_for_p2 = probability_one_for_p2 + (probability_two_for_p2 * math.pow(probability_one_for_p2, i))
      tempalpha = 1 - probability_for_p1
      tempbeta = probability_for_p2
      if ((tempbeta <= BetaHigh) and (BetaLow <= tempbeta) and 
          (tempalpha <= AlphaHigh) and (AlphaLow <= tempalpha)):
        tempalphaplusbeta = tempalpha + tempbeta
        chsp_1_df = chsp_1_df.append({"n":n, "i":i, 
                                    "Alpha":tempalpha, "Beta":tempbeta, 
                                    "Alpha+Beta":tempalphaplusbeta}, 
                                    ignore_index=True)
        break
  return chsp_1_df


#========================================================================
# Function definition for ChSP-4(c1,c2)
#========================================================================
def chsp_4(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2):
  '''
  Input: User specified values - AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2
  Function: Computes the probability for both p1 & p2 for each pair of (n,c1,c2,k)
            using the ChSP-4 formula, derives alpha & beta values 
            from the computed probabilities, tests if the derived values are 
            within user specified range (low and high) and returns all that
            satisfy this criteria as admissible plan(s)
  Output: Admissible plan(s) as a dataframe
  '''
  
  chsp_4_df = pd.DataFrame()
  for c1 in range(0, 6):
    for c2 in range(c1+1, c1+6):
      for n in range(5, 501):
        for k in range(2, 21):
          probability_one_for_p1 = 0
          probability_two_for_p1 = 0
          probability_one_for_p2 = 0
          probability_two_for_p2 = 0
          for x1 in range(c1+1):
            probability_one_for_p1 = probability_one_for_p1 + binomial(n=n, p=p1, x=x1)
            probability_one_for_p2 = probability_one_for_p2 + binomial(n=n, p=p2, x=x1)
          for x2 in range(c1+1, c2+1):
            probability_k_for_p1 = 0
            probability_k_for_p2 = 0
            for y in range((c2-x2)+1):
              probability_k_for_p1 = probability_k_for_p1 + binomial(n=n, p=p1, x=y, k=k)
              probability_k_for_p2 = probability_k_for_p2 + binomial(n=n, p=p2, x=y, k=k)
            probability_two_for_p1 = probability_two_for_p1 + (binomial(n=n, p=p1, x=x2) * probability_k_for_p1)
            probability_two_for_p2 = probability_two_for_p2 + (binomial(n=n, p=p2, x=x2) * probability_k_for_p2)
          probability_for_p1 = probability_one_for_p1 + probability_two_for_p1
          probability_for_p2 = probability_one_for_p2 + probability_two_for_p2
          tempalpha = 1 - probability_for_p1
          tempbeta = probability_for_p2
          if ((tempbeta <= BetaHigh) and (BetaLow <= tempbeta) and 
              (tempalpha <= AlphaHigh) and (AlphaLow <= tempalpha)):
            tempalphaplusbeta = tempalpha + tempbeta
            chsp_4_df = chsp_4_df.append({"n":n, "c1":c1, "c2":c2, "k":k, 
                                          "Alpha":tempalpha, "Beta":tempbeta, 
                                          "Alpha+Beta":tempalphaplusbeta}, 
                                         ignore_index=True)
            break
  return chsp_4_df


#========================================================================
# Function definition for MDS-1(c1,c2)
#========================================================================
def mds_1(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2):
  '''
  Input: User specified values - AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2
  Function: Computes the probability for both p1 & p2 for each pair of (n,c1,c2,i)
            using the MDS-1 formula, derives alpha & beta values 
            from the computed probabilities, tests if the derived values are 
            within user specified range (low and high) and returns all that
            satisfy this criteria as admissible plan(s)
  Output: Admissible plan(s) as a dataframe
  '''
  
  mds_1_df = pd.DataFrame()
  for c1 in range(0, 6):
    for c2 in range(c1+1, c1+6):
      for n in range(5, 501):
        for i in range(0, 21):
          probability_one_for_p1 = 0
          probability_two_for_p1 = 0
          probability_one_for_p2 = 0
          probability_two_for_p2 = 0
          for x1 in range(c1+1):
            probability_one_for_p1 = probability_one_for_p1 + binomial(n=n, p=p1, x=x1)
            probability_one_for_p2 = probability_one_for_p2 + binomial(n=n, p=p2, x=x1)
          for x2 in range(c1+1, c2+1):
            probability_two_for_p1 = probability_two_for_p1 + binomial(n=n, p=p1, x=x2)
            probability_two_for_p2 = probability_two_for_p2 + binomial(n=n, p=p2, x=x2)
          probability_for_p1 = probability_one_for_p1 + (probability_two_for_p1 * math.pow(probability_one_for_p1, i))
          probability_for_p2 = probability_one_for_p2 + (probability_two_for_p2 * math.pow(probability_one_for_p2, i))
          tempalpha = 1 - probability_for_p1
          tempbeta = probability_for_p2
          if ((tempbeta <= BetaHigh) and (BetaLow <= tempbeta) and 
              (tempalpha <= AlphaHigh) and (AlphaLow <= tempalpha)):
            tempalphaplusbeta = tempalpha + tempbeta
            mds_1_df = mds_1_df.append({"n":n, "c1":c1, "c2":c2, "i":i, 
                                        "Alpha":tempalpha, "Beta":tempbeta, 
                                        "Alpha+Beta":tempalphaplusbeta}, 
                                       ignore_index=True)
            break
  return mds_1_df


#====================================================================
# Main function of the program
#====================================================================
def sampling_plans():
  '''
  Input: None
  Function: Provides user with a choice to select a sampling plan and based on the
            user selection, calls the corresponding plan function and outputs the
            optimum plan
  Output: Optimum plan as a dataframe
  '''

  print('''Select the number to run sampling plan of your choice:\n 
        1.Single Sampling plan\n 
        2.ChSP-1\n 
        3.ChSP-4(c1,c2)\n 
        4.MDS-1(c1,c2)\n''')
  user_selection = int(input("Enter the number to run the sampling plan of your choice:"))
  if user_selection > 4:
    print("\nInvalid selection, please select from the list")
    sampling_plans()
  else:
    AlphaLow = float(input("Enter the value for AlphaLow: "))
    AlphaHigh = float(input("Enter the value for AlphaHigh: "))
    BetaLow = float(input("Enter the value for BetaLow: "))
    BetaHigh = float(input("Enter the value for BetaHigh: "))
    p1 = float(input("Enter the value for p1: "))
    p2 = float(input("Enter the value for p2: "))
    if user_selection == 1:
      available_plans_df = single_sampling_plan(AlphaLow, AlphaHigh, BetaLow, 
                                         BetaHigh, p1, p2)
    elif user_selection == 2:
      available_plans_df = chsp_1(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2)
    elif user_selection == 3:
      available_plans_df = chsp_4(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2)
    elif user_selection == 4:
      available_plans_df = mds_1(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2)
    print('''\n\nFor the user selections:\n 
          Alpha low: {}
          Alpha high: {} 
          Beta low: {}
          Beta high: {}
          p1: {}
          p2: {}\n'''.format(AlphaLow, AlphaHigh, BetaLow, BetaHigh, p1, p2))
    if len(available_plans_df) == 0:
      print("No plans available")
    elif len(available_plans_df) == 1:
      print("The optimum plan is:")
      print(available_plans_df)
    else:
      print("Total available plans: ", available_plans_df.shape[0])
      available_plans_df = available_plans_df.sort_values('Alpha+Beta')
      print("Available plans:")
      print(available_plans_df)
      optimum_plan_df = available_plans_df.head(1)
      print("\nThe optimum plan is:")
      print(optimum_plan_df)
    yes_no = str(input("\n\nDo you want to continue? (y/n): ")).lower()
    if yes_no == 'y':
      sampling_plans()
      
      
#========================================================================
# Calling the final function
#========================================================================
sampling_plans()
