# Terraform::Vault::TransitSecretBackendKey

CloudFormation equivalent of vault_transit_secret_backend_key

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#mindecryptionversion" title="MinDecryptionVersion">MinDecryptionVersion</a>: <i>Double</i>
    <a href="#minencryptionversion" title="MinEncryptionVersion">MinEncryptionVersion</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AllowPlaintextBackup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvergentEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Derived

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exportable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDecryptionVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinEncryptionVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

