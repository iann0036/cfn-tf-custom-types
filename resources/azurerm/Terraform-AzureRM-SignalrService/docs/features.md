# Terraform::AzureRM::SignalrService Features

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flag" title="Flag">Flag</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#flag" title="Flag">Flag</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Flag

The kind of Feature. Possible values are `EnableConnectivityLogs` and `ServiceMode`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

A value of a feature flag. Possible values are `Classic`, `Default` and `Serverless`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

