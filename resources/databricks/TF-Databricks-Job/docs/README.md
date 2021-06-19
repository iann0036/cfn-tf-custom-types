# TF::Databricks::Job

CloudFormation equivalent of databricks_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::Job",
    "Properties" : {
        "<a href="#existingclusterid" title="ExistingClusterId">ExistingClusterId</a>" : <i>String</i>,
        "<a href="#maxconcurrentruns" title="MaxConcurrentRuns">MaxConcurrentRuns</a>" : <i>Double</i>,
        "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
        "<a href="#minretryintervalmillis" title="MinRetryIntervalMillis">MinRetryIntervalMillis</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#retryontimeout" title="RetryOnTimeout">RetryOnTimeout</a>" : <i>Boolean</i>,
        "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
        "<a href="#emailnotifications" title="EmailNotifications">EmailNotifications</a>" : <i>[ <a href="emailnotificationsdefinition.md">EmailNotificationsDefinition</a>, ... ]</i>,
        "<a href="#library" title="Library">Library</a>" : <i>[ <a href="librarydefinition.md">LibraryDefinition</a>, ... ]</i>,
        "<a href="#newcluster" title="NewCluster">NewCluster</a>" : <i>[ <a href="newclusterdefinition.md">NewClusterDefinition</a>, ... ]</i>,
        "<a href="#notebooktask" title="NotebookTask">NotebookTask</a>" : <i>[ <a href="notebooktaskdefinition.md">NotebookTaskDefinition</a>, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="scheduledefinition.md">ScheduleDefinition</a>, ... ]</i>,
        "<a href="#sparkjartask" title="SparkJarTask">SparkJarTask</a>" : <i>[ <a href="sparkjartaskdefinition.md">SparkJarTaskDefinition</a>, ... ]</i>,
        "<a href="#sparkpythontask" title="SparkPythonTask">SparkPythonTask</a>" : <i>[ <a href="sparkpythontaskdefinition.md">SparkPythonTaskDefinition</a>, ... ]</i>,
        "<a href="#sparksubmittask" title="SparkSubmitTask">SparkSubmitTask</a>" : <i>[ <a href="sparksubmittaskdefinition.md">SparkSubmitTaskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::Job
Properties:
    <a href="#existingclusterid" title="ExistingClusterId">ExistingClusterId</a>: <i>String</i>
    <a href="#maxconcurrentruns" title="MaxConcurrentRuns">MaxConcurrentRuns</a>: <i>Double</i>
    <a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
    <a href="#minretryintervalmillis" title="MinRetryIntervalMillis">MinRetryIntervalMillis</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#retryontimeout" title="RetryOnTimeout">RetryOnTimeout</a>: <i>Boolean</i>
    <a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
    <a href="#emailnotifications" title="EmailNotifications">EmailNotifications</a>: <i>
      - <a href="emailnotificationsdefinition.md">EmailNotificationsDefinition</a></i>
    <a href="#library" title="Library">Library</a>: <i>
      - <a href="librarydefinition.md">LibraryDefinition</a></i>
    <a href="#newcluster" title="NewCluster">NewCluster</a>: <i>
      - <a href="newclusterdefinition.md">NewClusterDefinition</a></i>
    <a href="#notebooktask" title="NotebookTask">NotebookTask</a>: <i>
      - <a href="notebooktaskdefinition.md">NotebookTaskDefinition</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="scheduledefinition.md">ScheduleDefinition</a></i>
    <a href="#sparkjartask" title="SparkJarTask">SparkJarTask</a>: <i>
      - <a href="sparkjartaskdefinition.md">SparkJarTaskDefinition</a></i>
    <a href="#sparkpythontask" title="SparkPythonTask">SparkPythonTask</a>: <i>
      - <a href="sparkpythontaskdefinition.md">SparkPythonTaskDefinition</a></i>
    <a href="#sparksubmittask" title="SparkSubmitTask">SparkSubmitTask</a>: <i>
      - <a href="sparksubmittaskdefinition.md">SparkSubmitTaskDefinition</a></i>
</pre>

## Properties

#### ExistingClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentRuns

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRetryIntervalMillis

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOnTimeout

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailNotifications

_Required_: No

_Type_: List of <a href="emailnotificationsdefinition.md">EmailNotificationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Library

_Required_: No

_Type_: List of <a href="librarydefinition.md">LibraryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewCluster

_Required_: No

_Type_: List of <a href="newclusterdefinition.md">NewClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotebookTask

_Required_: No

_Type_: List of <a href="notebooktaskdefinition.md">NotebookTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="scheduledefinition.md">ScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkJarTask

_Required_: No

_Type_: List of <a href="sparkjartaskdefinition.md">SparkJarTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkPythonTask

_Required_: No

_Type_: List of <a href="sparkpythontaskdefinition.md">SparkPythonTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkSubmitTask

_Required_: No

_Type_: List of <a href="sparksubmittaskdefinition.md">SparkSubmitTaskDefinition</a>

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

#### Url

Returns the <code>Url</code> value.

