# TF::AWS::MwaaEnvironment LoggingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dagprocessinglogs" title="DagProcessingLogs">DagProcessingLogs</a>" : <i>[ <a href="dagprocessinglogsdefinition.md">DagProcessingLogsDefinition</a>, ... ]</i>,
    "<a href="#schedulerlogs" title="SchedulerLogs">SchedulerLogs</a>" : <i>[ <a href="schedulerlogsdefinition.md">SchedulerLogsDefinition</a>, ... ]</i>,
    "<a href="#tasklogs" title="TaskLogs">TaskLogs</a>" : <i>[ <a href="tasklogsdefinition.md">TaskLogsDefinition</a>, ... ]</i>,
    "<a href="#webserverlogs" title="WebserverLogs">WebserverLogs</a>" : <i>[ <a href="webserverlogsdefinition.md">WebserverLogsDefinition</a>, ... ]</i>,
    "<a href="#workerlogs" title="WorkerLogs">WorkerLogs</a>" : <i>[ <a href="workerlogsdefinition.md">WorkerLogsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dagprocessinglogs" title="DagProcessingLogs">DagProcessingLogs</a>: <i>
      - <a href="dagprocessinglogsdefinition.md">DagProcessingLogsDefinition</a></i>
<a href="#schedulerlogs" title="SchedulerLogs">SchedulerLogs</a>: <i>
      - <a href="schedulerlogsdefinition.md">SchedulerLogsDefinition</a></i>
<a href="#tasklogs" title="TaskLogs">TaskLogs</a>: <i>
      - <a href="tasklogsdefinition.md">TaskLogsDefinition</a></i>
<a href="#webserverlogs" title="WebserverLogs">WebserverLogs</a>: <i>
      - <a href="webserverlogsdefinition.md">WebserverLogsDefinition</a></i>
<a href="#workerlogs" title="WorkerLogs">WorkerLogs</a>: <i>
      - <a href="workerlogsdefinition.md">WorkerLogsDefinition</a></i>
</pre>

## Properties

#### DagProcessingLogs

_Required_: No

_Type_: List of <a href="dagprocessinglogsdefinition.md">DagProcessingLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulerLogs

_Required_: No

_Type_: List of <a href="schedulerlogsdefinition.md">SchedulerLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskLogs

_Required_: No

_Type_: List of <a href="tasklogsdefinition.md">TaskLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebserverLogs

_Required_: No

_Type_: List of <a href="webserverlogsdefinition.md">WebserverLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerLogs

_Required_: No

_Type_: List of <a href="workerlogsdefinition.md">WorkerLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

