# Terraform::VCD::ExternalNetwork IpScope

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dns1" title="Dns1">Dns1</a>" : <i>String</i>,
    "<a href="#dns2" title="Dns2">Dns2</a>" : <i>String</i>,
    "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
    "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ <a href="ipscope-staticippool.md">StaticIpPool</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dns1" title="Dns1">Dns1</a>: <i>String</i>
<a href="#dns2" title="Dns2">Dns2</a>: <i>String</i>
<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - <a href="ipscope-staticippool.md">StaticIpPool</a></i>
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

#### Gateway

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No
_Type_: List of <a href="ipscope-staticippool.md">StaticIpPool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

