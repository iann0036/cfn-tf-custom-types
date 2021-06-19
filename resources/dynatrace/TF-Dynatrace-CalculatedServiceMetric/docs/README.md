# TF::Dynatrace::CalculatedServiceMetric

CloudFormation equivalent of dynatrace_calculated_service_metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::CalculatedServiceMetric",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
        "<a href="#managementzones" title="ManagementZones">ManagementZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#metrickey" title="MetricKey">MetricKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
        "<a href="#unitdisplayname" title="UnitDisplayName">UnitDisplayName</a>" : <i>String</i>,
        "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
        "<a href="#dimensiondefinition" title="DimensionDefinition">DimensionDefinition</a>" : <i>[ <a href="dimensiondefinitiondefinition.md">DimensionDefinitionDefinition</a>, ... ]</i>,
        "<a href="#metricdefinition" title="MetricDefinition">MetricDefinition</a>" : <i>[ <a href="metricdefinitiondefinition.md">MetricDefinitionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::CalculatedServiceMetric
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
    <a href="#managementzones" title="ManagementZones">ManagementZones</a>: <i>
      - String</i>
    <a href="#metrickey" title="MetricKey">MetricKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#unit" title="Unit">Unit</a>: <i>String</i>
    <a href="#unitdisplayname" title="UnitDisplayName">UnitDisplayName</a>: <i>String</i>
    <a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
    <a href="#dimensiondefinition" title="DimensionDefinition">DimensionDefinition</a>: <i>
      - <a href="dimensiondefinitiondefinition.md">DimensionDefinitionDefinition</a></i>
    <a href="#metricdefinition" title="MetricDefinition">MetricDefinition</a>: <i>
      - <a href="metricdefinitiondefinition.md">MetricDefinitionDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitDisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DimensionDefinition

_Required_: No

_Type_: List of <a href="dimensiondefinitiondefinition.md">DimensionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDefinition

_Required_: No

_Type_: List of <a href="metricdefinitiondefinition.md">MetricDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

