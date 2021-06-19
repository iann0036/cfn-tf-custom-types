# TF::AzureRM::ApiManagementApi SubscriptionKeyParameterNamesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#header" title="Header">Header</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#header" title="Header">Header</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
</pre>

## Properties

#### Header

The name of the HTTP Header which should be used for the Subscription Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

The name of the QueryString parameter which should be used for the Subscription Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

