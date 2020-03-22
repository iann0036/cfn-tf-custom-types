# Terraform::Rundeck::Job

The job resource allows Rundeck jobs to be managed by Terraform. In Rundeck a job is a particular
named set of steps that can be executed against one or more of the nodes configured for its
associated project.

Each job belongs to a project. A project can be created with the `rundeck_project` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::Job",
    "Properties" : {
        "<a href="#allowconcurrentexecutions" title="AllowConcurrentExecutions">AllowConcurrentExecutions</a>" : <i>Boolean</i>,
        "<a href="#commandorderingstrategy" title="CommandOrderingStrategy">CommandOrderingStrategy</a>" : <i>String</i>,
        "<a href="#continueonerror" title="ContinueOnError">ContinueOnError</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#executionenabled" title="ExecutionEnabled">ExecutionEnabled</a>" : <i>Boolean</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
        "<a href="#maxthreadcount" title="MaxThreadCount">MaxThreadCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodefilterexcludeprecedence" title="NodeFilterExcludePrecedence">NodeFilterExcludePrecedence</a>" : <i>Boolean</i>,
        "<a href="#nodefilterquery" title="NodeFilterQuery">NodeFilterQuery</a>" : <i>String</i>,
        "<a href="#preserveoptionsorder" title="PreserveOptionsOrder">PreserveOptionsOrder</a>" : <i>Boolean</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#rankattribute" title="RankAttribute">RankAttribute</a>" : <i>String</i>,
        "<a href="#rankorder" title="RankOrder">RankOrder</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#scheduleenabled" title="ScheduleEnabled">ScheduleEnabled</a>" : <i>Boolean</i>,
        "<a href="#successonemptynodefilter" title="SuccessOnEmptyNodeFilter">SuccessOnEmptyNodeFilter</a>" : <i>Boolean</i>,
        "<a href="#command" title="Command">Command</a>" : <i>[ <a href="command.md">Command</a>, ... ]</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ <a href="notification.md">Notification</a>, ... ]</i>,
        "<a href="#option" title="Option">Option</a>" : <i>[ <a href="option.md">Option</a>, ... ]</i>,
        "<a href="#job" title="Job">Job</a>" : <i>[ <a href="job.md">Job</a>, ... ]</i>,
        "<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>" : <i>[ <a href="nodestepplugin.md">NodeStepPlugin</a>, ... ]</i>,
        "<a href="#stepplugin" title="StepPlugin">StepPlugin</a>" : <i>[ <a href="stepplugin.md">StepPlugin</a>, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="email.md">Email</a>, ... ]</i>,
        "<a href="#plugin" title="Plugin">Plugin</a>" : <i>[ <a href="plugin.md">Plugin</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::Job
Properties:
    <a href="#allowconcurrentexecutions" title="AllowConcurrentExecutions">AllowConcurrentExecutions</a>: <i>Boolean</i>
    <a href="#commandorderingstrategy" title="CommandOrderingStrategy">CommandOrderingStrategy</a>: <i>String</i>
    <a href="#continueonerror" title="ContinueOnError">ContinueOnError</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#executionenabled" title="ExecutionEnabled">ExecutionEnabled</a>: <i>Boolean</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
    <a href="#maxthreadcount" title="MaxThreadCount">MaxThreadCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodefilterexcludeprecedence" title="NodeFilterExcludePrecedence">NodeFilterExcludePrecedence</a>: <i>Boolean</i>
    <a href="#nodefilterquery" title="NodeFilterQuery">NodeFilterQuery</a>: <i>String</i>
    <a href="#preserveoptionsorder" title="PreserveOptionsOrder">PreserveOptionsOrder</a>: <i>Boolean</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#rankattribute" title="RankAttribute">RankAttribute</a>: <i>String</i>
    <a href="#rankorder" title="RankOrder">RankOrder</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#scheduleenabled" title="ScheduleEnabled">ScheduleEnabled</a>: <i>Boolean</i>
    <a href="#successonemptynodefilter" title="SuccessOnEmptyNodeFilter">SuccessOnEmptyNodeFilter</a>: <i>Boolean</i>
    <a href="#command" title="Command">Command</a>: <i>
      - <a href="command.md">Command</a></i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - <a href="notification.md">Notification</a></i>
    <a href="#option" title="Option">Option</a>: <i>
      - <a href="option.md">Option</a></i>
    <a href="#job" title="Job">Job</a>: <i>
      - <a href="job.md">Job</a></i>
    <a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>: <i>
      - <a href="nodestepplugin.md">NodeStepPlugin</a></i>
    <a href="#stepplugin" title="StepPlugin">StepPlugin</a>: <i>
      - <a href="stepplugin.md">StepPlugin</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="email.md">Email</a></i>
    <a href="#plugin" title="Plugin">Plugin</a>: <i>
      - <a href="plugin.md">Plugin</a></i>
</pre>

## Properties

#### AllowConcurrentExecutions

Boolean defining whether two or more executions of
this job can run concurrently. The default is `false`, meaning that jobs will only run
sequentially.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommandOrderingStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueOnError

Boolean defining whether Rundeck will continue to run
subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
will stop and the execution will be considered to have failed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A longer description of the job, describing the job in the Rundeck UI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionEnabled

If you want job execution to be enabled or disabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

The name of a group within the project in which to place the job.
Setting this creates collapsable subcategories within the Rundeck UI's project job index.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

The log level that Rundeck should use for this job. Defaults to "INFO".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThreadCount

The maximum number of threads to use to execute this job, which
controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
the nodes will be visited sequentially.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the job, used to describe the job in the Rundeck UI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeFilterExcludePrecedence

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeFilterQuery

A query string using
[Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
that defines which subset of the project's nodes will be used to execute this job.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveOptionsOrder

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

The name of the project that this job should belong to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RankAttribute

The name of the attribute that will be used to decide in which
order the nodes will be visited while executing the job across multiple nodes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RankOrder

Keyword deciding which direction the nodes are sorted in terms of
the chosen `rank_attribute`. May be either "ascending" (the default) or "descending".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

The jobs schedule in Unix crontab format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleEnabled

Sets the job schedule to be enabled or disabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessOnEmptyNodeFilter

Boolean determining if an empty node filter yields
a successful result.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of <a href="command.md">Command</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of <a href="notification.md">Notification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of <a href="option.md">Option</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Job

_Required_: No

_Type_: List of <a href="job.md">Job</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeStepPlugin

_Required_: No

_Type_: List of <a href="nodestepplugin.md">NodeStepPlugin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepPlugin

_Required_: No

_Type_: List of <a href="stepplugin.md">StepPlugin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="email.md">Email</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plugin

_Required_: No

_Type_: List of <a href="plugin.md">Plugin</a>

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

