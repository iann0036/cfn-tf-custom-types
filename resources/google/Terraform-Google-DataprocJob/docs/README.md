# Terraform::Google::DataprocJob

CloudFormation equivalent of google_dataproc_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DataprocJob",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#drivercontrolsfilesuri" title="DriverControlsFilesUri">DriverControlsFilesUri</a>" : <i>String</i>,
        "<a href="#driveroutputresourceuri" title="DriverOutputResourceUri">DriverOutputResourceUri</a>" : <i>String</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>[ &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;, ... ]</i>,
        "<a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>" : <i>[ &lt;a href=&#34;hadoopconfig.md&#34;&gt;HadoopConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#hiveconfig" title="HiveConfig">HiveConfig</a>" : <i>[ &lt;a href=&#34;hiveconfig.md&#34;&gt;HiveConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#pigconfig" title="PigConfig">PigConfig</a>" : <i>[ &lt;a href=&#34;pigconfig.md&#34;&gt;PigConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;, ... ]</i>,
        "<a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>" : <i>[ &lt;a href=&#34;pysparkconfig.md&#34;&gt;PysparkConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#reference" title="Reference">Reference</a>" : <i>[ &lt;a href=&#34;reference.md&#34;&gt;Reference&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ &lt;a href=&#34;scheduling.md&#34;&gt;Scheduling&lt;/a&gt;, ... ]</i>,
        "<a href="#sparkconfig" title="SparkConfig">SparkConfig</a>" : <i>[ &lt;a href=&#34;sparkconfig.md&#34;&gt;SparkConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>" : <i>[ &lt;a href=&#34;sparksqlconfig.md&#34;&gt;SparksqlConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DataprocJob
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#drivercontrolsfilesuri" title="DriverControlsFilesUri">DriverControlsFilesUri</a>: <i>String</i>
    <a href="#driveroutputresourceuri" title="DriverOutputResourceUri">DriverOutputResourceUri</a>: <i>String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>
      - &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;</i>
    <a href="#hadoopconfig" title="HadoopConfig">HadoopConfig</a>: <i>
      - &lt;a href=&#34;hadoopconfig.md&#34;&gt;HadoopConfig&lt;/a&gt;</i>
    <a href="#hiveconfig" title="HiveConfig">HiveConfig</a>: <i>
      - &lt;a href=&#34;hiveconfig.md&#34;&gt;HiveConfig&lt;/a&gt;</i>
    <a href="#pigconfig" title="PigConfig">PigConfig</a>: <i>
      - &lt;a href=&#34;pigconfig.md&#34;&gt;PigConfig&lt;/a&gt;</i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;</i>
    <a href="#pysparkconfig" title="PysparkConfig">PysparkConfig</a>: <i>
      - &lt;a href=&#34;pysparkconfig.md&#34;&gt;PysparkConfig&lt;/a&gt;</i>
    <a href="#reference" title="Reference">Reference</a>: <i>
      - &lt;a href=&#34;reference.md&#34;&gt;Reference&lt;/a&gt;</i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - &lt;a href=&#34;scheduling.md&#34;&gt;Scheduling&lt;/a&gt;</i>
    <a href="#sparkconfig" title="SparkConfig">SparkConfig</a>: <i>
      - &lt;a href=&#34;sparkconfig.md&#34;&gt;SparkConfig&lt;/a&gt;</i>
    <a href="#sparksqlconfig" title="SparksqlConfig">SparksqlConfig</a>: <i>
      - &lt;a href=&#34;sparksqlconfig.md&#34;&gt;SparksqlConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverControlsFilesUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverOutputResourceUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: List of &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HadoopConfig

_Required_: No

_Type_: List of &lt;a href=&#34;hadoopconfig.md&#34;&gt;HadoopConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveConfig

_Required_: No

_Type_: List of &lt;a href=&#34;hiveconfig.md&#34;&gt;HiveConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PigConfig

_Required_: No

_Type_: List of &lt;a href=&#34;pigconfig.md&#34;&gt;PigConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PysparkConfig

_Required_: No

_Type_: List of &lt;a href=&#34;pysparkconfig.md&#34;&gt;PysparkConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reference

_Required_: No

_Type_: List of &lt;a href=&#34;reference.md&#34;&gt;Reference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of &lt;a href=&#34;scheduling.md&#34;&gt;Scheduling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkConfig

_Required_: No

_Type_: List of &lt;a href=&#34;sparkconfig.md&#34;&gt;SparkConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparksqlConfig

_Required_: No

_Type_: List of &lt;a href=&#34;sparksqlconfig.md&#34;&gt;SparksqlConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;

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

Returns the &lt;code&gt;DriverControlsFilesUri&lt;/code&gt; value.

#### DriverOutputResourceUri

Returns the &lt;code&gt;DriverOutputResourceUri&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

