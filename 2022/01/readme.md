# [2022: Week 1 The Prep School - Parental Contact Details](https://preppindata.blogspot.com/2022/01/2022-week-1-prep-school-parental.html)

## Things I learned/practiced

* string concatenation among series. Add string columns together to get a new concatenated series.

* `pandas.series.where`: replace values in a series where a condition is False. Used here to select values between two series based on a value in another series.

* `pandas.series.dt.days`: return the number of days contained within a TimeDelta. See also `dt.seconds`, `dt.microseconds`, and `dt.nanoseconds`

* `df.to_csv`: using the `columns` attribute to define the columns and their order to be written to csv
