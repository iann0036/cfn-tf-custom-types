# TF::GoogleBeta::GoogleDataCatalogEntry BigqueryTableSpecDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tablesourcetype" title="TableSourceType">TableSourceType</a>" : <i>String</i>,
    "<a href="#tablespec" title="TableSpec">TableSpec</a>" : <i>[ <a href="bigquerytablespecdefinition.md">BigqueryTableSpecDefinition</a>, ... ]</i>,
    "<a href="#viewspec" title="ViewSpec">ViewSpec</a>" : <i>[ <a href="bigquerytablespecdefinition2.md">BigqueryTableSpecDefinition2</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tablesourcetype" title="TableSourceType">TableSourceType</a>: <i>String</i>
<a href="#tablespec" title="TableSpec">TableSpec</a>: <i>
      - <a href="bigquerytablespecdefinition.md">BigqueryTableSpecDefinition</a></i>
<a href="#viewspec" title="ViewSpec">ViewSpec</a>: <i>
      - <a href="bigquerytablespecdefinition2.md">BigqueryTableSpecDefinition2</a></i>
</pre>

## Properties

#### TableSourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableSpec

_Required_: No

_Type_: List of <a href="bigquerytablespecdefinition.md">BigqueryTableSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewSpec

_Required_: No

_Type_: List of <a href="bigquerytablespecdefinition2.md">BigqueryTableSpecDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

