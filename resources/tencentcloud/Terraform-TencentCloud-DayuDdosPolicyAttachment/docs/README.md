# Terraform::TencentCloud::DayuDdosPolicyAttachment

Provides a resource to create a dayu DDoS policy attachment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuDdosPolicyAttachment",
    "Properties" : {
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuDdosPolicyAttachment
Properties:
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
</pre>

## Properties

#### PolicyId

Id of the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

Id of the attached resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the DDoS policy works for, valid values are `bgpip`, `bgp`, `bgp-multip`, `net`.

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

