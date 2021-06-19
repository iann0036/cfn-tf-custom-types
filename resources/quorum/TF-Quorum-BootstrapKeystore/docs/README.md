# TF::Quorum::BootstrapKeystore

Use this resource to create a keystore which maintains multiple Ethereum accounts.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapKeystore",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>[ <a href="accountdefinition.md">AccountDefinition</a>, ... ]</i>,
        "<a href="#keystoredir" title="KeystoreDir">KeystoreDir</a>" : <i>String</i>,
        "<a href="#uselightweightkdf" title="UseLightWeightKdf">UseLightWeightKdf</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapKeystore
Properties:
    <a href="#account" title="Account">Account</a>: <i>
      - <a href="accountdefinition.md">AccountDefinition</a></i>
    <a href="#keystoredir" title="KeystoreDir">KeystoreDir</a>: <i>String</i>
    <a href="#uselightweightkdf" title="UseLightWeightKdf">UseLightWeightKdf</a>: <i>Boolean</i>
</pre>

## Properties

#### Account

Account being created under this keystore.

_Required_: No

_Type_: List of <a href="accountdefinition.md">AccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeystoreDir

Directory contains private keys
- `use_light_weight_kdf` - (Optional) True to lower the memory and CPU requirements of the key store scrypt KDF at the expense of security.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLightWeightKdf

True to lower the memory and CPU requirements of the key store scrypt KDF at the expense of security.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### KeystoreDirAbs

Returns the <code>KeystoreDirAbs</code> value.

