# TF::Circonus::OverlaySet OverlaysDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#dataopts" title="DataOpts">DataOpts</a>" : <i>[ <a href="dataoptsdefinition.md">DataOptsDefinition</a>, ... ]</i>,
    "<a href="#uispecs" title="UiSpecs">UiSpecs</a>" : <i>[ <a href="uispecsdefinition.md">UiSpecsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#dataopts" title="DataOpts">DataOpts</a>: <i>
      - <a href="dataoptsdefinition.md">DataOptsDefinition</a></i>
<a href="#uispecs" title="UiSpecs">UiSpecs</a>: <i>
      - <a href="uispecsdefinition.md">UiSpecsDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataOpts

_Required_: No

_Type_: List of <a href="dataoptsdefinition.md">DataOptsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiSpecs

_Required_: No

_Type_: List of <a href="uispecsdefinition.md">UiSpecsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

