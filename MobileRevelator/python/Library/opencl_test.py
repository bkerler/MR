#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from Library import opencl

def pbkdf2_sha1_test(opencl_ctx,passwordlist):
    opencl_ctx.compile('pbkdf2_sha1')
    result=opencl_ctx.run(passwordlist)
    test=False
    if (result[0]=='624720cc0e467b2105352eea65580c4dc93b157a6bc057f1720d3ff57bd8db9f'):
        if (result[1] == '45999865271fbe67280eda4ea79afa3d07adf7bd74b658ba2672b95abc033577'):
            test=True
    if (test==True):
        print ("Ok !")
    else:
        print ("Failed !")

def pbkdf2_sha256_test(opencl_ctx,passwordlist):
    opencl_ctx.compile('pbkdf2_sha256')
    result = opencl_ctx.run(passwordlist)
    test=False
    if (result[0]=='67f6eb6e2e00dea5e3866a5af9956b9a3005f8daf07a2901c45275b54facf9d5'):
        if (result[1] == 'b3f7b5906bfe21d7e981c6b8cc90aba88f30376fab26305ebe3c083af4cdf976'):
            test=True
    if (test==True):
        print ("Ok !")
    else:
        print ("Failed !")

def sha1_test(opencl_ctx,passwordlist):
    opencl_ctx.compile('sha1')
    result = opencl_ctx.run(passwordlist)
    test=False
    if (result[0]=='5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'):
        if (result[1] == 'efe8f9c825bbdac1f2a1e554ade41efff4d93d27'):
            test=True
    if (test==True):
        print ("Ok !")
    else:
        print ("Failed !")

def sha256_test(opencl_ctx,passwordlist):
    opencl_ctx.compile('sha256')
    result = opencl_ctx.run(passwordlist)
    test=False
    if (result[0]=='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'):
        if (result[1] == 'a7c3fce0af38fcb83c2f6adfa53ab220e9b1d739e2208a665ffa54267bbc8781'):
            test=True
    if (test==True):
        print ("Ok !")
    else:
        print(result[0])
        print(result[1])
        print ("Failed !")
        
def main(argv):
    if (len(argv)<2):
        print("PyOpenCL PBKDF2/SHA1/SHA256 implementation test (c) B.Kerler 2018")
        print("-----------------------------------------------------------------")
        info=opencl.opencl_information()
        info.printplatforms()
        print("\nPlease run as: python test.py [platform number]")
        exit(0)

    # Input values to be hashed
    passwordlist = [b'password', b'default_password',b'passwd']
    salt = b'1234'
    iterations = 1000
    debug = 0
    
    print("Init opencl...")
    platform = int(argv[1])
    opencl_ctx = opencl.pbkdf2_opencl(platform, salt, iterations, debug)
    
    print("Testing pbkdf2_sha1...")
    pbkdf2_sha1_test(opencl_ctx,passwordlist);
    
    print("Testing pbkdf2_sha256...")
    pbkdf2_sha256_test(opencl_ctx,passwordlist)
        
    print("Testing sha1...")
    sha1_test(opencl_ctx,passwordlist)
 
    print("Testing sha256...")
    sha256_test(opencl_ctx,passwordlist)
    
if __name__ == '__main__':
  main(sys.argv)