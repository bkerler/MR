/*
    PBKDF2 SHA256 OpenCL Optimized kernel, limited to max. 32 chars for salt and password
    (c) B. Kerler 2017
    MIT License
*/

typedef struct {
	unsigned int length;
	unsigned int buffer[32/4];
} inbuf;

typedef struct {
	unsigned int buffer[32/4];
} outbuf;

#define F1(x,y,z)   (bitselect(z,y,x))
#define F0(x,y,z)   (bitselect (x, y, (x ^ z)))
#define mod(x,y) x-(x/y*y)
#define shr32(x,n) ((x) >> (n))
#define rotl32(a,n) rotate ((a), (n))

unsigned int SWAP (unsigned int val)
{
    return (rotate(((val) & 0x00FF00FF), 24U) | rotate(((val) & 0xFF00FF00), 8U));
}

#define S0(x) (rotl32 ((x), 25u) ^ rotl32 ((x), 14u) ^ shr32 ((x),  3u))
#define S1(x) (rotl32 ((x), 15u) ^ rotl32 ((x), 13u) ^ shr32 ((x), 10u))
#define S2(x) (rotl32 ((x), 30u) ^ rotl32 ((x), 19u) ^ rotl32 ((x), 10u))
#define S3(x) (rotl32 ((x), 26u) ^ rotl32 ((x), 21u) ^ rotl32 ((x),  7u))

#define SHA256C00 0x428a2f98u
#define SHA256C01 0x71374491u
#define SHA256C02 0xb5c0fbcfu
#define SHA256C03 0xe9b5dba5u
#define SHA256C04 0x3956c25bu
#define SHA256C05 0x59f111f1u
#define SHA256C06 0x923f82a4u
#define SHA256C07 0xab1c5ed5u
#define SHA256C08 0xd807aa98u
#define SHA256C09 0x12835b01u
#define SHA256C0a 0x243185beu
#define SHA256C0b 0x550c7dc3u
#define SHA256C0c 0x72be5d74u
#define SHA256C0d 0x80deb1feu
#define SHA256C0e 0x9bdc06a7u
#define SHA256C0f 0xc19bf174u
#define SHA256C10 0xe49b69c1u
#define SHA256C11 0xefbe4786u
#define SHA256C12 0x0fc19dc6u
#define SHA256C13 0x240ca1ccu
#define SHA256C14 0x2de92c6fu
#define SHA256C15 0x4a7484aau
#define SHA256C16 0x5cb0a9dcu
#define SHA256C17 0x76f988dau
#define SHA256C18 0x983e5152u
#define SHA256C19 0xa831c66du
#define SHA256C1a 0xb00327c8u
#define SHA256C1b 0xbf597fc7u
#define SHA256C1c 0xc6e00bf3u
#define SHA256C1d 0xd5a79147u
#define SHA256C1e 0x06ca6351u
#define SHA256C1f 0x14292967u
#define SHA256C20 0x27b70a85u
#define SHA256C21 0x2e1b2138u
#define SHA256C22 0x4d2c6dfcu
#define SHA256C23 0x53380d13u
#define SHA256C24 0x650a7354u
#define SHA256C25 0x766a0abbu
#define SHA256C26 0x81c2c92eu
#define SHA256C27 0x92722c85u
#define SHA256C28 0xa2bfe8a1u
#define SHA256C29 0xa81a664bu
#define SHA256C2a 0xc24b8b70u
#define SHA256C2b 0xc76c51a3u
#define SHA256C2c 0xd192e819u
#define SHA256C2d 0xd6990624u
#define SHA256C2e 0xf40e3585u
#define SHA256C2f 0x106aa070u
#define SHA256C30 0x19a4c116u
#define SHA256C31 0x1e376c08u
#define SHA256C32 0x2748774cu
#define SHA256C33 0x34b0bcb5u
#define SHA256C34 0x391c0cb3u
#define SHA256C35 0x4ed8aa4au
#define SHA256C36 0x5b9cca4fu
#define SHA256C37 0x682e6ff3u
#define SHA256C38 0x748f82eeu
#define SHA256C39 0x78a5636fu
#define SHA256C3a 0x84c87814u
#define SHA256C3b 0x8cc70208u
#define SHA256C3c 0x90befffau
#define SHA256C3d 0xa4506cebu
#define SHA256C3e 0xbef9a3f7u
#define SHA256C3f 0xc67178f2u 

