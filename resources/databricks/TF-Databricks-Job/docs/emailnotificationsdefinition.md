# TF::Databricks::Job EmailNotificationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#noalertforskippedruns" title="NoAlertForSkippedRuns">NoAlertForSkippedRuns</a>" : <i>Boolean</i>,
    "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ String, ... ]</i>,
    "<a href="#onstart" title="OnStart">OnStart</a>" : <i>[ String, ... ]</i>,
    "<a href="#onsuccess" title="OnSuccess">OnSuccess</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#noalertforskippedruns" title="NoAlertForSkippedRuns">NoAlertForSkippedRuns</a>: <i>Boolean</i>
<a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - String</i>
<a href="#onstart" title="OnStart">OnStart</a>: <i>
      - String</i>
<a href="#onsuccess" title="OnSuccess">OnSuccess</a>: <i>
      - String</i>
</pre>

## Properties

#### NoAlertForSkippedRuns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnFailure

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnStart

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnSuccess

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

