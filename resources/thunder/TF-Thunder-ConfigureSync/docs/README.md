# TF::Thunder::ConfigureSync

`thunder_configure_sync` provides details about Configure Sync

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::ConfigureSync",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#allpartitions" title="AllPartitions">AllPartitions</a>" : <i>Double</i>,
        "<a href="#autoauthentication" title="AutoAuthentication">AutoAuthentication</a>" : <i>Double</i>,
        "<a href="#partitionname" title="PartitionName">PartitionName</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#pwd" title="Pwd">Pwd</a>" : <i>String</i>,
        "<a href="#pwdenc" title="PwdEnc">PwdEnc</a>" : <i>String</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usr" title="Usr">Usr</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::ConfigureSync
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#allpartitions" title="AllPartitions">AllPartitions</a>: <i>Double</i>
    <a href="#autoauthentication" title="AutoAuthentication">AutoAuthentication</a>: <i>Double</i>
    <a href="#partitionname" title="PartitionName">PartitionName</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#pwd" title="Pwd">Pwd</a>: <i>String</i>
    <a href="#pwdenc" title="PwdEnc">PwdEnc</a>: <i>String</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usr" title="Usr">Usr</a>: <i>String</i>
</pre>

## Properties

#### Address

Specify the destination ip address to sync.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllPartitions

All partition configurations.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAuthentication

Authenticate with local username and password.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionName

Partition name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

Use private key for authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pwd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PwdEnc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

Shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

‘running’: Sync local running to peer’s running configuration; ‘all’: Sync local running to peer’s running configuration, and local startup to peer’s startup configuration;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usr

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

#### Id

Returns the <code>Id</code> value.

