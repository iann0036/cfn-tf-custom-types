# TF::FortiOS::Wirelesscontrollerhotspot20H2qposuprovider ServiceDescriptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lang" title="Lang">Lang</a>" : <i>String</i>,
    "<a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>" : <i>[ <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a>, ... ]</i>,
    "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#lang" title="Lang">Lang</a>: <i>String</i>
<a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>: <i>
      - <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a></i>
<a href="#serviceid" title="ServiceId">ServiceId</a>: <i>Double</i>
</pre>

## Properties

#### Lang

Language code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDescription

_Required_: No

_Type_: List of <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

OSU service ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

