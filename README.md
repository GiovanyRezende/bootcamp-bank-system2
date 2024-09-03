# Bank System in Python with functions
*This is a challenge of Data Engineering NTT DATA Bootcamp in [DIO](https://web.dio.me/).* It consists in a bank system based in five operations: withdraw money, deposit money, see account statement, register user and register account; using Python functions. The project also considers the currency as the brazilian one (Real).

# The Libraries
It was used Pandas to generate statement table and datetime module to create a date.

# Rules

## Withdraw rules
- There is a limit of 3 withdraws per day;
- A person can not withdraw if there is no money in account;
- A person can not withdraw if desired value is higher than account balance;
- A person can not withdraw if desired value is higher than R$ 500.00

## Deposit rule
- Deposit value can not be negative

## Statement rule
- No statement table should be showed if there weren't any previous withdraw or deposit operations;
- The table must describe the operation executed and its value;
- The values in table must be like R$ XX.XX (R$ 34.56, R$ 123.56)

## Registers rules
- An user must be registered if wasn't registered before;
- An account can not be registered if the user wasn't previously registered
