# TF::FortiOS::UserQuarantine TargetsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#entry" title="Entry">Entry</a>" : <i>String</i>,
    "<a href="#macs" title="Macs">Macs</a>" : <i>[ <a href="macsdefinition.md">MacsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#entry" title="Entry">Entry</a>: <i>String</i>
<a href="#macs" title="Macs">Macs</a>: <i>
      - <a href="macsdefinition.md">MacsDefinition</a></i>
</pre>

## Properties

#### Description

Description for the quarantine entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entry

Quarantine entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Macs

_Required_: No

_Type_: List of <a href="macsdefinition.md">MacsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

