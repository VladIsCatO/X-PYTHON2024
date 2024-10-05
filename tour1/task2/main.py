"""               ___________________
                -| Python Converter |-
                 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"""
# from ast import literal_eval # didn't work
import sys
def retry():
    """Code to ask if user wants to retry converting"""
    again = input('retry (Y/n): ').strip().upper()
    if again == 'Y':
        return main()
    sys.exit()

def main():
    """Main function"""
    #Describing App
    print("""
                ___________________
                -| Python Converter |-
                ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    !For now we only support foot, yards and miles!
    1. Enter number, supported unit FROM what you wanna convert and supported unit TO what you wanna convert,
    example:
    15 ft yd
    --> Result: 5 yards
    2. Get your result.

        HELPER:
    foot = ft;
    yard = yd;
    miles = mi.""")
    unit_signs = {'ft_yd':'/3',
                'ft_mi':'/5280',
                'mi_ft':'*5280',
                'mi_yd':'*1760',
                'yd_ft':'*3',
                'yd_mi':'*1760'}
    user = input('>').strip().split()
    if len(user) == 3:
        try:
            print(0)
            number = int(user[0])
            from_unit = user[1]
            to_unit = user[2]
            print(1)
        except ValueError:
            print('Error: Not right value. Watch example again and retry.')
            retry()
        print(from_unit)
        sign = unit_signs[f'{from_unit}_{to_unit}']
        return eval(str(number)+sign)
    print('Error: Less numbers than expected. Watch example again and retry.')
    return retry()

print(main())
