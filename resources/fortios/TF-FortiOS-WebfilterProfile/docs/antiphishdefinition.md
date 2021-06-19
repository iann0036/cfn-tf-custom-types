# TF::FortiOS::WebfilterProfile AntiphishDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkbasicauth" title="CheckBasicAuth">CheckBasicAuth</a>" : <i>String</i>,
    "<a href="#checkuri" title="CheckUri">CheckUri</a>" : <i>String</i>,
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#domaincontroller" title="DomainController">DomainController</a>" : <i>String</i>,
    "<a href="#maxbodylen" title="MaxBodyLen">MaxBodyLen</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#custompatterns" title="CustomPatterns">CustomPatterns</a>" : <i>[ <a href="custompatternsdefinition.md">CustomPatternsDefinition</a>, ... ]</i>,
    "<a href="#inspectionentries" title="InspectionEntries">InspectionEntries</a>" : <i>[ <a href="inspectionentriesdefinition.md">InspectionEntriesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#checkbasicauth" title="CheckBasicAuth">CheckBasicAuth</a>: <i>String</i>
<a href="#checkuri" title="CheckUri">CheckUri</a>: <i>String</i>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#domaincontroller" title="DomainController">DomainController</a>: <i>String</i>
<a href="#maxbodylen" title="MaxBodyLen">MaxBodyLen</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#custompatterns" title="CustomPatterns">CustomPatterns</a>: <i>
      - <a href="custompatternsdefinition.md">CustomPatternsDefinition</a></i>
<a href="#inspectionentries" title="InspectionEntries">InspectionEntries</a>: <i>
      - <a href="inspectionentriesdefinition.md">InspectionEntriesDefinition</a></i>
</pre>

## Properties

#### CheckBasicAuth

Enable/disable checking of HTTP Basic Auth field for known credentials. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckUri

Enable/disable checking of GET URI parameters for known credentials. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

Action to be taken when there is no matching rule. Valid values: `exempt`, `log`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainController

Domain for which to verify received credentials against.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBodyLen

Maximum size of a POST body to check for credentials.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Toggle AntiPhishing functionality. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPatterns

_Required_: No

_Type_: List of <a href="custompatternsdefinition.md">CustomPatternsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionEntries

_Required_: No

_Type_: List of <a href="inspectionentriesdefinition.md">InspectionEntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

