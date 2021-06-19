# TF::Volterra::Bgp PeersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#targetservice" title="TargetService">TargetService</a>" : <i>String</i>,
    "<a href="#external" title="External">External</a>" : <i>[ <a href="externaldefinition.md">ExternalDefinition</a>, ... ]</i>,
    "<a href="#internal" title="Internal">Internal</a>" : <i>[ <a href="internaldefinition.md">InternalDefinition</a>, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#targetservice" title="TargetService">TargetService</a>: <i>String</i>
<a href="#external" title="External">External</a>: <i>
      - <a href="externaldefinition.md">ExternalDefinition</a></i>
<a href="#internal" title="Internal">Internal</a>: <i>
      - <a href="internaldefinition.md">InternalDefinition</a></i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
</pre>

## Properties

#### TargetService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

_Required_: No

_Type_: List of <a href="externaldefinition.md">ExternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

_Required_: No

_Type_: List of <a href="internaldefinition.md">InternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

