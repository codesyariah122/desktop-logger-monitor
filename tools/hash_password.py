import bcrypt

stored_hash = "$2y$10$iK7rMfZD9DfjmBALD/lH9u0q8ulsMAik129eEh7nmHXOsh738K8cC"

password = "@#$webdev28S"

if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
    print("Password cocok!")
else:
    print("Password tidak cocok.")
