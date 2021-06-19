# TF::Google::OsConfigPatchDeployment PatchConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rebootconfig" title="RebootConfig">RebootConfig</a>" : <i>String</i>,
    "<a href="#apt" title="Apt">Apt</a>" : <i>[ <a href="aptdefinition.md">AptDefinition</a>, ... ]</i>,
    "<a href="#goo" title="Goo">Goo</a>" : <i>[ <a href="goodefinition.md">GooDefinition</a>, ... ]</i>,
    "<a href="#poststep" title="PostStep">PostStep</a>" : <i>[ <a href="poststepdefinition.md">PostStepDefinition</a>, ... ]</i>,
    "<a href="#prestep" title="PreStep">PreStep</a>" : <i>[ <a href="prestepdefinition.md">PreStepDefinition</a>, ... ]</i>,
    "<a href="#windowsupdate" title="WindowsUpdate">WindowsUpdate</a>" : <i>[ <a href="windowsupdatedefinition.md">WindowsUpdateDefinition</a>, ... ]</i>,
    "<a href="#yum" title="Yum">Yum</a>" : <i>[ <a href="yumdefinition.md">YumDefinition</a>, ... ]</i>,
    "<a href="#zypper" title="Zypper">Zypper</a>" : <i>[ <a href="zypperdefinition.md">ZypperDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rebootconfig" title="RebootConfig">RebootConfig</a>: <i>String</i>
<a href="#apt" title="Apt">Apt</a>: <i>
      - <a href="aptdefinition.md">AptDefinition</a></i>
<a href="#goo" title="Goo">Goo</a>: <i>
      - <a href="goodefinition.md">GooDefinition</a></i>
<a href="#poststep" title="PostStep">PostStep</a>: <i>
      - <a href="poststepdefinition.md">PostStepDefinition</a></i>
<a href="#prestep" title="PreStep">PreStep</a>: <i>
      - <a href="prestepdefinition.md">PreStepDefinition</a></i>
<a href="#windowsupdate" title="WindowsUpdate">WindowsUpdate</a>: <i>
      - <a href="windowsupdatedefinition.md">WindowsUpdateDefinition</a></i>
<a href="#yum" title="Yum">Yum</a>: <i>
      - <a href="yumdefinition.md">YumDefinition</a></i>
<a href="#zypper" title="Zypper">Zypper</a>: <i>
      - <a href="zypperdefinition.md">ZypperDefinition</a></i>
</pre>

## Properties

#### RebootConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Apt

_Required_: No

_Type_: List of <a href="aptdefinition.md">AptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Goo

_Required_: No

_Type_: List of <a href="goodefinition.md">GooDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostStep

_Required_: No

_Type_: List of <a href="poststepdefinition.md">PostStepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStep

_Required_: No

_Type_: List of <a href="prestepdefinition.md">PreStepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsUpdate

_Required_: No

_Type_: List of <a href="windowsupdatedefinition.md">WindowsUpdateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yum

_Required_: No

_Type_: List of <a href="yumdefinition.md">YumDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zypper

_Required_: No

_Type_: List of <a href="zypperdefinition.md">ZypperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

