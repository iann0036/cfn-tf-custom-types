# Terraform::Circonus::OverlaySet Overlays

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#dataopts" title="DataOpts">DataOpts</a>" : <i>[ <a href="overlays-dataopts.md">DataOpts</a>, ... ]</i>,
    "<a href="#uispecs" title="UiSpecs">UiSpecs</a>" : <i>[ <a href="overlays-uispecs.md">UiSpecs</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#dataopts" title="DataOpts">DataOpts</a>: <i>
      - <a href="overlays-dataopts.md">DataOpts</a></i>
<a href="#uispecs" title="UiSpecs">UiSpecs</a>: <i>
      - <a href="overlays-uispecs.md">UiSpecs</a></i>
</pre>

## Properties

#### Id

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataOpts

_Required_: No
_Type_: List of <a href="overlays-dataopts.md">DataOpts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiSpecs

_Required_: No
_Type_: List of <a href="overlays-uispecs.md">UiSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

