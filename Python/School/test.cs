using System;
class Test
{
    static void Main ()
  {
    double loanAmount;
    int fee = 0;
    int percentage;
    double deposit;
    
    Console.WriteLine("Enter the loan amount: \n");
    
    loanAmount = Double.Parse(Console.ReadLine());
    
    if (loanAmount < 50000)
      {

    	if (loanAmount < 10000)
    	  {
    	    percentage = 10;
    	    fee = 0;
    	  }
    	else if (loanAmount >= 10000 && loanAmount < 15000)
    	  {
    	    percentage = 6;
    	    fee = 200;
    	  }
    	else if (loanAmount >= 15000 && loanAmount < 20000)
    	  {
    	    percentage = 5;
    	    fee = 500;
    	  }
    	else if (loanAmount >= 20000 && loanAmount < 50000)
    	  {
    	    percentage = 3;
    	    fee = 1000;
    	  }
    	    deposit = (loanAmount * percentage) / 100 + fee;
    	    Console.WriteLine("Deposit Amount is $%.2lf\n", deposit);
      }
    else
    {
	    Console.WriteLine("Loans in excess of $50000 are not allowed\n");
    }
  }
}
