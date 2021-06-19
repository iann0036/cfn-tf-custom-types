# TF::GoogleBeta::GoogleBigqueryDataset AccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    "<a href="#groupbyemail" title="GroupByEmail">GroupByEmail</a>" : <i>String</i>,
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#specialgroup" title="SpecialGroup">SpecialGroup</a>" : <i>String</i>,
    "<a href="#userbyemail" title="UserByEmail">UserByEmail</a>" : <i>String</i>,
    "<a href="#view" title="View">View</a>" : <i>[ <a href="viewdefinition.md">ViewDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domain" title="Domain">Domain</a>: <i>String</i>
<a href="#groupbyemail" title="GroupByEmail">GroupByEmail</a>: <i>String</i>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#specialgroup" title="SpecialGroup">SpecialGroup</a>: <i>String</i>
<a href="#userbyemail" title="UserByEmail">UserByEmail</a>: <i>String</i>
<a href="#view" title="View">View</a>: <i>
      - <a href="viewdefinition.md">ViewDefinition</a></i>
</pre>

## Properties

#### Domain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupByEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecialGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserByEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of <a href="viewdefinition.md">ViewDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

