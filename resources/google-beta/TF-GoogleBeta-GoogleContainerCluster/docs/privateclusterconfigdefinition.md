# TF::GoogleBeta::GoogleContainerCluster PrivateClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableprivateendpoint" title="EnablePrivateEndpoint">EnablePrivateEndpoint</a>" : <i>Boolean</i>,
    "<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>" : <i>Boolean</i>,
    "<a href="#masteripv4cidrblock" title="MasterIpv4CidrBlock">MasterIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#masterglobalaccessconfig" title="MasterGlobalAccessConfig">MasterGlobalAccessConfig</a>" : <i>[ <a href="masterglobalaccessconfigdefinition.md">MasterGlobalAccessConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableprivateendpoint" title="EnablePrivateEndpoint">EnablePrivateEndpoint</a>: <i>Boolean</i>
<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>: <i>Boolean</i>
<a href="#masteripv4cidrblock" title="MasterIpv4CidrBlock">MasterIpv4CidrBlock</a>: <i>String</i>
<a href="#masterglobalaccessconfig" title="MasterGlobalAccessConfig">MasterGlobalAccessConfig</a>: <i>
      - <a href="masterglobalaccessconfigdefinition.md">MasterGlobalAccessConfigDefinition</a></i>
</pre>

## Properties

#### EnablePrivateEndpoint

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterIpv4CidrBlock

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterGlobalAccessConfig

_Required_: No

_Type_: List of <a href="masterglobalaccessconfigdefinition.md">MasterGlobalAccessConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

