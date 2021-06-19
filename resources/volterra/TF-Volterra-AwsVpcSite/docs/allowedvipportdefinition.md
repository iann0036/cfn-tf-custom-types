# TF::Volterra::AwsVpcSite AllowedVipPortDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#usehttphttpsport" title="UseHttpHttpsPort">UseHttpHttpsPort</a>" : <i>Boolean</i>,
    "<a href="#usehttpport" title="UseHttpPort">UseHttpPort</a>" : <i>Boolean</i>,
    "<a href="#usehttpsport" title="UseHttpsPort">UseHttpsPort</a>" : <i>Boolean</i>,
    "<a href="#customports" title="CustomPorts">CustomPorts</a>" : <i>[ <a href="customportsdefinition.md">CustomPortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#usehttphttpsport" title="UseHttpHttpsPort">UseHttpHttpsPort</a>: <i>Boolean</i>
<a href="#usehttpport" title="UseHttpPort">UseHttpPort</a>: <i>Boolean</i>
<a href="#usehttpsport" title="UseHttpsPort">UseHttpsPort</a>: <i>Boolean</i>
<a href="#customports" title="CustomPorts">CustomPorts</a>: <i>
      - <a href="customportsdefinition.md">CustomPortsDefinition</a></i>
</pre>

## Properties

#### UseHttpHttpsPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHttpPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHttpsPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPorts

_Required_: No

_Type_: List of <a href="customportsdefinition.md">CustomPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

