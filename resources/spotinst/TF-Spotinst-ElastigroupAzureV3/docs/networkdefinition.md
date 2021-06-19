# TF::Spotinst::ElastigroupAzureV3 NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
    "<a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>" : <i>String</i>,
    "<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>" : <i>[ <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
<a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>: <i>String</i>
<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>: <i>
      - <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a></i>
</pre>

## Properties

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaces

_Required_: No

_Type_: List of <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

