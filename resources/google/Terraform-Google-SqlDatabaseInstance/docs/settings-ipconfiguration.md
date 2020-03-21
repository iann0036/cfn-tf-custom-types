# Terraform::Google::SqlDatabaseInstance Settings IpConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipv4enabled" title="Ipv4Enabled">Ipv4Enabled</a>" : <i>Boolean</i>,
    "<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>" : <i>String</i>,
    "<a href="#requiressl" title="RequireSsl">RequireSsl</a>" : <i>Boolean</i>,
    "<a href="#authorizednetworks" title="AuthorizedNetworks">AuthorizedNetworks</a>" : <i>[ <a href="settings-ipconfiguration-authorizednetworks.md">AuthorizedNetworks</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipv4enabled" title="Ipv4Enabled">Ipv4Enabled</a>: <i>Boolean</i>
<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>: <i>String</i>
<a href="#requiressl" title="RequireSsl">RequireSsl</a>: <i>Boolean</i>
<a href="#authorizednetworks" title="AuthorizedNetworks">AuthorizedNetworks</a>: <i>
      - <a href="settings-ipconfiguration-authorizednetworks.md">AuthorizedNetworks</a></i>
</pre>

## Properties

#### Ipv4Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetwork

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSsl

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedNetworks

_Required_: No
_Type_: List of <a href="settings-ipconfiguration-authorizednetworks.md">AuthorizedNetworks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

