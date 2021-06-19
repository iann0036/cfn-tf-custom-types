# TF::Quorum::BootstrapAccount

Use this resource to create a new Ethereum account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapAccount",
    "Properties" : {
        "<a href="#balance" title="Balance">Balance</a>" : <i>String</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#walletid" title="WalletId">WalletId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapAccount
Properties:
    <a href="#balance" title="Balance">Balance</a>: <i>String</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#walletid" title="WalletId">WalletId</a>: <i>String</i>
</pre>

## Properties

#### Balance

A place holder to keep account initial balance for referencing
- `passphrase` - (Optional) Passphrase to lock/unlock the account. Default is empty
- `wallet_id` - (Required) ID of a wallet storing the newly created account. For keystore, it's the keystore resource id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

Passphrase to lock/unlock the account. Default is empty
- `wallet_id` - (Required) ID of a wallet storing the newly created account. For keystore, it's the keystore resource id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WalletId

ID of a wallet storing the newly created account. For keystore, it's the keystore resource id.

_Required_: Yes

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

#### AccountUrl

Returns the <code>AccountUrl</code> value.

#### Address

Returns the <code>Address</code> value.

#### Id

Returns the <code>Id</code> value.

