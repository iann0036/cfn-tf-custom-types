# Terraform::Google::AppEngineApplication FeatureSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#splithealthchecks" title="SplitHealthChecks">SplitHealthChecks</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#splithealthchecks" title="SplitHealthChecks">SplitHealthChecks</a>: <i>Boolean</i>
</pre>

## Properties

#### SplitHealthChecks

Set to false to use the legacy health check instead of the readiness
and liveness checks.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

