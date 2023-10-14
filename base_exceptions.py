ArrayLengthException = Exception("Sensor data must be an array of exactly four numbers")
InvalidDataPointException = Exception("Sensor data points must be between 0 and 1")
NegativeMileageException = Exception(
    "The current mileage cannot be less than the last service mileage."
)

NegativeTimeException = Exception(
    "The current date cannot be before the last service date."
)
