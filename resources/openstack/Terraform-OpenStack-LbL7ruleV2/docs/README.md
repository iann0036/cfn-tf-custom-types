# Terraform::OpenStack::LbL7ruleV2

Manages a V2 L7 Rule resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::LbL7ruleV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#comparetype" title="CompareType">CompareType</a>" : <i>String</i>,
        "<a href="#invert" title="Invert">Invert</a>" : <i>Boolean</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#l7policyid" title="L7policyId">L7policyId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::LbL7ruleV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#comparetype" title="CompareType">CompareType</a>: <i>String</i>
    <a href="#invert" title="Invert">Invert</a>: <i>Boolean</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#l7policyid" title="L7policyId">L7policyId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminStateUp

The administrative state of the L7 Rule.
A valid value is true (UP) or false (DOWN).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareType

The comparison type for the L7 rule - can either be
CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Invert

When true the logic of the rule is inverted. For example, with invert
true, equal to would become not equal to. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The key to use for the comparison. For example, the name of the cookie to
evaluate. Valid when `type` is set to COOKIE or HEADER.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L7policyId

The ID of the L7 Policy to query. Changing this creates a new
L7 Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
L7 Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Required for admins. The UUID of the tenant who owns
the L7 Rule.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
HOST\_NAME or PATH.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value to use for the comparison. For example, the file type to
compare.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ListenerId

Returns the <code>ListenerId</code> value.

