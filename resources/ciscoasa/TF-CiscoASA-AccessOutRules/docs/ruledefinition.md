# TF::CiscoASA::AccessOutRules RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
    "<a href="#destinationservice" title="DestinationService">DestinationService</a>" : <i>String</i>,
    "<a href="#permit" title="Permit">Permit</a>" : <i>Boolean</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#sourceservice" title="SourceService">SourceService</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#active" title="Active">Active</a>: <i>Boolean</i>
<a href="#destination" title="Destination">Destination</a>: <i>String</i>
<a href="#destinationservice" title="DestinationService">DestinationService</a>: <i>String</i>
<a href="#permit" title="Permit">Permit</a>: <i>Boolean</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#sourceservice" title="SourceService">SourceService</a>: <i>String</i>
</pre>

## Properties

#### Active

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationService

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

