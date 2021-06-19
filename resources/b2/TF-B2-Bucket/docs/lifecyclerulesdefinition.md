# TF::B2::Bucket LifecycleRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#daysfromhidingtodeleting" title="DaysFromHidingToDeleting">DaysFromHidingToDeleting</a>" : <i>Double</i>,
    "<a href="#daysfromuploadingtohiding" title="DaysFromUploadingToHiding">DaysFromUploadingToHiding</a>" : <i>Double</i>,
    "<a href="#filenameprefix" title="FileNamePrefix">FileNamePrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#daysfromhidingtodeleting" title="DaysFromHidingToDeleting">DaysFromHidingToDeleting</a>: <i>Double</i>
<a href="#daysfromuploadingtohiding" title="DaysFromUploadingToHiding">DaysFromUploadingToHiding</a>: <i>Double</i>
<a href="#filenameprefix" title="FileNamePrefix">FileNamePrefix</a>: <i>String</i>
</pre>

## Properties

#### DaysFromHidingToDeleting

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysFromUploadingToHiding

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileNamePrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

