# TF::Volterra::VirtualNetwork StaticRoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attrs" title="Attrs">Attrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>" : <i>Boolean</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ipprefixes" title="IpPrefixes">IpPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attrs" title="Attrs">Attrs</a>: <i>
      - String</i>
<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>: <i>Boolean</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ipprefixes" title="IpPrefixes">IpPrefixes</a>: <i>
      - String</i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
</pre>

## Properties

#### Attrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

