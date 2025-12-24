import os
import re

# --- CONFIGURATION ---
# The domain that acts as the "Password"
DOMAIN_LOCK = "aryansingh19gh.github.io" 

# Files you want to encrypt (add more if needed)
TARGET_FILES = ["index.html", "dashboard.html"] 

# --- ENCRYPTION LOGIC (Must match the JS Decryptor) ---
def xor_encrypt(content, key):
    hex_output = ""
    key_len = len(key)
    for i, char in enumerate(content):
        # XOR the character code with the key character code
        encrypted_val = ord(char) ^ ord(key[i % key_len])
        # Convert to 2-digit Hex
        hex_output += format(encrypted_val, '02x')
    return hex_output

# --- THE JS LOADER TEMPLATE ---
# This replaces your original <script> tag
LOADER_TEMPLATE = """
<script>
(async function(){
    const _DOMAIN = "%s"; 
    const _PAYLOAD = "%s"; 

    // SECURITY SYSTEM
    const _guard = () => {
        const no = () => { document.body.innerHTML="<h1>ILLEGAL ACTION</h1>"; throw "STOP"; };
        // Poison Console
        window.console.log=window.console.error=window.console.warn=no;
        // Debugger Trap
        setInterval(()=>{const t=performance.now();debugger;if(performance.now()-t>100)no();}, 500);
        // Keyboard Lock
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = (e) => {
            if(e.key=='F12' || (e.ctrlKey && e.shiftKey)) e.preventDefault();
        };
    };

    function _decrypt(str, key) {
        let res = "";
        for (let i = 0; i < str.length; i += 2) {
            const hex = parseInt(str.substr(i, 2), 16);
            // XOR Reverse
            res += String.fromCharCode(hex ^ key.charCodeAt((i/2) %% key.length));
        }
        return res;
    }

    try {
        // Domain Check
        if (window.location.hostname !== _DOMAIN) {
            throw new Error("INVALID_HOST");
        }
        
        _guard(); // Activate protections

        const _code = _decrypt(_PAYLOAD, _DOMAIN);
        const blob = new Blob([_code], { type: 'text/javascript' });
        const url = URL.createObjectURL(blob);
        await import(url);
        URL.revokeObjectURL(url);

    } catch (e) {
        document.body.innerHTML = "<h1 style='color:red;text-align:center;margin-top:20%%'>ACCESS DENIED</h1>";
    }
})();
</script>
"""

def process_files():
    print(f"🔒 Starting Encryption Build for Domain: {DOMAIN_LOCK}")
    
    for filename in TARGET_FILES:
        if not os.path.exists(filename):
            print(f"⚠️  Skipping {filename} (Not found)")
            continue
            
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find <script type="module"> ... </script>
        # We capture everything inside the tags
        pattern = re.compile(r'<script type="module">([\s\S]*?)</script>', re.MULTILINE)
        match = pattern.search(content)

        if match:
            raw_js = match.group(1)
            print(f"   - Found JS block ({len(raw_js)} bytes). Encrypting...")
            
            # 1. Encrypt
            encrypted_data = xor_encrypt(raw_js, DOMAIN_LOCK)
            
            # 2. Prepare the new Loader Script
            # We use string formatting to insert the Key and the Payload
            new_script = LOADER_TEMPLATE % (DOMAIN_LOCK, encrypted_data)
            
            # 3. Replace in the file content
            new_content = pattern.sub(new_script, content)
            
            # 4. Overwrite the file (Only happens in the Build Environment!)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"   ✅ {filename} Secured.")
        else:
            print(f"   ❌ No <script type='module'> found in {filename}")

if __name__ == "__main__":
    process_files()
