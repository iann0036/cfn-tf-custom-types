# Terraform::TencentCloud::DayuCcHttpsPolicy

Use this resource to create a dayu CC self-define https policy

~> **NOTE:** creating CC self-define https policy need a valid resource `tencentcloud_dayu_l7_rule`; The resource only support Anti-DDoS of resource type `bgpip`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuCcHttpsPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
        "<a href="#switch" title="Switch">Switch</a>" : <i>Boolean</i>,
        "<a href="#rulelist" title="RuleList">RuleList</a>" : <i>[ <a href="rulelist.md">RuleList</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuCcHttpsPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
    <a href="#switch" title="Switch">Switch</a>: <i>Boolean</i>
    <a href="#rulelist" title="RuleList">RuleList</a>: <i>
      - <a href="rulelist.md">RuleList</a></i>
</pre>

## Properties

#### Action

Action mode. Valid values are `alg` and `drop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the CC self-define https policy. Length should between 1 and 20.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

ID of the resource that the CC self-define https policy works for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Switch

Indicate the CC self-define https policy takes effect or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleList

_Required_: No

_Type_: List of <a href="rulelist.md">RuleList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpList

Returns the <code>IpList</code> value.

#### PolicyId

Returns the <code>PolicyId</code> value.

