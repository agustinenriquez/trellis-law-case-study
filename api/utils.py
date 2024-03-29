def number_to_english(number: int) -> str:
    """
        
    """
    if number == 0:
        return 'zero'

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    parts = []

    # millions
    if number >= 1000000:
        parts.append(number_to_english(number // 1000000) + ' million')
        # Remove first number
        number %= 1000000

    # thousands
    if number >= 1000:
        parts.append(number_to_english(number // 1000) + ' thousand')
        number %= 1000

    # hundreds
    if number >= 100:
        parts.append(number_to_english(number // 100) + ' hundred')
        number %= 100

    if number >= 20:
        parts.append(tens[number // 10])
        number %= 10
    elif number >= 10:
        parts.append(teens[number - 10])
        number = 0

    if number > 0:
        parts.append(ones[number])

    return ' '.join(parts)
