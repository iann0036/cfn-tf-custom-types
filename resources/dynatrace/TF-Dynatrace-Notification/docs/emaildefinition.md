# TF::Dynatrace::Notification EmailDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
    "<a href="#alertingprofile" title="AlertingProfile">AlertingProfile</a>" : <i>String</i>,
    "<a href="#bccreceivers" title="BccReceivers">BccReceivers</a>" : <i>[ String, ... ]</i>,
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#ccreceivers" title="CcReceivers">CcReceivers</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#receivers" title="Receivers">Receivers</a>" : <i>[ String, ... ]</i>,
    "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#active" title="Active">Active</a>: <i>Boolean</i>
<a href="#alertingprofile" title="AlertingProfile">AlertingProfile</a>: <i>String</i>
<a href="#bccreceivers" title="BccReceivers">BccReceivers</a>: <i>
      - String</i>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#ccreceivers" title="CcReceivers">CcReceivers</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#receivers" title="Receivers">Receivers</a>: <i>
      - String</i>
<a href="#subject" title="Subject">Subject</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
</pre>

## Properties

#### Active

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertingProfile

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BccReceivers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CcReceivers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Receivers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

