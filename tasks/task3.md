# ASSYMETRIC ENCRYPTION

1. Install `gpg`:

(MacOS)
```bash
brew install gpg
```

(Debian Linux)
```bash
sudo apt install gpg
```

2. Generate public-private key pair:

```bash
gpg --generate-key
```

(answer the prompts for name and e-mail)

3. Export the key

```bash
gpg --armor --export put.your@email.here > public.key
```

and share it with your friend (e.g. over e-mail)

4. Import your friend's key

```bash
gpg --import friend.key
```

and make it a trusted source:

```bash
gpg --edit-key your.friend@email.here
gpg> trust
gpg> 5
gpg> quit
```

and finally restart gpg-agent to apply the changes:

```bash
gpgconf --kill gpg-agent
```

5. Encrypt a message:

```bash
gpg --output out-message.gpg --recipient your.friend@email.here --armor --encrypt path/to/message
```

(provided your file is named `message` located under `path/to` subdirectory to a place you run your terminal).

6. Share the messages with your friends over e-mail.

7. Decrypt your friend's message:

```bash
gpg --output path/to/decrypted-message --decrypt path/to/encrypted-message
```

and read it:
```bash
cat path/to/decrypted-message
```

comparare it with the encrypted message

```bash
cat path/to/encrypted-message
```

and check that your friend's key would have encrypted it completely differently:

```bash
gpg --output path/to/out-message.gpg --recipient your.friend@email.here --armor --encrypt path/to/decrypted-message
```

and then have a look on differently-encrypted message 

```bash
cat path/to/out-message.gpg
```

or, if possible, take a look in a more human-friendly way:

```bash
diff -y path/to/out-message.gpg path/to/encrypted-message
```




