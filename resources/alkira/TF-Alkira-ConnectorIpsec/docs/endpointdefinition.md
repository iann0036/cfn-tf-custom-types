# TF::Alkira::ConnectorIpsec EndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customergatewayasn" title="CustomerGatewayAsn">CustomerGatewayAsn</a>" : <i>String</i>,
    "<a href="#customergatewayip" title="CustomerGatewayIp">CustomerGatewayIp</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#presharedkeys" title="PresharedKeys">PresharedKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#advanced" title="Advanced">Advanced</a>" : <i>[ <a href="advanceddefinition.md">AdvancedDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customergatewayasn" title="CustomerGatewayAsn">CustomerGatewayAsn</a>: <i>String</i>
<a href="#customergatewayip" title="CustomerGatewayIp">CustomerGatewayIp</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#presharedkeys" title="PresharedKeys">PresharedKeys</a>: <i>
      - String</i>
<a href="#advanced" title="Advanced">Advanced</a>: <i>
      - <a href="advanceddefinition.md">AdvancedDefinition</a></i>
</pre>

## Properties

#### CustomerGatewayAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerGatewayIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresharedKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Advanced

_Required_: No

_Type_: List of <a href="advanceddefinition.md">AdvancedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

