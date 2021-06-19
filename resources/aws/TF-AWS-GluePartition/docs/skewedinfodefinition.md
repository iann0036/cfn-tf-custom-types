# TF::AWS::GluePartition SkewedInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#skewedcolumnnames" title="SkewedColumnNames">SkewedColumnNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#skewedcolumnvaluelocationmaps" title="SkewedColumnValueLocationMaps">SkewedColumnValueLocationMaps</a>" : <i>[ <a href="skewedcolumnvaluelocationmapsdefinition.md">SkewedColumnValueLocationMapsDefinition</a>, ... ]</i>,
    "<a href="#skewedcolumnvalues" title="SkewedColumnValues">SkewedColumnValues</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#skewedcolumnnames" title="SkewedColumnNames">SkewedColumnNames</a>: <i>
      - String</i>
<a href="#skewedcolumnvaluelocationmaps" title="SkewedColumnValueLocationMaps">SkewedColumnValueLocationMaps</a>: <i>
      - <a href="skewedcolumnvaluelocationmapsdefinition.md">SkewedColumnValueLocationMapsDefinition</a></i>
<a href="#skewedcolumnvalues" title="SkewedColumnValues">SkewedColumnValues</a>: <i>
      - String</i>
</pre>

## Properties

#### SkewedColumnNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedColumnValueLocationMaps

_Required_: No

_Type_: List of <a href="skewedcolumnvaluelocationmapsdefinition.md">SkewedColumnValueLocationMapsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedColumnValues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

