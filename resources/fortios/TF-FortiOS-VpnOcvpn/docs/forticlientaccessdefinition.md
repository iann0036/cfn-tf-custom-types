# TF::FortiOS::VpnOcvpn ForticlientAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#psksecret" title="Psksecret">Psksecret</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#authgroups" title="AuthGroups">AuthGroups</a>" : <i>[ <a href="authgroupsdefinition.md">AuthGroupsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#psksecret" title="Psksecret">Psksecret</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#authgroups" title="AuthGroups">AuthGroups</a>: <i>
      - <a href="authgroupsdefinition.md">AuthGroupsDefinition</a></i>
</pre>

## Properties

#### Psksecret

Pre-shared secret for FortiClient PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable FortiClient to access OCVPN networks. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthGroups

_Required_: No

_Type_: List of <a href="authgroupsdefinition.md">AuthGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

