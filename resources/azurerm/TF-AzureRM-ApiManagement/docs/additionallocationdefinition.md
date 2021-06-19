# TF::AzureRM::ApiManagement AdditionalLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>" : <i>[ <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#virtualnetworkconfiguration" title="VirtualNetworkConfiguration">VirtualNetworkConfiguration</a>: <i>
      - <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a></i>
</pre>

## Properties

#### Location

The name of the Azure Region in which the API Management Service should be expanded to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkConfiguration

_Required_: No

_Type_: List of <a href="virtualnetworkconfigurationdefinition.md">VirtualNetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

