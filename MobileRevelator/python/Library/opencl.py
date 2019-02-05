#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Copyright by B.Kerler 2017, PBKDF1_SHA1 and SHA256 PyOpenCl implementation, max 32 chars for password + salt
    MIT License
    Implementation was confirmed to work with Intel OpenCL on Intel(R) HD Graphics 520 and Intel(R) Core(TM) i5-6200U CPU
'''
import pyopencl as cl
import numpy as np
import binascii
import os

class opencl_information:
    def __init__(self):
        i=0

    def printplatforms(self):
        i=0
        for platform in cl.get_platforms():
            print('Platform %d - Name %s, Vendor %s' %(i,platform.name,platform.vendor))
            i+=1

    def printfullinfo(self):
        print('\n' + '=' * 60 + '\nOpenCL Platforms and Devices')
        i=0
        for platform in cl.get_platforms():
            print('=' * 60)
            print('Platform %d - Name: ' %i + platform.name)
            print('Platform %d - Vendor: ' %i + platform.vendor)
            print('Platform %d - Version: ' %i + platform.version)
            print('Platform %d - Profile: ' %i + platform.profile)

            for device in platform.get_devices():
                print(' ' + '-' * 56)
                print(' Device - Name: ' \
                      + device.name)
                print(' Device - Type: ' \
                      + cl.device_type.to_string(device.type))
                print(' Device - Max Clock Speed: {0} Mhz' \
                      .format(device.max_clock_frequency))
                print(' Device - Compute Units: {0}' \
                      .format(device.max_compute_units))
                print(' Device - Local Memory: {0:.0f} KB' \
                      .format(device.local_mem_size / 1024.0))
                print(' Device - Constant Memory: {0:.0f} KB' \
                      .format(device.max_constant_buffer_size / 1024.0))
                print(' Device - Global Memory: {0:.0f} GB' \
                      .format(device.global_mem_size / 1073741824.0))
                print(' Device - Max Buffer/Image Size: {0:.0f} MB' \
                      .format(device.max_mem_alloc_size / 1048576.0))
                print(' Device - Max Work Group Size: {0:.0f}' \
                      .format(device.max_work_group_size))
                print('\n')
        i+=1

class pbkdf2_opencl:

    def __init__(self,platform,salt,iter,debug):
        if type(salt)!=bytes:
            assert("Parameter salt has to be type of bytes")
        if type(iter)!=int:
            assert("Parameter Iteration has to be type of int")
        platforms = cl.get_platforms()
        if (platform > len(platforms)):
            assert("Selected platform %d doesn't exist" % platform)

        saltlen = int(len(salt))
        if (saltlen>int(32)):
            print('Salt longer than 32 chars is not supported!')
            exit(0)
        hash=b'\x00'*32
        hash_len=32
        n_salt = np.fromstring(salt, dtype=np.uint32)
        n_saltlen = np.array([saltlen], dtype=np.uint32)
        self.n_iter = np.array(iter, dtype=np.uint32)
        self.salt=np.append(n_saltlen,n_salt)

        # Get platforms
        devices = platforms[platform].get_devices()
        self.workgroupsize=60000
        #Create context for GPU/CPU
        print("Using Platform %d:" % platform)
        self.ctx = cl.Context(devices)
        for device in devices:
            print('--------------------------------------------------------------------------')
            print(' Device - Name: '+ device.name)
            print(' Device - Type: '+ cl.device_type.to_string(device.type))
            print(' Device - Compute Units: {0}'.format(device.max_compute_units))
            print(' Device - Max Work Group Size: {0:.0f}'.format(device.max_work_group_size))
            if (device.max_work_group_size<self.workgroupsize):
                self.workgroupsize=device.max_work_group_size

        print ("\nUsing work group size of %d\n" % self.workgroupsize)

        # Create queue for each kernel execution
        self.queue = cl.CommandQueue(self.ctx)

        # Kernel function
        src=""
        if (debug):
            os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'
            src = """
            typedef struct {
                unsigned int length;
                unsigned int buffer[32/4];
            } inbuf;
            
            typedef struct {
                unsigned int buffer[32/4];
            } outbuf;
            
            static void pbkdf(__global const unsigned int *pass, int pass_len, const unsigned int *salt, int salt_len, int iter, unsigned int* hash, unsigned int hash_len)
            {
                hash[0]=pass_len;
                hash[1]=pass[0];
                hash[2]=hash_len;
                hash[3]=iter;
                hash[4]=salt_len;
                hash[5]=salt[0];
            }
            
            __kernel void func_pbkdf2(__global const inbuf * inbuffer, __global outbuf * outbuffer, __global const inbuf * salt, const int iterations)
            {
                unsigned int idx = get_global_id(0);
                unsigned int hash[32/4]={0};
                unsigned int ssalt[32/4]={0};
                ssalt[0]=salt[0].buffer[0];
                ssalt[1]=salt[0].buffer[1];
                ssalt[2]=salt[0].buffer[2];
                ssalt[3]=salt[0].buffer[3];
                ssalt[4]=salt[0].buffer[4];
                ssalt[5]=salt[0].buffer[5];
                ssalt[6]=salt[0].buffer[6];
                ssalt[7]=salt[0].buffer[7];
                int salt_len=salt[0].length;
                pbkdf(inbuffer[idx].buffer, inbuffer[idx].length, ssalt, salt_len, iterations, hash,32);
                outbuffer[idx].buffer[0]=hash[0];
                outbuffer[idx].buffer[1]=hash[1];
                outbuffer[idx].buffer[2]=hash[2];
                outbuffer[idx].buffer[3]=hash[3];
                outbuffer[idx].buffer[4]=hash[4];
                outbuffer[idx].buffer[5]=hash[5];
                outbuffer[idx].buffer[6]=hash[6];
                outbuffer[idx].buffer[7]=hash[7];
            }
            """
        else:
            os.environ['PYOPENCL_COMPILER_OUTPUT'] = '0'

    def compile(self,type):
        fname = ""
        self.type=type
        if (self.type == 'sha1'):
            fname = os.path.join("Library","sha1.cl")
        elif (self.type == 'sha256'):
            fname = os.path.join("Library","sha256.cl")
        elif (self.type == 'pbkdf2_sha1'):
            fname = os.path.join("Library","pbkdf2_sha1.cl")
        elif (self.type == 'pbkdf2_sha256'):
            fname = os.path.join("Library","pbkdf2_sha256.cl")
        else:
            print('Type: ' + self.type + ' not supported!')
            exit(0)

        with open(fname, "r") as rf:
            src = rf.read()

        # Kernel function instantiation
        self.prg = cl.Program(self.ctx, src).build()

    def run(self,passwordlist):
        if type(passwordlist)!=list:
            assert("Parameter passwordlist has to be an array")
        if len(passwordlist)==0:
            assert ("Password list is empty")
        if type(passwordlist[0])!=bytes:
            assert ("Password in passwordlist has to be type of utf-8 string or bytes")
        pos=0
        mf = cl.mem_flags
        totalpws=len(passwordlist)
        results = []
        while (totalpws>0):
            pwarray = np.empty(0, dtype=np.uint32)
            if (totalpws<self.workgroupsize):
                pwcount=totalpws
            else:
                pwcount=self.workgroupsize

            pwdim = (pwcount,)

            for pw in passwordlist[pos:pos+pwcount]:
                pwlen = int(len(pw))
                if (pwlen>int(32)): #Only chars up to length 32 supported
                    continue
                modlen=len(pw)%4
                if modlen!=0:
                    pw=pw+(b'\0'*(4-modlen))
                n_pw = np.frombuffer(pw, dtype=np.uint32)
                n_pwlen = np.array([pwlen], dtype=np.uint32)
                password = np.array([0]*9,dtype=np.uint32)
                z=0
                for i in range(0,len(n_pwlen)):
                    password[z]=n_pwlen[i]
                    z+=1
                max=9-len(n_pwlen)
                if max>len(n_pw):
                    max=len(n_pw)
                for i in range(0,max):
                    password[z+i]=n_pw[i]
                pwarray = np.append(pwarray, password)

            result = np.zeros(int(32 / 4) * pwcount, dtype=np.uint32)

            #Allocate memory for variables on the device
            pass_g =  cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=pwarray)
            salt_g = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.salt)
            result_g = cl.Buffer(self.ctx, mf.WRITE_ONLY, result.nbytes)
            
            #Call Kernel. Automatically takes care of block/grid distribution
            if (self.type=="pbkdf2_sha1" or self.type=="pbkdf2_sha256"):
                hashlen=0x20
                self.prg.func_pbkdf2(self.queue, pwdim, None , pass_g, result_g, salt_g, self.n_iter)
            elif (self.type=="sha1"):
                hashlen=0x14
                self.prg.func_sha1(self.queue,pwdim,None,pass_g,result_g)
                #SHA1 does support longer lengths, but inputbuffer and hash are limited to 32 chars
            elif (self.type=="sha256"):
                hashlen=0x20
                self.prg.func_sha256(self.queue,pwdim,None,pass_g,result_g)
                #SHA256 does support longer lengths, but inputbuffer and hash are limited to 32 chars
            cl.enqueue_copy(self.queue, result, result_g)
            totalpws-=pwcount
            pos+=pwcount
            hexvalue = binascii.hexlify(result)
            for value in range(0, len(hexvalue), 64):
                results.append(hexvalue[value:value + 64].decode()[0:hashlen*2])
        return results