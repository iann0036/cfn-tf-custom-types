# TF::VRA::Deployment ResourcesDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#createdat" title="CreatedAt">CreatedAt</a>" : <i>String</i>,
    "<a href="#dependson" title="DependsOn">DependsOn</a>" : <i>[ String, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#expense" title="Expense">Expense</a>" : <i>[ <a href="expensedefinition.md">ExpenseDefinition</a>, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#propertiesjson" title="PropertiesJson">PropertiesJson</a>" : <i>String</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#syncstatus" title="SyncStatus">SyncStatus</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#createdat" title="CreatedAt">CreatedAt</a>: <i>String</i>
<a href="#dependson" title="DependsOn">DependsOn</a>: <i>
      - String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#expense" title="Expense">Expense</a>: <i>
      - <a href="expensedefinition.md">ExpenseDefinition</a></i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#propertiesjson" title="PropertiesJson">PropertiesJson</a>: <i>String</i>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#syncstatus" title="SyncStatus">SyncStatus</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CreatedAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DependsOn

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expense

_Required_: No

_Type_: List of <a href="expensedefinition.md">ExpenseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertiesJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

