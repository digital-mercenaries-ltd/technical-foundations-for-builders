# Authentication and credential management

Status: practical reference - reviewed 2026-08-02

Choose an account pattern first, then design multi-factor authentication (MFA) and recovery as separate controls. The four patterns below are a practical TFB decision model, not a classification defined by the cited standards. In particular, the boundary between platform and independent password managers is a risk and recovery judgement: either category can be well or poorly implemented.

This reference concerns human accounts and the credentials used by applications and automation. It does not replace a service's recovery rules, an organisation's identity policy or a risk assessment for a consequential system. The canonical explanatory home is the [Chapter 9 plan](../OUTLINE.md#9-security-privacy-and-identity).

## Terms

| Term | Meaning |
| --- | --- |
| **Passkey** | A phishing-resistant public-key credential. A passkey may be synchronised through a credential provider or bound to a device or hardware security key. |
| **Federated login** | Authentication through Apple, Google, Microsoft or an enterprise identity provider. The relying service trusts an assertion from that provider instead of verifying the user's primary authenticator itself. |
| **Platform password manager** | A manager integrated with an operating system or browser, such as Apple Passwords or Google Password Manager. |
| **Independent password manager** | A separate dedicated vault, such as Password Safe, KeePass, Strongbox, Bitwarden or 1Password. |
| **Recovery material** | Recovery codes, backup security keys and emergency-access information. |

Product examples were reviewed on 2026-08-02; verify their current capabilities before relying on them.

## Decision sequence

1. Use a passkey when the service offers a suitable implementation.
2. Otherwise, use an approved federated login when the dependency and recovery model are acceptable.
3. Otherwise, generate a unique password with a cryptographically secure generator.
4. Store a low-consequence account password in a platform password manager.
5. Store a consequential account password in an independent password manager with protected, tested backups.
6. Apply MFA according to impact, privilege and phishing risk.
7. Establish recovery paths while the account and its authenticators are available.

## Four account patterns

### 1. Passkey

Prefer a passkey when the service supports a suitable implementation. Keep it on a trusted device, in a trusted synchronised passkey provider or on a hardware security key. Store any fallback credential and recovery material in a separate failure domain. Use step-up authentication for unusually sensitive actions where the service supports it.

Passkeys use Web Authentication (WebAuthn) or related Fast Identity Online (FIDO) protocols to bind authentication to the legitimate service, which provides phishing resistance. Synchronised and device-bound passkeys have different recovery and assurance properties. A synchronised passkey must not be assumed to satisfy the non-exportable-key requirement of NIST Authentication Assurance Level 3 (AAL3).

### 2. Federated login

Use a suitable identity provider when reducing password proliferation is worth depending on that provider. The identity-provider account becomes part of the root of trust: compromise, suspension or failed recovery there can affect every relying account. Protect it with strong MFA and maintain an independent recovery path.

Federation moves authentication rather than removing it. The relying service must still validate the provider's signed, audience-restricted assertion and manage its own session and authorisation correctly.

### 3. Generated password in a platform password manager

Use this pattern for low-consequence accounts such as content websites, forums, hobby sites, minor retailers and disposable trials. Generate a long, unique random password and let the manager autofill it. MFA can remain optional only while the account contains no sensitive personal data, payment details or access that materially increases the impact of compromise.

The low-consequence boundary is a TFB heuristic, not a claim that platform password managers are intrinsically weak. Deep operating-system and browser integration can improve autofill and passkey support. The trade-off is concentration in the platform account, device and synchronisation fabric.

### 4. Generated password in an independent password manager

Use this pattern when compromise or loss could cause financial harm, expose sensitive information, compromise another account, affect business systems or make recovery difficult. Typical examples include:

- primary email and identity-provider accounts;
- financial, government and healthcare accounts;
- mobile-network and domain-registrar accounts;
- source control, cloud platforms and production systems;
- business administration accounts; and
- credentials that can recover other accounts.

Generate a long, unique random password. Store it in the independent password manager and its protected, tested backups. Require MFA for these accounts and prefer phishing-resistant authentication for consequential or privileged access.

An independent vault creates another security and recovery boundary; it does not remove concentration risk. Protect the vault itself with strong MFA, a memorable master passphrase where one remains necessary and a recovery design that does not depend solely on the vault being available.

## Credentials to memorise

Memorise only credentials that may be needed when the password manager or usual device is unavailable:

1. the master passphrase for an independent password manager, where one is used;
2. the device PIN or login credential; and
3. a workforce or single-sign-on password where password fallback remains necessary.

Use a unique, randomly generated multiword passphrase for a credential that a person must remember. Use random strings for credentials that a manager will store and autofill.

A primary email or identity-provider password does not automatically need to be memorised. It can be a generated value in the independent vault if the account has a tested recovery path that does not depend solely on access to that vault. Avoid circular recovery in which the vault, primary email, identity provider and usual device can each be recovered only through another member of the same failed set.

## Multi-factor authentication

MFA is a separate control, not a fifth account pattern. Require it for:

- primary email and identity-provider accounts;
- password managers;
- financial and mobile-network accounts;
- professional systems; and
- accounts that can recover other accounts.

For professional use, require MFA by default for business email, enterprise identity, source control, cloud services, virtual private networks, production systems and administrative software as a service.

Prefer phishing-resistant cryptographic authentication for consequential and privileged access. Hardware security keys, hardware-backed passkeys and suitable device-bound passkeys are common choices. Certificate-backed authentication can be appropriate in managed enterprise environments. Time-based one-time password (TOTP) applications are a useful fallback but are not phishing-resistant. Use SMS only when stronger authentication is unavailable. Reserve email codes for confirmation or recovery where unavoidable; NIST does not treat them as out-of-band authentication, and a code sent to the account being recovered is not an independent factor.

NIST SP 800-63B-4 requires verifiers operating at AAL2 to offer a phishing-resistant option; AAL3 requires a phishing-resistant cryptographic authenticator with a non-exportable private key. These are assurance requirements for authentication systems, not universal labels for the four account patterns.

## Password rules

- Generate stored passwords with a cryptographically secure generator.
- Use a different password for every account.
- Use random strings for passwords that a manager stores and autofills.
- Use generated random-word passphrases only for credentials a person must remember.
- Do not impose arbitrary character-composition rules.
- Do not rotate human passwords routinely. Change them after compromise or disclosure, at the user's request, or when a justified policy requires it.

Service operators should allow password managers, autofill and paste; accept sufficiently long passwords; reject common or compromised values; rate-limit guessing; and store passwords using an appropriate salted password-hashing scheme. Those implementation duties are distinct from a user's credential-storage choice.

## Recovery

Design recovery with the authentication method. For consequential accounts:

- keep recovery material outside the sole failure domain of the account or authenticator it recovers;
- retain protected offline recovery codes where justified;
- register more than one security key where supported;
- maintain an independent recovery path for primary email and identity-provider accounts;
- back up and test the independent password vault; and
- document, protect and test professional break-glass procedures.

Avoid one incident removing access to the phone, email, passkeys, password vault and recovery material together. Treat recovery as another authentication route: its strength and monitoring should be proportionate to the account it restores. Revoke lost authenticators promptly, notify the account owner of recovery events and replace single-use recovery codes after use.

## Non-human identities

Applications and automation do not use the four human account patterns. Prefer workload identity, narrowly scoped roles and short-lived credentials. When a static secret is unavoidable, store it in a secrets manager, retrieve it at runtime, restrict its permissions, record its owner and purpose, audit its use, support rotation and revocation, and remove it when no longer needed. Do not place secret values in source code, logs, documentation or AI conversations.

## From hacker folklore: xkcd's password cartoon

[xkcd 936, “Password Strength”](https://xkcd.com/936/), made the case for long multiword passwords memorable. Its lasting lesson is that length and a genuinely random selection process matter more than predictable substitutions and arbitrary composition rules. Its limitation matters too: the cartoon is not a password generator, a familiar phrase or a human-chosen sequence of words is not equivalent to words selected at random, and a password manager should normally generate a higher-entropy random string for credentials that nobody needs to type or remember. The comic is referenced rather than embedded so that attribution, context and the canonical copy remain together.

## Reference basis

This model is a practical synthesis, not a replacement for the underlying standards and guidance:

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) - authenticator types, assurance levels, phishing resistance, password-verifier rules and account recovery.
- [NIST SP 800-63C-4](https://pages.nist.gov/800-63-4/sp800-63c.html) - federation, identity providers, assertions and relying-party controls.
- [NCSC: Managing your passwords](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/password-managers), [NCSC: Three random words](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/three-random-words) and [NCSC: Passkeys](https://www.ncsc.gov.uk/passkeys) - practical personal guidance for password managers, memorable passphrases and passkeys.
- [NCSC password policy guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach) - reducing password burden through password managers, single sign-on and appropriate policy.
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) and [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) - implementation guidance for passwords, passkeys, MFA, recovery and service-side password hashing.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) - application credentials, secret lifecycle, least privilege, short-lived credentials and break-glass access.
- [CISA: Implementing Phishing-Resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf) - migration of professional systems towards FIDO/WebAuthn.

## Core rule

Prefer a suitable passkey, then an approved federated login. When a password is necessary, generate it. Use the platform password manager for low-consequence accounts and an independent password manager for consequential accounts, while treating that split as a risk and recovery judgement rather than a universal product ranking. Memorise only the few credentials needed to regain access. Apply MFA and recovery controls according to impact, privilege, phishing risk and failure domains.