__constant uint k_sha256[64] =
{
  SHA256C00, SHA256C01, SHA256C02, SHA256C03,
  SHA256C04, SHA256C05, SHA256C06, SHA256C07,
  SHA256C08, SHA256C09, SHA256C0a, SHA256C0b,
  SHA256C0c, SHA256C0d, SHA256C0e, SHA256C0f,
  SHA256C10, SHA256C11, SHA256C12, SHA256C13,
  SHA256C14, SHA256C15, SHA256C16, SHA256C17,
  SHA256C18, SHA256C19, SHA256C1a, SHA256C1b,
  SHA256C1c, SHA256C1d, SHA256C1e, SHA256C1f,
  SHA256C20, SHA256C21, SHA256C22, SHA256C23,
  SHA256C24, SHA256C25, SHA256C26, SHA256C27,
  SHA256C28, SHA256C29, SHA256C2a, SHA256C2b,
  SHA256C2c, SHA256C2d, SHA256C2e, SHA256C2f,
  SHA256C30, SHA256C31, SHA256C32, SHA256C33,
  SHA256C34, SHA256C35, SHA256C36, SHA256C37,
  SHA256C38, SHA256C39, SHA256C3a, SHA256C3b,
  SHA256C3c, SHA256C3d, SHA256C3e, SHA256C3f,
};

#define SHA256_STEP(F0a,F1a,a,b,c,d,e,f,g,h,x,K)  \
{                                               \
  h += K;                                       \
  h += x;                                       \
  h += S3 (e);                           \
  h += F1a (e,f,g);                              \
  d += h;                                       \
  h += S2 (a);                           \
  h += F0a (a,b,c);                              \
}

#define SHA256_EXPAND(x,y,z,w) (S1 (x) + y + S0 (z) + w) 

static void sha256_process2 (const unsigned int *W, unsigned int *digest)
{
  unsigned int a = digest[0];
  unsigned int b = digest[1];
  unsigned int c = digest[2];
  unsigned int d = digest[3];
  unsigned int e = digest[4];
  unsigned int f = digest[5];
  unsigned int g = digest[6];
  unsigned int h = digest[7];

  unsigned int w0_t = W[0];
  unsigned int w1_t = W[1];
  unsigned int w2_t = W[2];
  unsigned int w3_t = W[3];
  unsigned int w4_t = W[4];
  unsigned int w5_t = W[5];
  unsigned int w6_t = W[6];
  unsigned int w7_t = W[7];
  unsigned int w8_t = W[8];
  unsigned int w9_t = W[9];
  unsigned int wa_t = W[10];
  unsigned int wb_t = W[11];
  unsigned int wc_t = W[12];
  unsigned int wd_t = W[13];
  unsigned int we_t = W[14];
  unsigned int wf_t = W[15];

  #define ROUND_EXPAND(i)                           \
  {                                                 \
    w0_t = SHA256_EXPAND (we_t, w9_t, w1_t, w0_t);  \
    w1_t = SHA256_EXPAND (wf_t, wa_t, w2_t, w1_t);  \
    w2_t = SHA256_EXPAND (w0_t, wb_t, w3_t, w2_t);  \
    w3_t = SHA256_EXPAND (w1_t, wc_t, w4_t, w3_t);  \
    w4_t = SHA256_EXPAND (w2_t, wd_t, w5_t, w4_t);  \
    w5_t = SHA256_EXPAND (w3_t, we_t, w6_t, w5_t);  \
    w6_t = SHA256_EXPAND (w4_t, wf_t, w7_t, w6_t);  \
    w7_t = SHA256_EXPAND (w5_t, w0_t, w8_t, w7_t);  \
    w8_t = SHA256_EXPAND (w6_t, w1_t, w9_t, w8_t);  \
    w9_t = SHA256_EXPAND (w7_t, w2_t, wa_t, w9_t);  \
    wa_t = SHA256_EXPAND (w8_t, w3_t, wb_t, wa_t);  \
    wb_t = SHA256_EXPAND (w9_t, w4_t, wc_t, wb_t);  \
    wc_t = SHA256_EXPAND (wa_t, w5_t, wd_t, wc_t);  \
    wd_t = SHA256_EXPAND (wb_t, w6_t, we_t, wd_t);  \
    we_t = SHA256_EXPAND (wc_t, w7_t, wf_t, we_t);  \
    wf_t = SHA256_EXPAND (wd_t, w8_t, w0_t, wf_t);  \
  }

  #define ROUND_STEP(i)                                                                   \
  {                                                                                       \
    SHA256_STEP (F0, F1, a, b, c, d, e, f, g, h, w0_t, k_sha256[i +  0]); \
    SHA256_STEP (F0, F1, h, a, b, c, d, e, f, g, w1_t, k_sha256[i +  1]); \
    SHA256_STEP (F0, F1, g, h, a, b, c, d, e, f, w2_t, k_sha256[i +  2]); \
    SHA256_STEP (F0, F1, f, g, h, a, b, c, d, e, w3_t, k_sha256[i +  3]); \
    SHA256_STEP (F0, F1, e, f, g, h, a, b, c, d, w4_t, k_sha256[i +  4]); \
    SHA256_STEP (F0, F1, d, e, f, g, h, a, b, c, w5_t, k_sha256[i +  5]); \
    SHA256_STEP (F0, F1, c, d, e, f, g, h, a, b, w6_t, k_sha256[i +  6]); \
    SHA256_STEP (F0, F1, b, c, d, e, f, g, h, a, w7_t, k_sha256[i +  7]); \
    SHA256_STEP (F0, F1, a, b, c, d, e, f, g, h, w8_t, k_sha256[i +  8]); \
    SHA256_STEP (F0, F1, h, a, b, c, d, e, f, g, w9_t, k_sha256[i +  9]); \
    SHA256_STEP (F0, F1, g, h, a, b, c, d, e, f, wa_t, k_sha256[i + 10]); \
    SHA256_STEP (F0, F1, f, g, h, a, b, c, d, e, wb_t, k_sha256[i + 11]); \
    SHA256_STEP (F0, F1, e, f, g, h, a, b, c, d, wc_t, k_sha256[i + 12]); \
    SHA256_STEP (F0, F1, d, e, f, g, h, a, b, c, wd_t, k_sha256[i + 13]); \
    SHA256_STEP (F0, F1, c, d, e, f, g, h, a, b, we_t, k_sha256[i + 14]); \
    SHA256_STEP (F0, F1, b, c, d, e, f, g, h, a, wf_t, k_sha256[i + 15]); \
  }

  ROUND_STEP (0);

  ROUND_EXPAND();
  ROUND_STEP(16);

  ROUND_EXPAND();
  ROUND_STEP(32);

  ROUND_EXPAND();
  ROUND_STEP(48);

  digest[0] += a;
  digest[1] += b;
  digest[2] += c;
  digest[3] += d;
  digest[4] += e;
  digest[5] += f;
  digest[6] += g;
  digest[7] += h;
}

