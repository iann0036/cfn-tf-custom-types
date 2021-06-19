# TF::NSXT::PolicyTier0GatewayHaVipConfig ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#externalinterfacepaths" title="ExternalInterfacePaths">ExternalInterfacePaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#vipsubnets" title="VipSubnets">VipSubnets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#externalinterfacepaths" title="ExternalInterfacePaths">ExternalInterfacePaths</a>: <i>
      - String</i>
<a href="#vipsubnets" title="VipSubnets">VipSubnets</a>: <i>
      - String</i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalInterfacePaths

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipSubnets

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

