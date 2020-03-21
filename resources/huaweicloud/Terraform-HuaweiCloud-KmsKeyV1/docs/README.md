# Terraform::HuaweiCloud::KmsKeyV1

CloudFormation equivalent of huaweicloud_kms_key_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::KmsKeyV1",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#keyalias" title="KeyAlias">KeyAlias</a>" : <i>String</i>,
        "<a href="#keydescription" title="KeyDescription">KeyDescription</a>" : <i>String</i>,
        "<a href="#pendingdays" title="PendingDays">PendingDays</a>" : <i>String</i>,
        "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::KmsKeyV1
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#keyalias" title="KeyAlias">KeyAlias</a>: <i>String</i>
    <a href="#keydescription" title="KeyDescription">KeyDescription</a>: <i>String</i>
    <a href="#pendingdays" title="PendingDays">PendingDays</a>: <i>String</i>
    <a href="#realm" title="Realm">Realm</a>: <i>String</i>
</pre>

## Properties

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlias

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingDays

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

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

#### CreationDate

Returns the <code>CreationDate</code> value.

#### DefaultKeyFlag

Returns the <code>DefaultKeyFlag</code> value.

#### DomainId

Returns the <code>DomainId</code> value.

#### ExpirationTime

Returns the <code>ExpirationTime</code> value.

#### KeyId

Returns the <code>KeyId</code> value.

#### ScheduledDeletionDate

Returns the <code>ScheduledDeletionDate</code> value.

