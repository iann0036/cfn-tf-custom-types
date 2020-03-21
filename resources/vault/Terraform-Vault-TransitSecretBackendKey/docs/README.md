# Terraform::Vault::TransitSecretBackendKey

Creates an Encryption Keyring on a Transit Secret Backend for Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::TransitSecretBackendKey",
    "Properties" : {
        "<a href="#allowplaintextbackup" title="AllowPlaintextBackup">AllowPlaintextBackup</a>" : <i>Boolean</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#convergentencryption" title="ConvergentEncryption">ConvergentEncryption</a>" : <i>Boolean</i>,
        "<a href="#deletionallowed" title="DeletionAllowed">DeletionAllowed</a>" : <i>Boolean</i>,
        "<a href="#derived" title="Derived">Derived</a>" : <i>Boolean</i>,
        "<a href="#exportable" title="Exportable">Exportable</a>" : <i>Boolean</i>,
        "<a href="#mindecryptionversion" title="MinDecryptionVersion">MinDecryptionVersion</a>" : <i>Double</i>,
        "<a href="#minencryptionversion" title="MinEncryptionVersion">MinEncryptionVersion</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::TransitSecretBackendKey
Properties:
    <a href="#allowplaintextbackup" title="AllowPlaintextBackup">AllowPlaintextBackup</a>: <i>Boolean</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#convergentencryption" title="ConvergentEncryption">ConvergentEncryption</a>: <i>Boolean</i>
    <a href="#deletionallowed" title="DeletionAllowed">DeletionAllowed</a>: <i>Boolean</i>
    <a href="#derived" title="Derived">Derived</a>: <i>Boolean</i>
    <a href="#exportable" title="Exportable">Exportable</a>: <i>Boolean</i>
    <a href="#mindecryptionversion" title="MinDecryptionVersion">MinDecryptionVersion</a>: <i>Double</i>
    <a href="#minencryptionversion" title="MinEncryptionVersion">MinEncryptionVersion</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AllowPlaintextBackup

Enables taking backup of entire keyring in the plaintext format. Once set, this cannot be disabled.
* Refer to Vault API documentation on key backups for more information: [Backup Key](https://www.vaultproject.io/api/secret/transit/index.html#backup-key).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The path the transit secret backend is mounted at, with no leading or trailing `/`s.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvergentEncryption

Whether or not to support convergent encryption, where the same plaintext creates the same ciphertext. This requires `derived` to be set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionAllowed

Specifies if the keyring is allowed to be deleted. Must be set to 'true' before terraform will be able to destroy keys.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Derived

Specifies if key derivation is to be used. If enabled, all encrypt/decrypt requests to this key must provide a context which is used for key derivation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exportable

Enables keys to be exportable. This allows for all valid private keys in the keyring to be exported. Once set, this cannot be disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDecryptionVersion

Minimum key version to use for decryption.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinEncryptionVersion

Minimum key version to use for encryption.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name to identify this key within the backend. Must be unique within the backend.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the type of key to create. The currently-supported types are: `aes256-gcm96` (default), `chacha20-poly1305`, `ed25519`, `ecdsa-p256`, `rsa-2048` and `rsa-4096`.
* Refer to the Vault documentation on transit key types for more information: [Key Types](https://www.vaultproject.io/docs/secrets/transit/index.html#key-types).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Keys

Returns the <code>Keys</code> value.

#### LatestVersion

Returns the <code>LatestVersion</code> value.

#### MinAvailableVersion

Returns the <code>MinAvailableVersion</code> value.

#### SupportsDecryption

Returns the <code>SupportsDecryption</code> value.

#### SupportsDerivation

Returns the <code>SupportsDerivation</code> value.

#### SupportsEncryption

Returns the <code>SupportsEncryption</code> value.

#### SupportsSigning

Returns the <code>SupportsSigning</code> value.

