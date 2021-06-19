# TF::AWS::MwaaEnvironment

Creates a MWAA Environment resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::MwaaEnvironment",
    "Properties" : {
        "<a href="#airflowconfigurationoptions" title="AirflowConfigurationOptions">AirflowConfigurationOptions</a>" : <i>[ <a href="airflowconfigurationoptionsdefinition.md">AirflowConfigurationOptionsDefinition</a>, ... ]</i>,
        "<a href="#airflowversion" title="AirflowVersion">AirflowVersion</a>" : <i>String</i>,
        "<a href="#dags3path" title="DagS3Path">DagS3Path</a>" : <i>String</i>,
        "<a href="#environmentclass" title="EnvironmentClass">EnvironmentClass</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>,
        "<a href="#maxworkers" title="MaxWorkers">MaxWorkers</a>" : <i>Double</i>,
        "<a href="#minworkers" title="MinWorkers">MinWorkers</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pluginss3objectversion" title="PluginsS3ObjectVersion">PluginsS3ObjectVersion</a>" : <i>String</i>,
        "<a href="#pluginss3path" title="PluginsS3Path">PluginsS3Path</a>" : <i>String</i>,
        "<a href="#requirementss3objectversion" title="RequirementsS3ObjectVersion">RequirementsS3ObjectVersion</a>" : <i>String</i>,
        "<a href="#requirementss3path" title="RequirementsS3Path">RequirementsS3Path</a>" : <i>String</i>,
        "<a href="#sourcebucketarn" title="SourceBucketArn">SourceBucketArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#webserveraccessmode" title="WebserverAccessMode">WebserverAccessMode</a>" : <i>String</i>,
        "<a href="#weeklymaintenancewindowstart" title="WeeklyMaintenanceWindowStart">WeeklyMaintenanceWindowStart</a>" : <i>String</i>,
        "<a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>" : <i>[ <a href="loggingconfigurationdefinition.md">LoggingConfigurationDefinition</a>, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::MwaaEnvironment
Properties:
    <a href="#airflowconfigurationoptions" title="AirflowConfigurationOptions">AirflowConfigurationOptions</a>: <i>
      - <a href="airflowconfigurationoptionsdefinition.md">AirflowConfigurationOptionsDefinition</a></i>
    <a href="#airflowversion" title="AirflowVersion">AirflowVersion</a>: <i>String</i>
    <a href="#dags3path" title="DagS3Path">DagS3Path</a>: <i>String</i>
    <a href="#environmentclass" title="EnvironmentClass">EnvironmentClass</a>: <i>String</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
    <a href="#maxworkers" title="MaxWorkers">MaxWorkers</a>: <i>Double</i>
    <a href="#minworkers" title="MinWorkers">MinWorkers</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pluginss3objectversion" title="PluginsS3ObjectVersion">PluginsS3ObjectVersion</a>: <i>String</i>
    <a href="#pluginss3path" title="PluginsS3Path">PluginsS3Path</a>: <i>String</i>
    <a href="#requirementss3objectversion" title="RequirementsS3ObjectVersion">RequirementsS3ObjectVersion</a>: <i>String</i>
    <a href="#requirementss3path" title="RequirementsS3Path">RequirementsS3Path</a>: <i>String</i>
    <a href="#sourcebucketarn" title="SourceBucketArn">SourceBucketArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#webserveraccessmode" title="WebserverAccessMode">WebserverAccessMode</a>: <i>String</i>
    <a href="#weeklymaintenancewindowstart" title="WeeklyMaintenanceWindowStart">WeeklyMaintenanceWindowStart</a>: <i>String</i>
    <a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>: <i>
      - <a href="loggingconfigurationdefinition.md">LoggingConfigurationDefinition</a></i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a></i>
</pre>

## Properties

#### AirflowConfigurationOptions

The `airflow_configuration_options` parameter specifies airflow override options. Check the [Official documentation](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html#configuring-env-variables-reference) for all possible configuration options.

_Required_: No

_Type_: List of <a href="airflowconfigurationoptionsdefinition.md">AirflowConfigurationOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AirflowVersion

Airflow version of your environment, will be set by default to the latest version that MWAA supports.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DagS3Path

The relative path to the DAG folder on your Amazon S3 storage bucket. For example, dags. For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentClass

Environment class for the cluster. Possible options are `mw1.small`, `mw1.medium`, `mw1.large`. Will be set by default to `mw1.small`. Please check the [AWS Pricing](https://aws.amazon.com/de/managed-workflows-for-apache-airflow/pricing/) for more information about the environment classes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

The Amazon Resource Name (ARN) of the task execution role that the Amazon MWAA and its environment can assume. Check the [official AWS documentation](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html) for the detailed role specification.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

The Amazon Resource Name (ARN) of your KMS key that you want to use for encryption. Will be set to the ARN of the managed KMS key `aws/airflow` by default. Please check the [Official Documentation](https://docs.aws.amazon.com/mwaa/latest/userguide/custom-keys-certs.html) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWorkers

The maximum number of workers that can be automatically scaled up. Value need to be between `1` and `25`. Will be `10` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinWorkers

The minimum number of workers that you want to run in your environment. Will be `1` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Apache Airflow Environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginsS3ObjectVersion

The plugins.zip file version you want to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginsS3Path

The relative path to the plugins.zip file on your Amazon S3 storage bucket. For example, plugins.zip. If a relative path is provided in the request, then plugins_s3_object_version is required. For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirementsS3ObjectVersion

The requirements.txt file version you want to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirementsS3Path

The relative path to the requirements.txt file on your Amazon S3 storage bucket. For example, requirements.txt. If a relative path is provided in the request, then requirements_s3_object_version is required. For more information, see [Importing DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceBucketArn

The Amazon Resource Name (ARN) of your Amazon S3 storage bucket. For example, arn:aws:s3:::airflow-mybucketname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of resource tags to associate with the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebserverAccessMode

Specifies whether the webserver should be accessible over the internet or via your specified VPC. Possible options: `PRIVATE_ONLY` (default) and `PUBLIC_ONLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyMaintenanceWindowStart

Specifies the start date for the weekly maintenance window.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfiguration

_Required_: No

_Type_: List of <a href="loggingconfigurationdefinition.md">LoggingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdated

Returns the <code>LastUpdated</code> value.

#### ServiceRoleArn

Returns the <code>ServiceRoleArn</code> value.

#### Status

Returns the <code>Status</code> value.

#### WebserverUrl

Returns the <code>WebserverUrl</code> value.

