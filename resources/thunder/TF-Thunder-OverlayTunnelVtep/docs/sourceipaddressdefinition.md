# TF::Thunder::OverlayTunnelVtep SourceIpAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#vnilist" title="VniList">VniList</a>" : <i>[ <a href="vnilistdefinition.md">VniListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#vnilist" title="VniList">VniList</a>: <i>
      - <a href="vnilistdefinition.md">VniListDefinition</a></i>
</pre>

## Properties

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VniList

_Required_: No

_Type_: List of <a href="vnilistdefinition.md">VniListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

