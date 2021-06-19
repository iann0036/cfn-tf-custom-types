# TF::GoogleBeta::GoogleDataprocJob

CloudFormation equivalent of google_dataproc_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleDataprocJob",
    "Properties" : {
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>" : <i>[ <a href="hadoopconfigdefinition.md">HadoopConfigDefinition</a>, ... ]</i>,
        "<a href="#hiveconfig" title="HiveConfig">HiveConfig</a>" : <i>[ <a href="hiveconfigdefinition.md">HiveConfigDefinition</a>, ... ]</i>,
        "<a href="#pigconfig" title="PigConfig">PigConfig</a>" : <i>[ <a href="pigconfigdefinition.md">PigConfigDefinition</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placementdefinition.md">PlacementDefinition</a>, ... ]</i>,
        "<a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>" : <i>[ <a href="pysparkconfigdefinition.md">PysparkConfigDefinition</a>, ... ]</i>,
        "<a href="#reference" title="Reference">Reference</a>" : <i>[ <a href="referencedefinition.md">ReferenceDefinition</a>, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="schedulingdefinition.md">SchedulingDefinition</a>, ... ]</i>,
        "<a href="#sparkconfig" title="SparkConfig">SparkConfig</a>" : <i>[ <a href="sparkconfigdefinition.md">SparkConfigDefinition</a>, ... ]</i>,
        "<a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>" : <i>[ <a href="sparksqlconfigdefinition.md">SparksqlConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleDataprocJob
Properties:
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>: <i>
      - <a href="hadoopconfigdefinition.md">HadoopConfigDefinition</a></i>
    <a href="#hiveconfig" title="HiveConfig">HiveConfig</a>: <i>
      - <a href="hiveconfigdefinition.md">HiveConfigDefinition</a></i>
    <a href="#pigconfig" title="PigConfig">PigConfig</a>: <i>
      - <a href="pigconfigdefinition.md">PigConfigDefinition</a></i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placementdefinition.md">PlacementDefinition</a></i>
    <a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>: <i>
      - <a href="pysparkconfigdefinition.md">PysparkConfigDefinition</a></i>
    <a href="#reference" title="Reference">Reference</a>: <i>
      - <a href="referencedefinition.md">ReferenceDefinition</a></i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="schedulingdefinition.md">SchedulingDefinition</a></i>
    <a href="#sparkconfig" title="SparkConfig">SparkConfig</a>: <i>
      - <a href="sparkconfigdefinition.md">SparkConfigDefinition</a></i>
    <a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>: <i>
      - <a href="sparksqlconfigdefinition.md">SparksqlConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ForceDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HadoopConfig

_Required_: No

_Type_: List of <a href="hadoopconfigdefinition.md">HadoopConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveConfig

_Required_: No

_Type_: List of <a href="hiveconfigdefinition.md">HiveConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PigConfig

_Required_: No

_Type_: List of <a href="pigconfigdefinition.md">PigConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placementdefinition.md">PlacementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PysparkConfig

_Required_: No

_Type_: List of <a href="pysparkconfigdefinition.md">PysparkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reference

_Required_: No

_Type_: List of <a href="referencedefinition.md">ReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of <a href="schedulingdefinition.md">SchedulingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkConfig

_Required_: No

_Type_: List of <a href="sparkconfigdefinition.md">SparkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparksqlConfig

_Required_: No

_Type_: List of <a href="sparksqlconfigdefinition.md">SparksqlConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DriverControlsFilesUri

Returns the <code>DriverControlsFilesUri</code> value.

#### DriverOutputResourceUri

Returns the <code>DriverOutputResourceUri</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

