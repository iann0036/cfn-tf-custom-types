# Terraform::Google::DataprocJob

Manages a job resource within a Dataproc cluster within GCE. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).

!> **Note:** This resource does not support 'update' and changing any attributes will cause the resource to be recreated.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DataprocJob",
    "Properties" : {
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>" : <i>[ <a href="hadoopconfig.md">HadoopConfig</a>, ... ]</i>,
        "<a href="#hiveconfig" title="HiveConfig">HiveConfig</a>" : <i>[ <a href="hiveconfig.md">HiveConfig</a>, ... ]</i>,
        "<a href="#pigconfig" title="PigConfig">PigConfig</a>" : <i>[ <a href="pigconfig.md">PigConfig</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placement.md">Placement</a>, ... ]</i>,
        "<a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>" : <i>[ <a href="pysparkconfig.md">PysparkConfig</a>, ... ]</i>,
        "<a href="#reference" title="Reference">Reference</a>" : <i>[ <a href="reference.md">Reference</a>, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="scheduling.md">Scheduling</a>, ... ]</i>,
        "<a href="#sparkconfig" title="SparkConfig">SparkConfig</a>" : <i>[ <a href="sparkconfig.md">SparkConfig</a>, ... ]</i>,
        "<a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>" : <i>[ <a href="sparksqlconfig.md">SparksqlConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ <a href="loggingconfig.md">LoggingConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DataprocJob
Properties:
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>: <i>
      - <a href="hadoopconfig.md">HadoopConfig</a></i>
    <a href="#hiveconfig" title="HiveConfig">HiveConfig</a>: <i>
      - <a href="hiveconfig.md">HiveConfig</a></i>
    <a href="#pigconfig" title="PigConfig">PigConfig</a>: <i>
      - <a href="pigconfig.md">PigConfig</a></i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placement.md">Placement</a></i>
    <a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>: <i>
      - <a href="pysparkconfig.md">PysparkConfig</a></i>
    <a href="#reference" title="Reference">Reference</a>: <i>
      - <a href="reference.md">Reference</a></i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="scheduling.md">Scheduling</a></i>
    <a href="#sparkconfig" title="SparkConfig">SparkConfig</a>: <i>
      - <a href="sparkconfig.md">SparkConfig</a></i>
    <a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>: <i>
      - <a href="sparksqlconfig.md">SparksqlConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - <a href="loggingconfig.md">LoggingConfig</a></i>
</pre>

## Properties

#### ForceDelete

By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

The list of labels (key/value pairs) to add to the job.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HadoopConfig

_Required_: No

_Type_: List of <a href="hadoopconfig.md">HadoopConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveConfig

_Required_: No

_Type_: List of <a href="hiveconfig.md">HiveConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PigConfig

_Required_: No

_Type_: List of <a href="pigconfig.md">PigConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placement.md">Placement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PysparkConfig

_Required_: No

_Type_: List of <a href="pysparkconfig.md">PysparkConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reference

_Required_: No

_Type_: List of <a href="reference.md">Reference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of <a href="scheduling.md">Scheduling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkConfig

_Required_: No

_Type_: List of <a href="sparkconfig.md">SparkConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparksqlConfig

_Required_: No

_Type_: List of <a href="sparksqlconfig.md">SparksqlConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of <a href="loggingconfig.md">LoggingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

