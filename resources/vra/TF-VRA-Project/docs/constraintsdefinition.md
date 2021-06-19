# TF::VRA::Project ConstraintsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#extensibility" title="Extensibility">Extensibility</a>" : <i>[ <a href="extensibilitydefinition.md">ExtensibilityDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
    "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storagedefinition.md">StorageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#extensibility" title="Extensibility">Extensibility</a>: <i>
      - <a href="extensibilitydefinition.md">ExtensibilityDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
<a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storagedefinition.md">StorageDefinition</a></i>
</pre>

## Properties

#### Extensibility

_Required_: No

_Type_: List of <a href="extensibilitydefinition.md">ExtensibilityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storagedefinition.md">StorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

