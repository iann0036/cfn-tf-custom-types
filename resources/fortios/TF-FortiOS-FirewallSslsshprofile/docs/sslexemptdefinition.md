# TF::FortiOS::FirewallSslsshprofile SslExemptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#address6" title="Address6">Address6</a>" : <i>String</i>,
    "<a href="#fortiguardcategory" title="FortiguardCategory">FortiguardCategory</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#wildcardfqdn" title="WildcardFqdn">WildcardFqdn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#address6" title="Address6">Address6</a>: <i>String</i>
<a href="#fortiguardcategory" title="FortiguardCategory">FortiguardCategory</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#regex" title="Regex">Regex</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#wildcardfqdn" title="WildcardFqdn">WildcardFqdn</a>: <i>String</i>
</pre>

## Properties

#### Address

IPv4 address object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Address6

IPv6 address object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCategory

FortiGuard category ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

Exempt servers by regular expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of address object (IPv4 or IPv6) or FortiGuard category. Valid values: `fortiguard-category`, `address`, `address6`, `wildcard-fqdn`, `regex`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildcardFqdn

Exempt servers by wildcard FQDN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

