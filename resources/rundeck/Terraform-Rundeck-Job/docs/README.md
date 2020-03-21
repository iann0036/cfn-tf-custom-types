# Terraform::Rundeck::Job

CloudFormation equivalent of rundeck_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::Job",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
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
        "<a href="#command" title="Command">Command</a>" : <i>[ &lt;a href=&#34;command.md&#34;&gt;Command&lt;/a&gt;, ... ]</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;, ... ]</i>,
        "<a href="#option" title="Option">Option</a>" : <i>[ &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;, ... ]</i>,
        "<a href="#job" title="Job">Job</a>" : <i>[ &lt;a href=&#34;job.md&#34;&gt;Job&lt;/a&gt;, ... ]</i>,
        "<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>" : <i>[ &lt;a href=&#34;nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;, ... ]</i>,
        "<a href="#stepplugin" title="StepPlugin">StepPlugin</a>" : <i>[ &lt;a href=&#34;stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;, ... ]</i>,
        "<a href="#plugin" title="Plugin">Plugin</a>" : <i>[ &lt;a href=&#34;plugin.md&#34;&gt;Plugin&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::Job
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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
      - &lt;a href=&#34;command.md&#34;&gt;Command&lt;/a&gt;</i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;</i>
    <a href="#option" title="Option">Option</a>: <i>
      - &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;</i>
    <a href="#job" title="Job">Job</a>: <i>
      - &lt;a href=&#34;job.md&#34;&gt;Job&lt;/a&gt;</i>
    <a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>: <i>
      - &lt;a href=&#34;nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;</i>
    <a href="#stepplugin" title="StepPlugin">StepPlugin</a>: <i>
      - &lt;a href=&#34;stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;</i>
    <a href="#email" title="Email">Email</a>: <i>
      - &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;</i>
    <a href="#plugin" title="Plugin">Plugin</a>: <i>
      - &lt;a href=&#34;plugin.md&#34;&gt;Plugin&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowConcurrentExecutions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommandOrderingStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueOnError

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThreadCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeFilterExcludePrecedence

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeFilterQuery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveOptionsOrder

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RankAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RankOrder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessOnEmptyNodeFilter

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of &lt;a href=&#34;command.md&#34;&gt;Command&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Job

_Required_: No

_Type_: List of &lt;a href=&#34;job.md&#34;&gt;Job&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeStepPlugin

_Required_: No

_Type_: List of &lt;a href=&#34;nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepPlugin

_Required_: No

_Type_: List of &lt;a href=&#34;stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plugin

_Required_: No

_Type_: List of &lt;a href=&#34;plugin.md&#34;&gt;Plugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

