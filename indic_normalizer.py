from sanic_cors import CORS
from sanic import Sanic, response
from sanic.response import json

import logging

app = Sanic()
CORS(app)

logging.basicConfig(filename="indic_nomralizer.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

def do_normalization(in_str):

    out_str = []
    i = 0
    length = len(in_str)
    ords = [ord(x) for x in in_str]
    
    while i < length:

        # DEVANAGARI STARTS
        if i < length - 2 and ords[i] == 0x905 and ords[i + 1] == 0x93E and ords[i + 2] == 0x945:
            out_str.append(chr(0x911))
            i += 3

        elif i < length - 2 and ords[i] == 0x905 and ords[i + 1] == 0x93E and ords[i + 2] == 0x946:
            out_str.append(chr(0x912))
            i += 3

        elif i < length - 2 and ords[i] == 0x905 and ords[i + 1] == 0x93E and ords[i + 2] == 0x947:
            out_str.append(chr(0x913))
            i += 3

        elif i < length - 2 and ords[i] == 0x905 and ords[i + 1] == 0x93E and ords[i + 2] == 0x948:
            out_str.append(chr(0x914))
            i += 3

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x93E:
            out_str.append(chr(0x906))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x945:
            out_str.append(chr(0x972))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x946:
            out_str.append(chr(0x904))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x949:
            out_str.append(chr(0x911))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x94a:
            out_str.append(chr(0x912))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x94b:
            out_str.append(chr(0x913))
            i += 2

        elif i < length - 1 and ords[i] == 0x905 and ords[i + 1] == 0x94c:
            out_str.append(chr(0x914))
            i += 2

        elif i < length - 1 and ords[i] == 0x906 and ords[i + 1] == 0x945:
            out_str.append(chr(0x911))
            i += 2

        elif i < length - 1 and ords[i] == 0x906 and ords[i + 1] == 0x946:
            out_str.append(chr(0x912))
            i += 2

        elif i < length - 1 and ords[i] == 0x906 and ords[i + 1] == 0x947:
            out_str.append(chr(0x913))
            i += 2

        elif i < length - 1 and ords[i] == 0x906 and ords[i + 1] == 0x948:
            out_str.append(chr(0x914))
            i += 2

        elif i < length - 1 and ords[i] == 0x90f and ords[i + 1] == 0x945:
            out_str.append(chr(0x90d))
            i += 2

        elif i < length - 1 and ords[i] == 0x90f and ords[i + 1] == 0x946:
            out_str.append(chr(0x90e))
            i += 2

        elif i < length - 1 and ords[i] == 0x90f and ords[i + 1] == 0x947:
            out_str.append(chr(0x910))
            i += 2

        elif i < length - 1 and ords[i] == 0x915 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x958))
            i += 2

        elif i < length - 1 and ords[i] == 0x916 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x959))
            i += 2

        elif i < length - 1 and ords[i] == 0x917 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95A))
            i += 2

        elif i < length -2 and ords[i] == 0x919 and ords[i + 1] == 0x94d and 0x915 <= ords[i + 2] <= 0x918:
            out_str.append(chr(0x902))
            i += 2

        elif i < length - 1 and ords[i] == 0x91c and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95B))
            i += 2

        elif i < length - 2 and ords[i] == 0x91e and ords[i + 1] == 0x94d and 0x91a <= ords[i + 2] <= 0x91d:
            out_str.append(chr(0x902))
            i += 2

        elif i < length - 1 and ords[i] == 0x921 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95C))
            i += 2

        elif i < length - 1 and ords[i] == 0x922 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95D))
            i += 2

        elif i < length - 2 and ords[i] == 0x923 and ords[i + 1] == 0x94d and 0x91f <= ords[i + 2] <= 0x922:
            out_str.append(chr(0x902))
            i += 2

        elif i < length - 1 and ords[i] == 0x928 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x929))
            i += 2

        elif i < length - 2 and ords[i] == 0x928 and ords[i + 1] == 0x94d and ords[i + 2] not in [0x928,0x923, 0x92f, 0x92e,0x92a,0x92b,0x92c,0x92d, 0x935, 0x939]:
            out_str.append(chr(0x902))
            i += 2

        elif i < length - 1 and ords[i] == 0x92b and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95e))
            i += 2

        elif i < length - 1 and ords[i] == 0x92f and ords[i + 1] == 0x93c:
            out_str.append(chr(0x95f))
            i += 2

        elif i < length - 1 and ords[i] == 0x930 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x931))
            i += 2

        elif i < length - 1 and ords[i] == 0x933 and ords[i + 1] == 0x93c:
            out_str.append(chr(0x934))
            i += 2

        elif i < length - 1 and ords[i] == 0x93e and ords[i + 1] == 0x945:
            out_str.append(chr(0x949))
            i += 2

        elif i < length - 1 and ords[i] == 0x93e and ords[i + 1] == 0x946:
            out_str.append(chr(0x94a))
            i += 2

        elif i < length - 1 and ords[i] == 0x93e and ords[i + 1] == 0x947:
            out_str.append(chr(0x94b))
            i += 2

        elif i < length - 1 and ords[i] == 0x93e and ords[i + 1] == 0x948:
            out_str.append(chr(0x94c))
            i += 2

        # DEVANAGARI ENDS

        # BENGALI STARTS
        elif i < length - 1 and ords[i] == 0x985 and ords[i + 1] == 0x9be:
            out_str.append(chr(0x986))
            i += 2

        elif i < length - 1 and ords[i] == 0x9A1 and ords[i + 1] == 0x9bc:
            out_str.append(chr(0x9DC))
            i += 2

        elif i < length - 1 and ords[i] == 0x9A2 and ords[i + 1] == 0x9bc:
            out_str.append(chr(0x9DD))
            i += 2

        elif i < length - 1 and ords[i] == 0x9AF and ords[i + 1] == 0x9bc:
            out_str.append(chr(0x9DF))
            i += 2

        elif i < length - 1 and ords[i] == 0x9C7 and ords[i + 1] == 0x9BE:
            out_str.append(chr(0x9CB))
            i += 2

        elif i < length - 1 and ords[i] == 0x9C7 and ords[i + 1] == 0x9D7:
            out_str.append(chr(0x9CC))
            i += 2

        elif i < length - 2 and ords[i] == 0x9A4 and ords[i + 1] == 0x9cd and ords[i + 2] == 0x200D:
            out_str.append(chr(0x9CE))
            i += 3

        # BENGALI ENDS

        # GURMUKHI STARTS
        elif i < length - 1 and ords[i] == 0xA05 and ords[i + 1] == 0xA3e:
            out_str.append(chr(0xA06))
            i += 2

        elif i < length - 1 and ords[i] == 0xA05 and ords[i + 1] == 0xA48:
            out_str.append(chr(0xA10))
            i += 2

        elif i < length - 1 and ords[i] == 0xA05 and ords[i + 1] == 0xA4c:
            out_str.append(chr(0xA14))
            i += 2

        elif i < length - 1 and ords[i] == 0xA72 and ords[i + 1] == 0xA3f:
            out_str.append(chr(0xA07))
            i += 2

        elif i < length - 1 and ords[i] == 0xA72 and ords[i + 1] == 0xA40:
            out_str.append(chr(0xA08))
            i += 2

        elif i < length - 1 and ords[i] == 0xA72 and ords[i + 1] == 0xA47:
            out_str.append(chr(0xA0F))
            i += 2

        elif i < length - 1 and ords[i] == 0xA73 and ords[i + 1] == 0xA41:
            out_str.append(chr(0xA09))
            i += 2

        elif i < length - 1 and ords[i] == 0xA73 and ords[i + 1] == 0xA42:
            out_str.append(chr(0xA0A))
            i += 2

        elif i < length - 1 and ords[i] == 0xA16 and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA59))
            i += 2

        elif i < length - 1 and ords[i] == 0xA17 and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA5A))
            i += 2

        elif i < length - 1 and ords[i] == 0xA1c and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA5B))
            i += 2

        elif i < length - 1 and ords[i] == 0xA2b and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA5e))
            i += 2

        elif i < length - 1 and ords[i] == 0xA32 and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA33))
            i += 2

        elif i < length - 1 and ords[i] == 0xA38 and ords[i + 1] == 0xA3c:
            out_str.append(chr(0xA36))
            i += 2

        # GURMUKHI ENDS

        # GUJARATI STARTS
        elif i < length - 2 and ords[i] == 0xA85 and ords[i + 1] == 0xABE and ords[i + 2] == 0xAC5:
            out_str.append(chr(0xA91))
            i += 3

        elif i < length - 2 and ords[i] == 0xA85 and ords[i + 1] == 0xABE and ords[i + 2] == 0xAC7:
            out_str.append(chr(0xA93))
            i += 3

        elif i < length - 2 and ords[i] == 0xA85 and ords[i + 1] == 0xABE and ords[i + 2] == 0xAC8:
            out_str.append(chr(0xA94))
            i += 3

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xABE:
            out_str.append(chr(0xA86))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xAC5:
            out_str.append(chr(0xA8D))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xAC7:
            out_str.append(chr(0xA8F))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xAC8:
            out_str.append(chr(0xA90))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xAC9:
            out_str.append(chr(0xA91))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xACB:
            out_str.append(chr(0xA93))
            i += 2

        elif i < length - 1 and ords[i] == 0xA85 and ords[i + 1] == 0xACC:
            out_str.append(chr(0xA94))
            i += 2

        elif i < length - 1 and ords[i] == 0xA86 and ords[i + 1] == 0xAC5:
            out_str.append(chr(0xA91))
            i += 2

        elif i < length - 1 and ords[i] == 0xA86 and ords[i + 1] == 0xAC7:
            out_str.append(chr(0xA93))
            i += 2

        elif i < length - 1 and ords[i] == 0xA86 and ords[i + 1] == 0xAC8:
            out_str.append(chr(0xA94))
            i += 2

        elif i < length - 1 and ords[i] == 0xABE and ords[i + 1] == 0xAC5:
            out_str.append(chr(0xAC9))
            i += 2

        elif i < length - 1 and ords[i] == 0xABE and ords[i + 1] == 0xAC7:
            out_str.append(chr(0xACB))
            i += 2

        elif i < length - 1 and ords[i] == 0xABE and ords[i + 1] == 0xAC8:
            out_str.append(chr(0xACC))
            i += 2

        # GUJARATI ENDS

        # ODIA STARTS

        elif i < length - 1 and ords[i] == 0xb05 and ords[i + 1] == 0xb3e:
            out_str.append(chr(0xb06))
            i += 2

        elif i < length - 1 and ords[i] == 0xb0F and ords[i + 1] == 0xb57:
            out_str.append(chr(0xb10))
            i += 2

        elif i < length - 1 and ords[i] == 0xb13 and ords[i + 1] == 0xb57:
            out_str.append(chr(0xb14))
            i += 2

        elif i < length - 1 and ords[i] == 0xb47 and ords[i + 1] == 0xb56:
            out_str.append(chr(0xb48))
            i += 2

        elif i < length - 1 and ords[i] == 0xb47 and ords[i + 1] == 0xb3e:
            out_str.append(chr(0xb4b))
            i += 2

        elif i < length - 1 and ords[i] == 0xb47 and ords[i + 1] == 0xb57:
            out_str.append(chr(0xb4c))
            i += 2

        elif i < length - 1 and ords[i] == 0xb21 and ords[i + 1] == 0xb3c:
            out_str.append(chr(0xb5c))
            i += 2

        elif i < length - 1 and ords[i] == 0xb22 and ords[i + 1] == 0xb3c:
            out_str.append(chr(0xb5d))
            i += 2

        # ODIA ENDS

        # TAMIL STARTS
        elif i < length - 1 and ords[i] == 0xb92 and ords[i + 1] == 0xbd7:
            out_str.append(chr(0xb94))
            i += 2

        elif i < length - 1 and ords[i] == 0xbc6 and ords[i + 1] == 0xbbe:
            out_str.append(chr(0xbca))
            i += 2

        elif i < length - 1 and ords[i] == 0xbc7 and ords[i + 1] == 0xbbe:
            out_str.append(chr(0xbcb))
            i += 2

        elif i < length - 1 and ords[i] == 0xbc6 and ords[i + 1] == 0xbd7:
            out_str.append(chr(0xbcc))
            i += 2

        # TAMIL ENDS

        # TELUGU STARTS
        elif i < length - 2 and ords[i] == 0xc2c and ords[i + 1] == 0xc41 and ords[i + 2] == 0xc41:
            out_str.append(chr(0xc0b))
            i += 3

        elif i < length - 1 and ords[i] == 0xc12 and ords[i + 1] == 0xc55:
            out_str.append(chr(0xc13))
            i += 2

        elif i < length - 1 and ords[i] == 0xc12 and ords[i + 1] == 0xc4c:
            out_str.append(chr(0xc14))
            i += 2

        elif i < length - 1 and ords[i] == 0xc46 and ords[i + 1] == 0xc55:
            out_str.append(chr(0xc47))
            i += 2

        elif i < length - 1 and ords[i] == 0xc46 and ords[i + 1] == 0xc56:
            out_str.append(chr(0xc48))
            i += 2

        elif i < length - 1 and ords[i] == 0xc4A and ords[i + 1] == 0xc55:
            out_str.append(chr(0xc4b))
            i += 2

        # TELUGU ENDS

        # KANNADA STARTS
        elif i < length - 2 and ords[i] == 0xcc6 and ords[i + 1] == 0xcc2 and ords[i + 2] == 0xcd5:
            out_str.append(chr(0xccb))
            i += 3

        elif i < length - 1 and ords[i] == 0xc92 and ords[i + 1] == 0xccc:
            out_str.append(chr(0xc94))
            i += 2

        elif i < length - 1 and ords[i] == 0xcbf and ords[i + 1] == 0xcd5:
            out_str.append(chr(0xcc0))
            i += 2

        elif i < length - 1 and ords[i] == 0xcc6 and ords[i + 1] == 0xcd5:
            out_str.append(chr(0xcc7))
            i += 2

        elif i < length - 1 and ords[i] == 0xcc6 and ords[i + 1] == 0xcd6:
            out_str.append(chr(0xcc8))
            i += 2

        elif i < length - 1 and ords[i] == 0xcc6 and ords[i + 1] == 0xcc2:
            out_str.append(chr(0xccA))
            i += 2

        elif i < length - 1 and ords[i] == 0xccA and ords[i + 1] == 0xcd5:
            out_str.append(chr(0xccb))
            i += 2

        # KANNADA ENDS

        # MALAYALAM STARTS
        elif i < length - 1 and ords[i] == 0xd07 and ords[i + 1] == 0xd57:
            out_str.append(chr(0xd08))
            i += 2

        elif i < length - 1 and ords[i] == 0xd09 and ords[i + 1] == 0xd57:
            out_str.append(chr(0xd0A))
            i += 2

        elif i < length - 1 and ords[i] == 0xd12 and ords[i + 1] == 0xd57:
            out_str.append(chr(0xd14))
            i += 2

        elif i < length - 1 and ords[i] == 0xd12 and ords[i + 1] == 0xd3e:
            out_str.append(chr(0xd13))
            i += 2

        elif i < length - 1 and ords[i] == 0xd0e and ords[i + 1] == 0xd46:
            out_str.append(chr(0xd10))
            i += 2

        elif i < length - 1 and ords[i] == 0xd46 and ords[i + 1] == 0xd46:
            out_str.append(chr(0xd48))
            i += 2

        elif i < length - 1 and ords[i] == 0xd46 and ords[i + 1] == 0xd3e:
            out_str.append(chr(0xd4A))
            i += 2

        elif i < length - 1 and ords[i] == 0xd47 and ords[i + 1] == 0xd3e:
            out_str.append(chr(0xd4B))
            i += 2

        elif i < length - 1 and ords[i] == 0xd46 and ords[i + 1] == 0xd57:
            out_str.append(chr(0xd4C))
            i += 2

        elif i < length - 2 and ords[i] == 0xd23 and ords[i + 1] == 0xd4d and ords[i + 2] == 0x200D:
            out_str.append(chr(0xd7A))
            i += 3

        elif i < length - 2 and ords[i] == 0xd28 and ords[i + 1] == 0xd4d and ords[i + 2] == 0x200D:
            out_str.append(chr(0xd7B))
            i += 3

        elif i < length - 2 and ords[i] == 0xd30 and ords[i + 1] == 0xd4d and ords[i + 2] == 0x200D:
            out_str.append(chr(0xd7C))
            i += 3

        elif i < length - 2 and ords[i] == 0xd32 and ords[i + 1] == 0xd4d and ords[i + 2] == 0x200D:
            out_str.append(chr(0xd7D))
            i += 3

        elif i < length - 2 and ords[i] == 0xd33 and ords[i + 1] == 0xd4d and ords[i + 2] == 0x200D:
            out_str.append(chr(0xd7E))
            i += 3

        # MALAYALAM ENDS

        else:
            out_str.append(in_str[i])
            i += 1

    return ''.join(out_str)



@app.route("/indic_normalizer",methods=['POST'])
def get_indic_normalized(request):
    
    try:
        input_text = request.json['text']
        #print(input_text, type(input_text))
        logger.info({"input_text":input_text})
        normalized_text = do_normalization(str(input_text).strip())
        logger.info({"input_text":input_text,"normalized_text":normalized_text })
        return json({"normalized_text":normalized_text})
    except Exception as e:
        logger.error(e)
        
    return json({"msg":"Could not Normalize the input text"})
        
if __name__ == "__main__":
    app.run(port=8091,host='0.0.0.0',access_log=False)