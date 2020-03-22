# Terraform::Cloudflare::Filter

Filter expressions that can be referenced across multiple features, e.g. [Firewall Rule](firewall_rule.html). The expression format is similar to [Wireshark Display Filter](https://www.wireshark.org/docs/man-pages/wireshark-filter.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::Filter",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
        "<a href="#paused" title="Paused">Paused</a>" : <i>Boolean</i>,
        "<a href="#ref" title="Ref">Ref</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::Filter
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expression" title="Expression">Expression</a>: <i>String</i>
    <a href="#paused" title="Paused">Paused</a>: <i>Boolean</i>
    <a href="#ref" title="Ref">Ref</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### Description

A note that you can use to describe the purpose of the filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expression

The filter expression to be used.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paused

Whether this filter is currently paused. Boolean value.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ref

Short reference tag to quickly select related rules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone to which the Filter should be added.

_Required_: Yes

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

