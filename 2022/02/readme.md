## Things I learned/practiced

* [pd.DateOffset](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects) - I used `pd.DateOffset` to replace the year of a `datetime` with a given year. When year, month, day, hour, minute, second, or microsecond is passed as an argument (note the singular nouns), adding a `DateOffset` to a `datetime` replaces that part of the original `datetime` with the new value. Despite using the `+` operator, it is **not** an arithmetic operation.

    ```python
    # change the year in the datetime series to 2022
    this_years_birthday=RAW["Date of Birth"] + pd.DateOffset(year=2022)
    ```

    Perhaps confusingly, `pd.DateOffets` can also be used to represent calendar durations. Passing the arguments years, months, weeks, days, hours, minutes, seconds, or microseconds (note the plural nouns), creates a duration that can be arithmetically added or subtracted to a `datetime`.

    `DateOffets` have a `.rollback()` and `.rollforward()` method to move a date to the next valid date relative to the offset. This is useful particularly for business weeks and business hours. I used it here in one method of calculating the day the cake is needed by "rolling back" any weekend days to Friday.

    ```python
    cake_needed_on2=(lambda df_: df_['this_years_birthday']
                        .apply(lambda x: pd.offsets.BusinessDay()
                            .rollback(x)
                            .day_name()
                            )
    ```

    `DateOffsets` behave similarly to `dateutils.relativedelta` so reading [that documentation](https://dateutil.readthedocs.io/en/stable/relativedelta.html) is helpful. There is a lot more `DateOffsets` can do so refer to the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects) as well.



* Accessing month name and week day name using `dt.month_name()` and `dt.day_name()`