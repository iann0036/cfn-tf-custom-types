# Terraform::OVH::IploadbalancingHttpRouteRule

Manage rules for HTTP route.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::IploadbalancingHttpRouteRule",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#field" title="Field">Field</a>" : <i>String</i>,
        "<a href="#match" title="Match">Match</a>" : <i>String</i>,
        "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
        "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
        "<a href="#routeid" title="RouteId">RouteId</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#subfield" title="SubField">SubField</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::IploadbalancingHttpRouteRule
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#field" title="Field">Field</a>: <i>String</i>
    <a href="#match" title="Match">Match</a>: <i>String</i>
    <a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
    <a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
    <a href="#routeid" title="RouteId">RouteId</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#subfield" title="SubField">SubField</a>: <i>String</i>
</pre>

## Properties

#### DisplayName

Human readable name for your rule, this field is for you.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

Name of the field to match like "protocol" or "host". See "/ipLoadbalancing/{serviceName}/availableRouteRules" for a list of available rules.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

Matching operator. Not all operators are available for all fields. See "/ipLoadbalancing/{serviceName}/availableRouteRules".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

Invert the matching operator effect.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

Value to match against this match. Interpretation if this field depends on the match and field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteId

The route to apply this rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The internal name of your IP load balancing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubField

Name of sub-field, if applicable. This may be a Cookie or Header name for instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

