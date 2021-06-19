# TF::AVI::Upgradestatusinfo ParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageref" title="ImageRef">ImageRef</a>" : <i>String</i>,
    "<a href="#patchref" title="PatchRef">PatchRef</a>" : <i>String</i>,
    "<a href="#segroupoptions" title="SeGroupOptions">SeGroupOptions</a>" : <i>[ <a href="segroupoptionsdefinition.md">SeGroupOptionsDefinition</a>, ... ]</i>,
    "<a href="#segroupresumeoptions" title="SeGroupResumeOptions">SeGroupResumeOptions</a>" : <i>[ <a href="segroupresumeoptionsdefinition.md">SeGroupResumeOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageref" title="ImageRef">ImageRef</a>: <i>String</i>
<a href="#patchref" title="PatchRef">PatchRef</a>: <i>String</i>
<a href="#segroupoptions" title="SeGroupOptions">SeGroupOptions</a>: <i>
      - <a href="segroupoptionsdefinition.md">SeGroupOptionsDefinition</a></i>
<a href="#segroupresumeoptions" title="SeGroupResumeOptions">SeGroupResumeOptions</a>: <i>
      - <a href="segroupresumeoptionsdefinition.md">SeGroupResumeOptionsDefinition</a></i>
</pre>

## Properties

#### ImageRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupOptions

_Required_: No

_Type_: List of <a href="segroupoptionsdefinition.md">SeGroupOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupResumeOptions

_Required_: No

_Type_: List of <a href="segroupresumeoptionsdefinition.md">SeGroupResumeOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

