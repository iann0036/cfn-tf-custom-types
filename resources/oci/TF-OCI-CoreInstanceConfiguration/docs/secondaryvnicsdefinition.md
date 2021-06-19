# TF::OCI::CoreInstanceConfiguration SecondaryVnicsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#nicindex" title="NicIndex">NicIndex</a>" : <i>Double</i>,
    "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#nicindex" title="NicIndex">NicIndex</a>: <i>Double</i>
<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicIndex

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

