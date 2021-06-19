# TF::Thunder::SlbTemplatePolicy ForwardPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acoseventlog" title="AcosEventLog">AcosEventLog</a>" : <i>Double</i>,
    "<a href="#locallogging" title="LocalLogging">LocalLogging</a>" : <i>Double</i>,
    "<a href="#noclientconnreuse" title="NoClientConnReuse">NoClientConnReuse</a>" : <i>Double</i>,
    "<a href="#requirewebcategory" title="RequireWebCategory">RequireWebCategory</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#actionlist" title="ActionList">ActionList</a>" : <i>[ <a href="actionlistdefinition.md">ActionListDefinition</a>, ... ]</i>,
    "<a href="#filtering" title="Filtering">Filtering</a>" : <i>[ <a href="filteringdefinition.md">FilteringDefinition</a>, ... ]</i>,
    "<a href="#sanfiltering" title="SanFiltering">SanFiltering</a>" : <i>[ <a href="sanfilteringdefinition.md">SanFilteringDefinition</a>, ... ]</i>,
    "<a href="#sourcelist" title="SourceList">SourceList</a>" : <i>[ <a href="sourcelistdefinition.md">SourceListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acoseventlog" title="AcosEventLog">AcosEventLog</a>: <i>Double</i>
<a href="#locallogging" title="LocalLogging">LocalLogging</a>: <i>Double</i>
<a href="#noclientconnreuse" title="NoClientConnReuse">NoClientConnReuse</a>: <i>Double</i>
<a href="#requirewebcategory" title="RequireWebCategory">RequireWebCategory</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#actionlist" title="ActionList">ActionList</a>: <i>
      - <a href="actionlistdefinition.md">ActionListDefinition</a></i>
<a href="#filtering" title="Filtering">Filtering</a>: <i>
      - <a href="filteringdefinition.md">FilteringDefinition</a></i>
<a href="#sanfiltering" title="SanFiltering">SanFiltering</a>: <i>
      - <a href="sanfilteringdefinition.md">SanFilteringDefinition</a></i>
<a href="#sourcelist" title="SourceList">SourceList</a>: <i>
      - <a href="sourcelistdefinition.md">SourceListDefinition</a></i>
</pre>

## Properties

#### AcosEventLog

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogging

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoClientConnReuse

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireWebCategory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionList

_Required_: No

_Type_: List of <a href="actionlistdefinition.md">ActionListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filtering

_Required_: No

_Type_: List of <a href="filteringdefinition.md">FilteringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanFiltering

_Required_: No

_Type_: List of <a href="sanfilteringdefinition.md">SanFilteringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceList

_Required_: No

_Type_: List of <a href="sourcelistdefinition.md">SourceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

