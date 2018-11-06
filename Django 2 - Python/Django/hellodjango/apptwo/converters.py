class TwoDigitDayConverter:
    regex = '[0-9]{2}'

    def to_python(selfself, value):
        return int(value)

    def to_url(self, value):
        return '%02d' % value