static void pbkdf256(__global const unsigned int *pass, int pass_len, unsigned int *salt, int salt_len, int iter, unsigned int* hash, unsigned int hash_len)
{
	
	int plen=pass_len/4;
	if (mod(pass_len,4)) plen++;
    
    int slen=salt_len/4;
    if (mod(salt_len,4)) slen++;
    
	unsigned int* p = hash;
	
	unsigned int ipad[16];
	ipad[0x0]=0x36363636;
	ipad[0x1]=0x36363636;
	ipad[0x2]=0x36363636;
	ipad[0x3]=0x36363636;
	ipad[0x4]=0x36363636;
	ipad[0x5]=0x36363636;
	ipad[0x6]=0x36363636;
	ipad[0x7]=0x36363636;
	ipad[0x8]=0x36363636;
	ipad[0x9]=0x36363636;
	ipad[0xA]=0x36363636;
	ipad[0xB]=0x36363636;
	ipad[0xC]=0x36363636;
	ipad[0xD]=0x36363636;
	ipad[0xE]=0x36363636;
	ipad[0xF]=0x36363636;

	unsigned int opad[16];
	opad[0x0]=0x5C5C5C5C;
	opad[0x1]=0x5C5C5C5C;
	opad[0x2]=0x5C5C5C5C;
	opad[0x3]=0x5C5C5C5C;
	opad[0x4]=0x5C5C5C5C;
	opad[0x5]=0x5C5C5C5C;
	opad[0x6]=0x5C5C5C5C;
	opad[0x7]=0x5C5C5C5C;
	opad[0x8]=0x5C5C5C5C;
	opad[0x9]=0x5C5C5C5C;
	opad[0xA]=0x5C5C5C5C;
	opad[0xB]=0x5C5C5C5C;
	opad[0xC]=0x5C5C5C5C;
	opad[0xD]=0x5C5C5C5C;
	opad[0xE]=0x5C5C5C5C;
	opad[0xF]=0x5C5C5C5C;

	for (int m=0;m<plen && m<16;m++)
	{
		ipad[m]^=SWAP(pass[m]);
		opad[m]^=SWAP(pass[m]);
	}

	// precompute ipad
			unsigned int stateipad[8];
			stateipad[0] = 0x6a09e667;
			stateipad[1] = 0xbb67ae85;
			stateipad[2] = 0x3c6ef372;
			stateipad[3] = 0xa54ff53a;
			stateipad[4] = 0x510e527f;
			stateipad[5] = 0x9b05688c;
			stateipad[6] = 0x1f83d9ab;
			stateipad[7] = 0x5be0cd19;

			//->sha256_update(state,W,ilenor,wposr,ipad,0x40);
			unsigned int W[0x10];
			W[0]=ipad[0];
			W[1]=ipad[1];
			W[2]=ipad[2];
			W[3]=ipad[3];
			W[4]=ipad[4];
			W[5]=ipad[5];
			W[6]=ipad[6];
			W[7]=ipad[7];
			W[8]=ipad[8];
			W[9]=ipad[9];
			W[10]=ipad[10];
			W[11]=ipad[11];
			W[12]=ipad[12];
			W[13]=ipad[13];
			W[14]=ipad[14];
			W[15]=ipad[15];
			sha256_process2(W,stateipad);

		// precompute ipad
			unsigned int stateopad[8]={0};
			stateopad[0] = 0x6a09e667;
			stateopad[1] = 0xbb67ae85;
			stateopad[2] = 0x3c6ef372;
			stateopad[3] = 0xa54ff53a;
			stateopad[4] = 0x510e527f;
			stateopad[5] = 0x9b05688c;
			stateopad[6] = 0x1f83d9ab;
			stateopad[7] = 0x5be0cd19;

			//->sha256_update(state,W,ilenor,wposr,ipad,0x40);
			W[0]=opad[0];
			W[1]=opad[1];
			W[2]=opad[2];
			W[3]=opad[3];
			W[4]=opad[4];
			W[5]=opad[5];
			W[6]=opad[6];
			W[7]=opad[7];
			W[8]=opad[8];
			W[9]=opad[9];
			W[10]=opad[10];
			W[11]=opad[11];
			W[12]=opad[12];
			W[13]=opad[13];
			W[14]=opad[14];
			W[15]=opad[15];
			sha256_process2(W,stateopad);

			
	unsigned int counter = 1;
    unsigned int state[8]={0};
    
    unsigned int tkeylen=hash_len;
	unsigned int cplen=0;
	while(tkeylen>0) 
	{
		if(tkeylen > 32) cplen = 32;
		else cplen=tkeylen;

		//hmac_sha256_init(state,W,ileno,wpos,ipad,opad,pwd);
		//->sha256_init(state,W,ileno,wpos);
		//->sha256_update(state,W,ileno,wpos,ipad,0x40);
		state[0] = stateipad[0];
		state[1] = stateipad[1];
		state[2] = stateipad[2];
		state[3] = stateipad[3];
		state[4] = stateipad[4];
		state[5] = stateipad[5];
		state[6] = stateipad[6];
		state[7] = stateipad[7];
		//hmac_sha256_update(state,W,ileno,wpos,ipad,opad,salt,salt_len);
		//->sha256_update(state,W,ileno,wpos,salt,salt_len);
		//hmac_sha256_update(state,W,ileno,wpos,ipad,opad,itmp,4);
		//->sha256_update(state,W,ileno,wpos,itmp,4);
		W[0]=0;
		W[1]=0;
		W[2]=0;
		W[3]=0;
		W[4]=0;
		W[5]=0;
		W[6]=0;
		W[7]=0;
		W[8]=0;
		W[9]=0;
		W[10]=0;
		W[11]=0;
		W[12]=0;
		W[13]=0;
		W[14]=0;
		for (int m=0;m<slen;m++)
        {
            W[m]=SWAP(salt[m]);
        }
        W[slen]=counter;
        
        unsigned int padding=0x80<<(((salt_len+4)-((salt_len+4)/4*4))*8);
        W[((mod((salt_len+4),(16*4)))/4)]|=SWAP(padding);
            // Let's add length
        W[0x0F]=(0x40+(salt_len+4))*8;

        //W[slen+1]=0x80000000;
        //W[15]=0x60*8;
		//hmac_sha256_final(state,W,ileno,ipad,opad,digtmp);
		//->sha256_finish(state,W,ileno,&opad[0x10]);
		
		sha256_process2(W,state);
		
		//sha256(opad,0x60,digtmp);
		//->sha256_init(state,W,ileno,wpos);
		//->sha256_update(state,W,ileno,wpos,opad,0x60);
		//->sha256_finish(state,W,ileno,digtmp);

		W[0]=state[0];
		W[1]=state[1];
		W[2]=state[2];
		W[3]=state[3];
		W[4]=state[4];
		W[5]=state[5];
		W[6]=state[6];
		W[7]=state[7];
		W[8]=0x80000000;
		W[9]=0;
		W[10]=0;
		W[11]=0;
		W[12]=0;
		W[13]=0;
		W[14]=0;
		W[15]=0x60*8;

		state[0]=stateopad[0];
		state[1]=stateopad[1];
		state[2]=stateopad[2];
		state[3]=stateopad[3];
		state[4]=stateopad[4];
		state[5]=stateopad[5];
		state[6]=stateopad[6];
		state[7]=stateopad[7];
		
		//sha256_finish(state,W,ileno,digtmp);
		sha256_process2(W,state);
		

		p[0]=W[0]=state[0];
		p[1]=W[1]=state[1];
		p[2]=W[2]=state[2];
		p[3]=W[3]=state[3];
		p[4]=W[4]=state[4];
		p[5]=W[5]=state[5];
		p[6]=W[6]=state[6];
		p[7]=W[7]=state[7];

		for(unsigned int j = 1; j < iter; j++) 
		{
			//hmac_sha256(pwd,digtmp,32,digtmp);
			//->sha256_init(state,W,ilenor,wposr);
			//->sha256_update(state,W,ilenor,wposr,digtmp,32);
			//->sha256_finish(state,W,ileno,&opad[0x10]);

			W[8]=0x80000000; //Padding
			W[9]=0;
			W[10]=0;
			W[11]=0;
			W[12]=0;
			W[13]=0;
			W[14]=0;
			W[15]=0x60*8;
			state[0] = stateipad[0];
			state[1] = stateipad[1];
			state[2] = stateipad[2];
			state[3] = stateipad[3];
			state[4] = stateipad[4];
			state[5] = stateipad[5];
			state[6] = stateipad[6];
			state[7] = stateipad[7];
			sha256_process2(W,state);

            unsigned int M[0x10]={0};
			M[0]=state[0];
			M[1]=state[1];
			M[2]=state[2];
			M[3]=state[3];
			M[4]=state[4];
			M[5]=state[5];
			M[6]=state[6];
			M[7]=state[7];
			M[8]=0x80000000; //Padding
			M[9]=0;
			M[10]=0;
			M[11]=0;
			M[12]=0;
			M[13]=0;
			M[14]=0;
			M[15]=0x60*8;

            //->sha256_init(state,W,ilenor,wposr);
			//->sha256_update(state,W,ilenor,wposr,opad,0x60);
			state[0] = stateopad[0];
			state[1] = stateopad[1];
			state[2] = stateopad[2];
			state[3] = stateopad[3];
			state[4] = stateopad[4];
			state[5] = stateopad[5];
			state[6] = stateopad[6];
			state[7] = stateopad[7];
            
			//->sha256_finish(state,W,ilenor,digtmp);
			sha256_process2(M,state);

			W[0]=state[0];
			W[1]=state[1];
			W[2]=state[2];
			W[3]=state[3];
			W[4]=state[4];
			W[5]=state[5];
			W[6]=state[6];
			W[7]=state[7];

			p[0] ^= state[0];
			p[1] ^= state[1];
			p[2] ^= state[2];
			p[3] ^= state[3];
			p[4] ^= state[4];
			p[5] ^= state[5];
			p[6] ^= state[6];
			p[7] ^= state[7];
		}
        
        p[0]=SWAP(p[0]);
        p[1]=SWAP(p[1]);
        p[2]=SWAP(p[2]);
        p[3]=SWAP(p[3]);
        p[4]=SWAP(p[4]);
        p[5]=SWAP(p[5]);
        p[6]=SWAP(p[6]);
        p[7]=SWAP(p[7]);
        
		tkeylen-= cplen;
		counter++;
		p+= cplen/4;
	}
	return;
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
    pbkdf256(inbuffer[idx].buffer, inbuffer[idx].length, ssalt, salt_len, iterations, hash,32);
    outbuffer[idx].buffer[0]=hash[0];
    outbuffer[idx].buffer[1]=hash[1];
    outbuffer[idx].buffer[2]=hash[2];
    outbuffer[idx].buffer[3]=hash[3];
    outbuffer[idx].buffer[4]=hash[4];
    outbuffer[idx].buffer[5]=hash[5];
    outbuffer[idx].buffer[6]=hash[6];
    outbuffer[idx].buffer[7]=hash[7];
}