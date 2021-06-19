# TF::Volterra::Fleet FlashArrayDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultfsopt" title="DefaultFsOpt">DefaultFsOpt</a>" : <i>String</i>,
    "<a href="#defaultfstype" title="DefaultFsType">DefaultFsType</a>" : <i>String</i>,
    "<a href="#defaultmountopts" title="DefaultMountOpts">DefaultMountOpts</a>" : <i>[ String, ... ]</i>,
    "<a href="#disablepreemptattachments" title="DisablePreemptAttachments">DisablePreemptAttachments</a>" : <i>Boolean</i>,
    "<a href="#iscsilogintimeout" title="IscsiLoginTimeout">IscsiLoginTimeout</a>" : <i>Double</i>,
    "<a href="#santype" title="SanType">SanType</a>" : <i>String</i>,
    "<a href="#flasharrays" title="FlashArrays">FlashArrays</a>" : <i>[ <a href="flasharraysdefinition.md">FlashArraysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultfsopt" title="DefaultFsOpt">DefaultFsOpt</a>: <i>String</i>
<a href="#defaultfstype" title="DefaultFsType">DefaultFsType</a>: <i>String</i>
<a href="#defaultmountopts" title="DefaultMountOpts">DefaultMountOpts</a>: <i>
      - String</i>
<a href="#disablepreemptattachments" title="DisablePreemptAttachments">DisablePreemptAttachments</a>: <i>Boolean</i>
<a href="#iscsilogintimeout" title="IscsiLoginTimeout">IscsiLoginTimeout</a>: <i>Double</i>
<a href="#santype" title="SanType">SanType</a>: <i>String</i>
<a href="#flasharrays" title="FlashArrays">FlashArrays</a>: <i>
      - <a href="flasharraysdefinition.md">FlashArraysDefinition</a></i>
</pre>

## Properties

#### DefaultFsOpt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultFsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMountOpts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePreemptAttachments

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiLoginTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlashArrays

_Required_: No

_Type_: List of <a href="flasharraysdefinition.md">FlashArraysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

