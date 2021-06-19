# TF::VCD::ExternalNetworkV2 IpScopeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dns1" title="Dns1">Dns1</a>" : <i>String</i>,
    "<a href="#dns2" title="Dns2">Dns2</a>" : <i>String</i>,
    "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
    "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ <a href="staticippooldefinition.md">StaticIpPoolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dns1" title="Dns1">Dns1</a>: <i>String</i>
<a href="#dns2" title="Dns2">Dns2</a>: <i>String</i>
<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - <a href="staticippooldefinition.md">StaticIpPoolDefinition</a></i>
</pre>

## Properties

#### Dns1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No

_Type_: List of <a href="staticippooldefinition.md">StaticIpPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

