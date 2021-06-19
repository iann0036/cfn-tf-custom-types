# TF::AVI::Systemconfiguration DnsConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#searchdomain" title="SearchDomain">SearchDomain</a>" : <i>String</i>,
    "<a href="#serverlist" title="ServerList">ServerList</a>" : <i>[ <a href="serverlistdefinition.md">ServerListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#searchdomain" title="SearchDomain">SearchDomain</a>: <i>String</i>
<a href="#serverlist" title="ServerList">ServerList</a>: <i>
      - <a href="serverlistdefinition.md">ServerListDefinition</a></i>
</pre>

## Properties

#### SearchDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerList

_Required_: No

_Type_: List of <a href="serverlistdefinition.md">ServerListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

