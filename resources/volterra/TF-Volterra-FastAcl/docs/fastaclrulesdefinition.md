# TF::Volterra::FastAcl FastAclRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>" : <i>[ <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>[ <a href="prefixdefinition.md">PrefixDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>: <i>
      - <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a></i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>
      - <a href="prefixdefinition.md">PrefixDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixSet

_Required_: No

_Type_: List of <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: List of <a href="prefixdefinition.md">PrefixDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

