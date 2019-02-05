#Filename="finanzassistent"
#Type=Prerun

import os

def main():
    ctx.gui_setMainLabel("Postbank Finanzassistent: Extracting key");
    error=""
    dbkey="73839EC3A528910B235859947CC8424543D7B686"
    ctx.gui_setMainLabel("Postbank: Key extracted: " + dbkey)
    if not (ctx.fs_sqlcipher_decrypt(filename, filename + ".dec", dbkey)):
        error="Error: Wrong key for decryption."
    if (error==""):
        return "Postbank Finanzassistent: Decryption of database successful."
    return ""