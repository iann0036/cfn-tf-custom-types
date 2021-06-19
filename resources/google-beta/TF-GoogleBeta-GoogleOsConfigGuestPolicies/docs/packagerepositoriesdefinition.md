# TF::GoogleBeta::GoogleOsConfigGuestPolicies PackageRepositoriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apt" title="Apt">Apt</a>" : <i>[ <a href="aptdefinition.md">AptDefinition</a>, ... ]</i>,
    "<a href="#goo" title="Goo">Goo</a>" : <i>[ <a href="goodefinition.md">GooDefinition</a>, ... ]</i>,
    "<a href="#yum" title="Yum">Yum</a>" : <i>[ <a href="yumdefinition.md">YumDefinition</a>, ... ]</i>,
    "<a href="#zypper" title="Zypper">Zypper</a>" : <i>[ <a href="zypperdefinition.md">ZypperDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apt" title="Apt">Apt</a>: <i>
      - <a href="aptdefinition.md">AptDefinition</a></i>
<a href="#goo" title="Goo">Goo</a>: <i>
      - <a href="goodefinition.md">GooDefinition</a></i>
<a href="#yum" title="Yum">Yum</a>: <i>
      - <a href="yumdefinition.md">YumDefinition</a></i>
<a href="#zypper" title="Zypper">Zypper</a>: <i>
      - <a href="zypperdefinition.md">ZypperDefinition</a></i>
</pre>

## Properties

#### Apt

_Required_: No

_Type_: List of <a href="aptdefinition.md">AptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Goo

_Required_: No

_Type_: List of <a href="goodefinition.md">GooDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yum

_Required_: No

_Type_: List of <a href="yumdefinition.md">YumDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zypper

_Required_: No

_Type_: List of <a href="zypperdefinition.md">ZypperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

