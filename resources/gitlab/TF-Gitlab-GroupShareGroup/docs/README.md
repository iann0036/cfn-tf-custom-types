# TF::Gitlab::GroupShareGroup

This resource allows you to share a group with another group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::GroupShareGroup",
    "Properties" : {
        "<a href="#expiresat" title="ExpiresAt">ExpiresAt</a>" : <i>String</i>,
        "<a href="#groupaccess" title="GroupAccess">GroupAccess</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#sharegroupid" title="ShareGroupId">ShareGroupId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::GroupShareGroup
Properties:
    <a href="#expiresat" title="ExpiresAt">ExpiresAt</a>: <i>String</i>
    <a href="#groupaccess" title="GroupAccess">GroupAccess</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#sharegroupid" title="ShareGroupId">ShareGroupId</a>: <i>Double</i>
</pre>

## Properties

#### ExpiresAt

Share expiration date. Format: `YYYY-MM-DD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAccess

One of five levels of access to the group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The id of the main group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareGroupId

The id of an additional group which will be shared with the main group.

_Required_: Yes

_Type_: Double

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

