# TF::Alicloud::KmsKey

This resouce used to create a secret and store its initial version.

-> **NOTE:** Available in 1.76.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::KmsKey",
    "Properties" : {
        "<a href="#automaticrotation" title="AutomaticRotation">AutomaticRotation</a>" : <i>String</i>,
        "<a href="#deletionwindowindays" title="DeletionWindowInDays">DeletionWindowInDays</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#keyspec" title="KeySpec">KeySpec</a>" : <i>String</i>,
        "<a href="#keystate" title="KeyState">KeyState</a>" : <i>String</i>,
        "<a href="#keyusage" title="KeyUsage">KeyUsage</a>" : <i>String</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
        "<a href="#pendingwindowindays" title="PendingWindowInDays">PendingWindowInDays</a>" : <i>Double</i>,
        "<a href="#protectionlevel" title="ProtectionLevel">ProtectionLevel</a>" : <i>String</i>,
        "<a href="#rotationinterval" title="RotationInterval">RotationInterval</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::KmsKey
Properties:
    <a href="#automaticrotation" title="AutomaticRotation">AutomaticRotation</a>: <i>String</i>
    <a href="#deletionwindowindays" title="DeletionWindowInDays">DeletionWindowInDays</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#keyspec" title="KeySpec">KeySpec</a>: <i>String</i>
    <a href="#keystate" title="KeyState">KeyState</a>: <i>String</i>
    <a href="#keyusage" title="KeyUsage">KeyUsage</a>: <i>String</i>
    <a href="#origin" title="Origin">Origin</a>: <i>String</i>
    <a href="#pendingwindowindays" title="PendingWindowInDays">PendingWindowInDays</a>: <i>Double</i>
    <a href="#protectionlevel" title="ProtectionLevel">ProtectionLevel</a>: <i>String</i>
    <a href="#rotationinterval" title="RotationInterval">RotationInterval</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### AutomaticRotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionWindowInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySpec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingWindowInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

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

#### Arn

Returns the <code>Arn</code> value.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### Creator

Returns the <code>Creator</code> value.

#### DeleteDate

Returns the <code>DeleteDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastRotationDate

Returns the <code>LastRotationDate</code> value.

#### MaterialExpireTime

Returns the <code>MaterialExpireTime</code> value.

#### NextRotationDate

Returns the <code>NextRotationDate</code> value.

#### PrimaryKeyVersion

Returns the <code>PrimaryKeyVersion</code> value.

