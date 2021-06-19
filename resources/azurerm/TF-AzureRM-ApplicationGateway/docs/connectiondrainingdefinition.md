# TF::AzureRM::ApplicationGateway ConnectionDrainingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#draintimeoutsec" title="DrainTimeoutSec">DrainTimeoutSec</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#draintimeoutsec" title="DrainTimeoutSec">DrainTimeoutSec</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
</pre>

## Properties

#### DrainTimeoutSec

The number of seconds connection draining is active. Acceptable values are from `1` second to `3600` seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

If connection draining is enabled or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

