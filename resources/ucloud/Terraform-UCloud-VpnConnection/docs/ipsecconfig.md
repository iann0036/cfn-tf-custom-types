# Terraform::UCloud::VpnConnection IpsecConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationalgorithm" title="AuthenticationAlgorithm">AuthenticationAlgorithm</a>" : <i>String</i>,
    "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
    "<a href="#localsubnetids" title="LocalSubnetIds">LocalSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#pfsdhgroup" title="PfsDhGroup">PfsDhGroup</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#remotesubnets" title="RemoteSubnets">RemoteSubnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#salifetime" title="SaLifeTime">SaLifeTime</a>" : <i>Double</i>,
    "<a href="#salifetimebytes" title="SaLifeTimeBytes">SaLifeTimeBytes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationalgorithm" title="AuthenticationAlgorithm">AuthenticationAlgorithm</a>: <i>String</i>
<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
<a href="#localsubnetids" title="LocalSubnetIds">LocalSubnetIds</a>: <i>
      - String</i>
<a href="#pfsdhgroup" title="PfsDhGroup">PfsDhGroup</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#remotesubnets" title="RemoteSubnets">RemoteSubnets</a>: <i>
      - String</i>
<a href="#salifetime" title="SaLifeTime">SaLifeTime</a>: <i>Double</i>
<a href="#salifetimebytes" title="SaLifeTimeBytes">SaLifeTimeBytes</a>: <i>Double</i>
</pre>

## Properties

#### AuthenticationAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PfsDhGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnets

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifeTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaLifeTimeBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

