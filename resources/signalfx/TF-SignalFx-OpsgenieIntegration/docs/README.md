# TF::SignalFx::OpsgenieIntegration

SignalFx Opsgenie integration.

~> **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider. Otherwise you'll receive a 4xx error.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::OpsgenieIntegration",
    "Properties" : {
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#apiurl" title="ApiUrl">ApiUrl</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::OpsgenieIntegration
Properties:
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#apiurl" title="ApiUrl">ApiUrl</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ApiKey

The API key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiUrl

Opsgenie API URL. Will default to `https://api.opsgenie.com`. You might also want `https://api.eu.opsgenie.com`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the integration is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the integration.

_Required_: Yes

_Type_: String

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
