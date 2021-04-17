class ParserMessage():
    
    @staticmethod
    def parse(request):
        requestObj = {}
        splitRequest = [line.strip('\r') for line in request.split('\n')]
        header = splitRequest[0].split(' ')
        
        requestObj['Request-Type'] = header[0]
        requestObj['Request-URI'] = header[1]
        requestObj['HTTP-Version'] = header[2].split('/')[1]
    
        index = 0
    
        for line in splitRequest[1:]:
            index += 1
            line = line.strip('\r')
            
            if line == '' or line == ' ':
                break
    
            if line.find(':') != -1:
                key, value = line.split(':', 1)
                value = value.strip(' ')
                if (value.find(',') != -1):
                    value = value.split(', ')
                requestObj[key] = value
    
        requestObj['body'] = '\n'.join(splitRequest[index:])
    
        return requestObj
    