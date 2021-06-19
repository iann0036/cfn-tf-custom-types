# TF::GoogleBeta::GoogleCloudTasksQueue

CloudFormation equivalent of google_cloud_tasks_queue

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleCloudTasksQueue",
    "Properties" : {
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#appengineroutingoverride" title="AppEngineRoutingOverride">AppEngineRoutingOverride</a>" : <i>[ <a href="appengineroutingoverridedefinition.md">AppEngineRoutingOverrideDefinition</a>, ... ]</i>,
        "<a href="#ratelimits" title="RateLimits">RateLimits</a>" : <i>[ <a href="ratelimitsdefinition.md">RateLimitsDefinition</a>, ... ]</i>,
        "<a href="#retryconfig" title="RetryConfig">RetryConfig</a>" : <i>[ <a href="retryconfigdefinition.md">RetryConfigDefinition</a>, ... ]</i>,
        "<a href="#stackdriverloggingconfig" title="StackdriverLoggingConfig">StackdriverLoggingConfig</a>" : <i>[ <a href="stackdriverloggingconfigdefinition.md">StackdriverLoggingConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleCloudTasksQueue
Properties:
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#appengineroutingoverride" title="AppEngineRoutingOverride">AppEngineRoutingOverride</a>: <i>
      - <a href="appengineroutingoverridedefinition.md">AppEngineRoutingOverrideDefinition</a></i>
    <a href="#ratelimits" title="RateLimits">RateLimits</a>: <i>
      - <a href="ratelimitsdefinition.md">RateLimitsDefinition</a></i>
    <a href="#retryconfig" title="RetryConfig">RetryConfig</a>: <i>
      - <a href="retryconfigdefinition.md">RetryConfigDefinition</a></i>
    <a href="#stackdriverloggingconfig" title="StackdriverLoggingConfig">StackdriverLoggingConfig</a>: <i>
      - <a href="stackdriverloggingconfigdefinition.md">StackdriverLoggingConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngineRoutingOverride

_Required_: No

_Type_: List of <a href="appengineroutingoverridedefinition.md">AppEngineRoutingOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimits

_Required_: No

_Type_: List of <a href="ratelimitsdefinition.md">RateLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryConfig

_Required_: No

_Type_: List of <a href="retryconfigdefinition.md">RetryConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackdriverLoggingConfig

_Required_: No

_Type_: List of <a href="stackdriverloggingconfigdefinition.md">StackdriverLoggingConfigDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

